import pandas as pd 
from content_scraper import get_table_contentTXT as get_table
import csv
import json

content_list = get_table()

def convert_to_json():
    

def set_data_csv(file_name: str, columns: int, data: dict) ->str:
    with open(json_file, encoding='utf-8') as file:
        df = pd.read_json(file)
    