import pandas as pd
import psycopg2
from psycopg2 import sql
from psycopg2.extras import execute_values
import os
#Read the CSV file
csv_file_path = r"files/sample.csv"
df = pd.read_csv(csv_file_path)

#Generate the CREATE TABLE SQL statement
def generate_create_table_sql(df, table_name):
    sql = f"CREATE TABLE {table_name} (\n"
    for column in df.columns:
        if df[column].dtype == 'int64':
            sql += f"    {column} INTEGER,\n"
        elif df[column].dtype == 'float64':
            sql += f"    {column} FLOAT,\n"
        else:
            sql += f"    {column} TEXT,\n"
    sql = sql.rstrip(',\n') + "\n);"
    return sql

table_name = 'persons'
create_table_sql = generate_create_table_sql(df, table_name)

#Database connection parameters
db_params = {
    'dbname': 'Sample',
    'user': 'postgres',
    'password': os.getenv('PGPASSWORD'),
    'host': 'localhost',
    'port': '5432'
}

#Connect to the database
conn = psycopg2.connect(**db_params)
cur = conn.cursor()

#Create the table
cur.execute(create_table_sql)

#Insert the data
insert_sql = f"INSERT INTO {table_name} ({', '.join(df.columns)}) VALUES %s"
#Here %s is a placeholder for the values to be inserted.
data_tuples = [tuple(x) for x in df.to_numpy()]

execute_values(cur, insert_sql, data_tuples)

#Commit the changes and close the connection
conn.commit()
cur.close()
conn.close()
