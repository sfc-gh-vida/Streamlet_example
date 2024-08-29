import os
import snowflake.connector
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def get_snowflake_connection():
    """
    Establishes a connection to Snowflake using environment variables.
    """
    return snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA")
    )

def fetch_snowflake_version():
    """
    Fetches and returns the current version of Snowflake.
    """
    conn = get_snowflake_connection()
    cur = conn.cursor()
    cur.execute("SELECT CURRENT_VERSION();")
    version = cur.fetchone()[0]
    cur.close()
    conn.close()
    return version

def fetch_user_data():
    """
    Fetches data from the 'user' table in Snowflake.
    """
    conn = get_snowflake_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM user;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def insert_user_data(user_id, user_name, created_on):
    """
    Inserts a new user into the Snowflake 'user' table.
    """
    conn = get_snowflake_connection()
    cur = conn.cursor()
    cur.execute(f"""
        INSERT INTO user (id, name, created_on) VALUES 
        ({user_id}, '{user_name}', '{created_on}');
    """)
    conn.commit()
    cur.close()
    conn.close()

def fetch_last_user_id():
    """
    Fetches the last user ID from the Snowflake 'user' table.
    Returns 0 if the table is empty.
    """
    conn = get_snowflake_connection()
    cur = conn.cursor()
    cur.execute("SELECT MAX(id) FROM user;")
    last_id = cur.fetchone()[0]
    cur.close()
    conn.close()
    return last_id if last_id else 0
