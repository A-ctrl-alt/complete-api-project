from sqlalchemy import create_engine
from sqlmodel import SQLModel,Session
from database.models import Shipments


e=create_engine(
    url="sqlite:///supply.db",echo=True,connect_args={"check_same_thread":False}
    )

def create_db_and_tables():
    SQLModel.metadata.create_all(bind=engine)

def get_session():
    with Session(engine)as db:
        yield db    


