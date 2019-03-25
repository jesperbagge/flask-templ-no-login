import os
from dotenv import load_dotenv

# load .env file
load_dotenv(override=True)


class Settings:
    SECRET_KEY = os.getenv('SECRET_KEY')
