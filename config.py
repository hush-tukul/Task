import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # SQLite database URI (relative path)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # SQLite database file will be created in the current directory
    SQLALCHEMY_TRACK_MODIFICATIONS = False
