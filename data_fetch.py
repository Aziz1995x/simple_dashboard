import pyodbc
import pandas as pd

def fetch_data():
    # Define connection string
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=LAPTOP-CILTFSV6\SQLEXPRESS;"
        "DATABASE=pubs;"
        "Trusted_Connection=yes;"
    )

    # Connect to SQL Server
    conn = pyodbc.connect(conn_str)

    # Query the database
    query = "SELECT * FROM employee"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

