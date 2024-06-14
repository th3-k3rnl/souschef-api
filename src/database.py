from typing import Optional
import mysql.connector

import os
from dotenv import load_dotenv

import database

# Load environment variables from a .env file
load_dotenv()


def create_database_connection() -> (
    Optional[database.PooledMySQLConnection | database.MySQLConnectionAbstract]
):
    SOUS_DATABASE_USERNAME = os.getenv("SOUS_DATABASE_USERNAME")
    SOUS_DATABASE_PASSWORD = os.getenv("SOUS_DATABASE_PASSWORD")
    SOUS_DATABASE_HOST = os.getenv("SOUS_DATABASE_HOST")
    SOUS_DATABASE_NAME = os.getenv("SOUS_DATABASE_NAME")

    if not SOUS_DATABASE_USERNAME:
        print("SOUS_DATABASE_USERNAME not found")
        return None
    if not SOUS_DATABASE_PASSWORD:
        print("SOUS_DATABASE_PASSWORD not found")
        return None
    if not SOUS_DATABASE_HOST:
        print("SOUS_DATABASE_HOST not found")
        return None
    if not SOUS_DATABASE_NAME:
        print("SOUS_DATABASE_NAME not found")
        return None

    return database.login(
        user=SOUS_DATABASE_USERNAME,
        password=SOUS_DATABASE_PASSWORD,
        host=SOUS_DATABASE_HOST,
        database_name=SOUS_DATABASE_NAME,
    )


def login(user: str, password: str, host: str, database_name: str):
    conn = mysql.connector.connect(
        user=user, password=password, host=host, database=database_name
    )
    print(f"server info:\n{conn.get_server_info()}")
    return conn


def logout(conn):
    print("Logging out of database.")
    conn.close()
