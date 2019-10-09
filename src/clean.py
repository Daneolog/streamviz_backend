# %%
import sys
sys.path
sys.path.append('..')

# %%
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

def clean(filename):
    df = pd.read_csv(filename)
    df['date'] = pd.to_datetime(df[['year', 'month', 'day']], errors='coerce')

    # rename columns
    df.rename(columns={'visual_score': 'Visual Score', 'biological_score': 'Biological Score', 'conductivity.uscm': 'Conductivity', 'turbidity.ntu': 'Turbidity', 'po4.mgL': 'Phosphate',
                    'no3.mgL': 'Nitrate', 'temperature.c': 'Temperature', 'e.coli.cfu': 'E.coli', 'ecoli.method.known': 'E.coli Method'}, inplace=True)

    df.drop(['WS', 'ID', 'month', 'year', 'day', 'quarter'], axis=1, inplace=True)

    return df

if __name__ == "__main__":
    df = clean('UOWN_data_master_04nov2018.csv')

    df.to_csv('data/UOWN_data_master_04nov2018_clean.csv', index=False)
    conn = create_engine('mysql+pymysql://root:password@localhost/streamviz')
    df.to_sql('stream', conn, index=False, if_exists='replace')

# %%
