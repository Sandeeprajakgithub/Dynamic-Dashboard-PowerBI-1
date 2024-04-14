import pandas as pd
import mysql.connector

def push_to_mysql(excel_file, table_name, host, user, password, database):
    df = pd.read_excel(excel_file)
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()
    cols = ','.join(df.columns)
    placeholders = ','.join(['%s'] * len(df.columns))
    sql = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
    data = [tuple(row) for row in df.values]
    cursor.executemany(sql, data)
    conn.commit()
    cursor.close()
    conn.close()

excel_file = 'your_excel_file.xlsx'
table_name = 'your_table_name'
host = 'localhost'
user = 'your_username'
password = 'your_password'
database = 'your_database_name'

push_to_mysql(excel_file, table_name, host, user, password, database)
