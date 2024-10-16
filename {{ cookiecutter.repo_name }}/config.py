from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database URL as specified in .env file
    db_url: str

    # Key to access git as specified in .env file
    git_key: str

    class Config:
        # Load environment variables from .env file
        env_file = ".env"
        env_file_encoding = "utf-8"

# Instantiate settings
settings = Settings()

"""
from general.functions import *
from economics.functions import *
from outliers.functions import *
from spatial_general.functions import *
from spatial_interpolate.functions import *
from spatial_plots.functions import *
from spatial_reallocation.functions import *
from spatial_census_process.functions import *
from adoption_curves.functions import *
from fuzzy_matching.functions import *
from data_products.functions import *

source /Users/jancg/opt/anaconda3/bin/activate
conda init 

alembic revision --autogenerate
alembic upgrade head

"""
