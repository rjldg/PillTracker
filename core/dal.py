from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
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
        session.commit()
        return result
    
    def create_user(fn, ln, username, email, pw, gender):
        query = text("CALL createuser(:fn, :ln, :username, :email, :password, :gender)")
        parameters = {"fn": fn, "ln": ln, "username": username, "email": email, "password": pw, "gender": gender}
        try:
            session.execute(query, parameters)
            session.commit()
            return True
        except IntegrityError as e:
            print(f"Error: {e}")
            return False
        except Exception as e:
            session.rollback()
            print(f"Error: {e}")
            return False
    
    '''
    "SELECT * FROM user WHERE id=:param",
        {"param":5}

    text("SELECT * FROM KLSE WHERE Stock LIKE :param"),{"param":Stock}
    '''
