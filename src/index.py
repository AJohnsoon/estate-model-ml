import os
from model import data_model
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

env_path = os.getenv('csv_data_path')
data_model.DataAnalysis(env_path)