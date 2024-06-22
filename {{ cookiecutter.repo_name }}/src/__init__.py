import os
import sys
from sqlalchemy import create_engine

# Set the base directory relative to the current working directory
base_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))
sys.path.append(base_dir)

# Import settings from a configuration file within the package
from src.config import settings

# Create a database engine using a URL from the settings
engine = create_engine(settings.db_url)

# Set a project directory from settings
project_dir = settings.project_dir

from general.functions import *
from economics.functions import *
from outliers.functions import *
from spatial_general.functions import *
from spatial_interpolate.functions import *
from spatial_plots.functions import *
from spatial_reallocation.functions import *
from spatial_census_process.functions import *
from spatial_crops.functions import *