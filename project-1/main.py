from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"status":"UP"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app"
    )