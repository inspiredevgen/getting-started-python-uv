from models import User
from database import SessionLocal, engine, Base

#Create Tables
Base.metadata.create_all(bind=engine)

#Seed the database with initial data

def seed_database():
    session = SessionLocal()

    #check if the data already exists to avoid duplication
    if not session.query(User).first():
        # add sample users
        session.add(User(id=101, name="Victoria", account_status="Active", subscription_plan="Pro Plan"))
        session.add(User(id=102, name="Alex", account_status="Active", subscription_plan="Pro Plan"))
        session.add(User(id=103, name="John", account_status="Active", subscription_plan="Free Plan"))
        session.add(User(id=104, name="Luke", account_status="Active", subscription_plan="Enterprise Plan"))
        session.add(User(id=105, name="Lance", account_status="Active", subscription_plan="Enterprise Plan"))
        session.add(User(id=106, name="Pauline", account_status="Active", subscription_plan="Free Plan"))
        session.add(User(id=107, name="Rob", account_status="Active", subscription_plan="Enterprise Plan"))
        session.add(User(id=108, name="Maurice", account_status="Active", subscription_plan="Pro Plan"))
        session.add(User(id=109, name="Axel", account_status="Active", subscription_plan="Pro Plan"))
        session.add(User(id=110, name="Bill", account_status="Active", subscription_plan="Free Plan"))
        session.add(User(id=111, name="Gedeon", account_status="Active", subscription_plan="Enterprise Plan"))
        session.add(User(id=112, name="Donald", account_status="Active", subscription_plan="Pro Plan"))
        session.commit()
        print("Database seed: Completed Successfully!")
    else:
        print("Database already seeded")
        print("Database seed: no action required")
    
    session.close()

if __name__ == '__main__':
    seed_database()