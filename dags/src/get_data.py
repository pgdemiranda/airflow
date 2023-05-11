import sqlite3
import pandas as pd

def run_query():
    conn= sqlite3.connect('\\wsl.localhost\Ubuntu\home\miranda\airflow\dags\src\data\db_olist.sqlite')
    query='SELECT * FROM order_reviews LIMIT10'
    
    # execute query
    pd.read_sql_query(query, conn)
    
    # save data
    df.to_csv('\\wsl.localhost\Ubuntu\home\miranda\airflow\dags\src\data\sqlite_data.csv', index = False)
    
    #close connection
    conn.close()
    
    return None