
import os
from dotenv import load_dotenv
load_dotenv()

def Credentials():

    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASS")
    db_name = os.getenv("DB_NAME")
    db_port = os.getenv("DB_PORT")
    db_host = os.getenv("DB_HOST")

    if not DB_USER and not DB_PASS:
        raise Exception(f"DB_USER and DB_PASS must be set")
    else:
        credent_info = {

            "db_user": db_user,
            "db_pass": db_pass,
            "db_name": db_name,
            "db_port": db_port,
            "db_host": db_host
        }
        return credent_info





