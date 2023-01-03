import os
from model import data_model
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
model = data_model

dotenv_data_path = os.getenv('data_path')

path = model.ReadingData(dotenv_data_path)
model.ShowColums(path)