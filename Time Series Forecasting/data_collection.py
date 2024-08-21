import pandas as pd
import requests
from io import StringIO
from configparser import ConfigParser
import os
import re
from sqlalchemy import create_engine, text
import time
dir_name = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = ConfigParser()
config.read('./config.ini')

MANDI_API = config.get("Credentials","mandi_api")
indian_states = eval(config.get("Credentials","indian_states"))
union_territories = eval(config.get('Credentials','union_territories'))
USER = config.get('Credentials','mysql_user')
PASSWORD = config.get('Credentials','mysql_password')
HOST = config.get('Credentials','mysql_host')
PORT = config.get('Credentials','mysql_port')
DATABASE = config.get('Credentials','mysql_database')
TABLE = config.get('Credentials','mysql_table')

def dump_mysql(df: pd.DataFrame) -> None:
    mysql_engine = create_engine(f'mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/')
    
    with mysql_engine.connect() as connection:
        connection.execute(text(f'CREATE DATABASE IF NOT EXISTS {DATABASE}'))
    time.sleep(10)
    mysql_engine = create_engine(f'mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')
   
    df.to_sql('mandi_price', con=mysql_engine, if_exists='append', index=False)


def column_renamer(df_all: pd.DataFrame) -> pd.DataFrame:
    df_all.columns = map(str.lower, df_all.columns)
    
    # Use regex to find columns with 'min', 'max', or 'mode' substring
    min_max_mode_columns = [col for col in df_all.columns if any(sub in col for sub in ['min', 'max', 'modal'])]
    
    # Create a mapping to rename columns
    column_mapping = {col: re.sub(r'(min|max|modal)', r'\1', col) for col in min_max_mode_columns}
    
    # Rename columns with 'min', 'max', or 'mode' substring
    df_all.rename(columns=column_mapping, inplace=True)
    
    # Create new columns 'min', 'max', and 'mode' and copy data
    for substring in ['min', 'max', 'modal']:
        matching_columns = [col for col in df_all.columns if substring in col]
        if matching_columns:
            df_all[substring] = df_all.get(substring, df_all[matching_columns[0]])
            df_all.drop(columns=matching_columns[0], inplace=True)

    df_all.rename(columns=lambda x: x.replace(' ', '_'), inplace=True)

    return df_all

def data_collector():
    all_states = list(indian_states+union_territories)
    df_all = pd.DataFrame()
    for state in all_states:
        try:
            response = requests.get(f"https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key={MANDI_API}&format=csv&filters%5Bstate%5D={state}")
            data_io = StringIO(response.text)
            df = pd.read_csv(data_io)
            df_all = pd.concat([df_all,df],axis=0).reset_index(drop=True)
        except:
            pass

    df_all = column_renamer(df_all)
    # Drop the old columns
    dump_mysql(df_all)

    

    

if __name__ =="__main__":
    data_collector()
    # pass
    
