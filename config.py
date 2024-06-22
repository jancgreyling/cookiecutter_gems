import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database URL as specified in .env file
    db_url: str

    # Key to access git as specified in .env file
    git_key: str

    # Path to data folder
    data_products: str

    # Define the global working directory
    project_dir: str = os.path.abspath(os.path.join(os.path.dirname(__file__)))

    class Config:
        # Load environment variables from .env file
        env_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '.env')
        env_file_encoding = 'utf-8'

# Instantiate settings
settings = Settings()