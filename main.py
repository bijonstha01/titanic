# main.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
import json

app = FastAPI()

# SQLite Database Setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define Titanic Table
class Titanic(Base):
    _tablename_ = "titanic"
    id = Column(Integer, primary_key=True, index=True)
    PassengerId = Column(Integer)
    Survived = Column(Integer)
    Pclass = Column(Integer)
    Name = Column(String)
    Sex = Column(String)
    Age = Column(Float)
    SibSp = Column(Integer)
    Parch = Column(Integer)
    Ticket = Column(String)
    Fare = Column(Float)
    Cabin = Column(String)
    Embarked = Column(String)

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Parse Titanic CSV and insert into SQLite
df_titanic = pd.read_csv("titanic.csv")
df_titanic.to_sql("titanic", engine, index=False, if_exists="replace")

# Titanic API Endpoint
@app.get("/titanic")
def read_titanic_data():
    db = SessionLocal()
    try:
        titanic_data = db.query(Titanic).all()
    finally:
        db.close()
    return titanic_data


# UBO JSON Parsing
def parse_ubo_json(file_path):
    with open(file_path, "r") as file:
        ubo_data = json.load(file)

    # Use pandas to flatten nested JSON structure
    df_ubo = pd.json_normalize(ubo_data)
    return df_ubo

# Example Usage
file_path = "ubo.json"
ubo_dataframe = parse_ubo_json(file_path)
print(ubo_dataframe)
