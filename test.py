'''
SETUP on ADWH
------------
Create in ADWH a new table with this sql command: 

create table logsData as select * from sh.supplementary_demographics where rownum = -1;


DESCRIPTION
-----------
Connection to an ADWH, get as Pandas dataframe a table, Export as CSV locally, import CSV in a Pandas dataframe, 
cleaning, bulk insert in a new ADWH table

'''




from __future__ import print_function
import math
import os
import pandas as pd
import cx_Oracle
# Connect as user "hr" with password "welcome" to the "oraclepdb" service running on this computer.
connection = cx_Oracle.connect("USER", "**********", "CONNECTION")

query = """
    SELECT * 
    FROM  sh.supplementary_demographics 
    WHERE occupation !='?' """

df_ora = pd.read_sql(query,con=connection)
print(df_ora.columns)
print(df_ora.head())

name="ex_products"
#df_ora.to_sql(name,con=connection,if_exists="replace")
df_ora.to_csv("ex_products.csv")


#dfIn = pd.read_csv("ex_products.csv", header=None , sep=',', lineterminator='\n')
dfIn = pd.read_csv("ex_products.csv", sep=',', lineterminator='\n')

dfIn.rename(columns={'Unnamed: 0':'INDEX'}, inplace=True)
print(dfIn.columns)

Row_list =[] 
  
# Iterate over each row 
for index, r in dfIn.iterrows(): 
    # Create list for the current row 

    my_list =[ r.CUST_ID,r.EDUCATION,r.OCCUPATION,r.HOUSEHOLD_SIZE,r.YRS_RESIDENCE,r.AFFINITY_CARD,r.BULK_PACK_DISKETTES,r.FLAT_PANEL_MONITOR,r.HOME_THEATER_PACKAGE,r.BOOKKEEPING_APPLICATION,r.PRINTER_SUPPLIES,r.Y_BOX_GAMES,r.OS_DOC_SET_KANJI,r.COMMENTS] 
      
    # append the list to the final list 
    clean=['' if x!=x else x for x in my_list]

    Row_list.append(tuple(clean)) 
    if index > 10:
        break

# myRow = Row_list[0]

# Print the list 
print(Row_list) 
cursor = connection.cursor()

#cursor.execute("insert into logsData  values (:1, :2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14)",myRow)
cursor.executemany("insert into logsData  values (:1, :2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14)",Row_list)
connection.commit()
