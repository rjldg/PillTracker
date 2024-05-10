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

# For successful database connection indicator
try:
    with engine.connect() as connectionString:
        print('Successfully connected to the PostgreSQL database')
except Exception as ex:
    print(f'Sorry failed to connect: {ex}')


""" DATA ACCESS LAYER """

class DAL:

    def validate_login(username, pw_input):
        result = session.execute(func.public.validate_login(username, pw_input)).scalar()
        session.commit()
        return result
    
    def increment_pills_taken(pill_id, date_today):
        new_value = session.execute(func.public.increment_pills_taken(pill_id, date_today)).scalar()
        session.commit()   
        return new_value
    
    def decrement_pills_taken(pill_id, date_today):
        new_value = session.execute(func.public.decrement_pills_taken(pill_id, date_today)).scalar()
        session.commit()   
        return new_value
    
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
        
    def create_pill(username, pn, pta, pdi):
        '''Read user_ID corresponding to logged in user's username'''
        get_user_id_query = text(f"SELECT \"User_ID\" FROM \"PillTracker_User\" WHERE \"Username\" = '{username}';")
        user_id = session.execute(get_user_id_query).scalar()
        session.commit()

        query = text("CALL createpill(:user_id, :pill_name, :pill_total_amt, :pill_daily_intake, :pill_notes);")
        parameters = {"user_id": user_id, "pill_name": pn, "pill_total_amt": pta, "pill_daily_intake": pdi, "pill_notes": ""}
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
        
    def update_user(loggedin_username, fn, ln, username, email, pw, gender):
        isUsernameChanged = False
        isPasswordChanged = False

        try:
            if fn != "":
                update_fn = text(f"UPDATE \"PillTracker_User\" SET \"First_Name\" = '{fn}' WHERE \"Username\" = '{loggedin_username}';")
                session.execute(update_fn)
                session.commit()
            
            if ln != "":
                update_ln = text(f"UPDATE \"PillTracker_User\" SET \"Last_Name\" = '{ln}' WHERE \"Username\" = '{loggedin_username}';")
                session.execute(update_ln)
                session.commit()
            
            if username != "":
                update_username = text(f"UPDATE \"PillTracker_User\" SET \"Username\" = '{username}' WHERE \"Username\" = '{loggedin_username}';")
                session.execute(update_username)
                session.commit()
                isUsernameChanged = True
            
            if email != "":
                update_email = text(f"UPDATE \"PillTracker_User\" SET \"Email\" = '{email}' WHERE \"Username\" = '{loggedin_username}';")
                session.execute(update_email)
                session.commit()
            
            if pw != "":
                update_pw = text(f"UPDATE \"PillTracker_User\" SET \"Password\" = '{pw}' WHERE \"Username\" = '{loggedin_username}';")
                session.execute(update_pw)
                session.commit()
                isPasswordChanged = True
            
            if gender != "":
                update_gender = text(f"UPDATE \"PillTracker_User\" SET \"Gender\" = '{gender}' WHERE \"Username\" = '{loggedin_username}';")
                session.execute(update_gender)
                session.commit()
            
            return (True, isUsernameChanged, isPasswordChanged)
        except Exception as e:
            session.rollback()
            print(f"Error: {e}")
            return False

    def read_pills_home_page(username:str):
        '''Read user_ID corresponding to logged in user's username'''
        get_user_id_query = text(f"SELECT \"User_ID\" FROM \"PillTracker_User\" WHERE \"Username\" = '{username}';")
        user_id = session.execute(get_user_id_query).scalar()
        session.commit()

        '''Get pill information from the user_ID that was read'''
        get_pillsInfo_query = text(f"SELECT \"Pill_Name\", \"Pills_Taken\", \"Pill_ID\", \"Pill_Total_Amount\" FROM \"Pills\" WHERE \"User_ID\" = {user_id};")
        pillsInfo = session.execute(get_pillsInfo_query).fetchall()
        session.commit()
        pillInfo = [list(row) for row in pillsInfo]

        return pillInfo
    
    def read_pills_schedule_page(username:str):
        '''Read user_ID corresponding to logged in user's username'''
        get_user_id_query = text(f"SELECT \"User_ID\" FROM \"PillTracker_User\" WHERE \"Username\" = '{username}';")
        user_id = session.execute(get_user_id_query).scalar()
        session.commit()

        '''Get pill information from the user_ID that was read'''
        get_pillsInfo_query = text(f"SELECT \"Pill_Name\", \"Pill_Daily_Intake\", \"Pill_Total_Amount\",\"Pill_ID\" FROM \"Pills\" WHERE \"User_ID\" = {user_id};")
        pillsInfo = session.execute(get_pillsInfo_query).fetchall()
        session.commit()
        pillInfo = [list(row) for row in pillsInfo]

        return pillInfo
    
    def delete_pill(pill_id):
        query = text(f"DELETE FROM \"Pills\" WHERE \"Pill_ID\" = {pill_id}")
        try:
            session.execute(query)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            print(f"Error: {e}")
            return False



    
    '''
    "SELECT * FROM user WHERE id=:param",
        {"param":5}

    text("SELECT * FROM KLSE WHERE Stock LIKE :param"),{"param":Stock}
    '''
