# DAL - Data Access Layer

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

connectionString = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(connectionString)
Session = sessionmaker(bind=engine)
session = Session()

'''
# For testing the connection
try:
    with engine.connect() as connectionString:
        print('Successfully connected to the PostgreSQL database')
except Exception as ex:
    print(f'Sorry failed to connect: {ex}')
'''

""" DATA ACCESS LAYER """
class DAL:

    def validate_login(username, pw_input):
        result = session.execute(func.public.validate_login(username, pw_input)).scalar()
        return result