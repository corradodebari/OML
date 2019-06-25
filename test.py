from __future__ import print_function
import os
import pandas as pd
import cx_Oracle
# Connect as user 
connection = cx_Oracle.connect("myuser", "mypassword", "my_tnsnames")

query = """
    SELECT * 
    FROM  sh.supplementary_demographics 
    WHERE occupation !='?' """

df_ora = pd.read_sql(query,con=connection)
print(df_ora.columns)
print(df_ora.head())

name="ex_supplementary.csv"
df_ora.to_csv(name)
