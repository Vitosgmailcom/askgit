
import os
from dotenv import load_dotenv
load_dotenv()

def Credentials():

    DB_USER = os.environ["DB_USER"]
    DB_PASS = os.environ["DB_PASS"]
    DB_NAME = os.environ["DB_NAME"]
    DB_PORT = os.environ["DB_PORT"]
    DB_HOST = os.environ["DB_HOST"]

    if not DB_USER and not DB_PASS:
        raise Exception(f"DB_USER and DB_PASS must be set")
    else:
        credent_info = {

            "db_user": DB_USER,
            "db_pass": DB_PASS,
            "db_name": DB_NAME,
            "db_port": DB_PORT,
            "db_host": DB_HOST
        }
        return credent_info





