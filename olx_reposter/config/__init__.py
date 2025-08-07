import os

from dotenv import load_dotenv

load_dotenv()
pg_host = os.getenv('POSTGRES_HOST')
pg_user = os.getenv('POSTGRES_USER')
pg_password = os.getenv('POSTGRES_PASSWORD')
pg_database = os.getenv('POSTGRES_DATABASE')
