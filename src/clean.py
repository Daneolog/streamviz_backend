# %%
import sys
sys.path
sys.path.append('..')

# %%
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

df = pd.read_csv('data/UOWN_data_master_04nov2018.csv')

# %%
# convert m/y/d to actual date column
df['date'] = pd.to_datetime(df[['year', 'month', 'day']], errors='coerce')
df['date']

# rename columns
df.rename(columns={'conductivity.uscm': 'conductivity', 'turbidity.ntu': 'turbidity', 'po4.mgL': 'phosphate',
                   'no3.mgL': 'nitrate', 'temperature.c': 'temperature', 'e.coli.cfu': 'ecoli', 'ecoli.method.known': 'ecoli_method'}, inplace=True)
df

# %%
df.drop(['WS', 'ID', 'month', 'year', 'day', 'quarter'], axis=1, inplace=True)

# %%
df.to_csv('data/UOWN_data_master_04nov2018_clean.csv', index=False)
conn = create_engine('mysql+pymysql://root:password@localhost/streamviz')
df.to_sql('stream', conn, index=False, if_exists='replace')

# %%


# %%
