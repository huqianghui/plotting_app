import mysql.connector
import pandas as pd
import streamlit as st


mydb = mysql.connector.connect(
    host="codex-sample-server.mysql.database.azure.com",
    user="huqianghui",
    password="XXXXX",
    database="codex-sample"
)

def insert_sql(dataframe):
    mycursor = mydb.cursor()
    table_name = "books"
    columns = ", ".join(dataframe.columns)
    placeholders = ", ".join(["%s"] * len(dataframe.columns))
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    values = [tuple(row) for row in dataframe.values]
    mycursor.executemany(query, values)
    print("Number of rows inserted: %d" % mycursor.rowcount)
    mycursor.close()
    mydb.commit()
    mydb.close()


@st.cache_data
def read_pd_byTableName(tableName):
    query = "SELECT * FROM " +  tableName
    mydb.connect()
    df = pd.read_sql(query, mydb)
    mydb.close()
    return df

