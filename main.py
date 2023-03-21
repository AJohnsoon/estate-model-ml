import os
import app
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

env_path = os.getenv('csv_data_path')
app.data_analysis(env_path)