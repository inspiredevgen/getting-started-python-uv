import instructor
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPEN_AI_KEY")


class Person(BaseModel):
    name: str
    age: int
    politicalParty: str


client = instructor.from_openai(OpenAI(api_key=api_key))



person = client.chat.completions.create(
    model="gpt-4o-mini",
    response_model=list[Person],
    messages=[
        {"role": "user", 
        "content": "List 5 famous politicians with their name, age, and their political party."}
    ],
)
#print(person)  # Person(name='John', age=30, occupation='software engineer')

for p in person:
    print(f"Name: {p.name}, Age: {p.age}, Occupation: {p.politicalParty}")