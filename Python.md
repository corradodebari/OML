# Use Python/Pandas to access Oracle Autonomous DB
This note helps who wants to setup an environment for a Machine Learning project in Python, leveraging dataset on Oracle Autonomous DB. This works on a **OCI** **VM.Standard2.2** shape, with **Ubuntu 18.x**, and uses ["cx_oracle"](https://oracle.github.io/python-cx_Oracle/) Python libraries to connect Oracle DB and ["Oracle Instant Client"](https://www.oracle.com/database/technologies/instant-client.html).

## 1. Install Oracle Instant Client
Download from ["here"](https://www.oracle.com/database/technologies/instant-client/downloads.html)
the right package for Autonomous DB: **instantclient-basic-linux.x64-18.5.0.0.0dbru.zip**   
Unzip in a directory, for example **/home/ubuntu/instantclient_18_5/** and:

```
# sudo apt-get install build-essential unzip python-dev libaio-dev
# export ORACLE_HOME=$(pwd)/instantclient_18_5
```
Update ~/.bashrc :
```
# export ORACLE_HOME=/home/ubuntu/instantclient_18_5
# export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME
```
Create or update:
```
 /etc/ld.so.conf.d/oracle.conf
```
putting this line inside:
```
/home/ubuntu/instantclient_18_5
```
Then 
```
# sudo ldconfig 
```
## 2. Install cx_Oracle:
Eventually install **pip** if not present. Then:
```
# pip install cx_oracle
```
## 3. Configure connection:
From **Autonomous Database/Autonomous Database Details/DB Connection**, Download Client Credentials Wallet. Take notes about one of the TNS names of Connection Strings to use later in the code.   
Unzip in a directory and copy all the files in:    
```
./instantclient_18_5/network/admin/   
```
In [**test.py**](test.py)  file change:   
```
connection = cx_Oracle.connect("myuser", "mypassword", "my_tnsnames")
```
with proper credentials and TNS names from Connection strings, this one normally .._low, _high 

Note that the connection is used by Pandas to create a Dataframe, and it is saved at the end as a _csv file.
Then run python script to test the env:
```
ubuntu@cdb-compute:~$ python myscript.py
Index([u'CUST_ID', u'EDUCATION', u'OCCUPATION', u'HOUSEHOLD_SIZE',
       u'YRS_RESIDENCE', u'AFFINITY_CARD', u'BULK_PACK_DISKETTES',
       u'FLAT_PANEL_MONITOR', u'HOME_THEATER_PACKAGE',
       u'BOOKKEEPING_APPLICATION', u'PRINTER_SUPPLIES', u'Y_BOX_GAMES',
       u'OS_DOC_SET_KANJI', u'COMMENTS'],
      dtype='object')
   CUST_ID EDUCATION OCCUPATION  ... Y_BOX_GAMES  OS_DOC_SET_KANJI  COMMENTS
0   102547      10th      Other  ...           1                 0      None
1   101050      10th      Other  ...           1                 0      None
2   100040      11th      Sales  ...           1                 0      None
3   102117   HS-grad    Farming  ...           1                 0      None
4   101074      10th    Handler  ...           1                 0      None

[5 rows x 14 columns]

```


