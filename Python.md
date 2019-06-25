# Use Python/Pandas to access Oracle Autonomous DB
This note helps who wants to setup an environment for a Machine Learning project in Python, leveraging dataset on Oracle Autonomous DB. This works on a OCI VM.Standard2.2 shape, with Ubuntu 18.x, and uses ["cx_oracle"](https://oracle.github.io/python-cx_Oracle/) Python libraries to connect Oracle DB and ["Oracle Instant Client"](https://www.oracle.com/database/technologies/instant-client.html).

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
From Autonomous Database/Autonomous Database Details/DB Connection, Download Client Credentials Wallet and unzip in a directory. Copy all the files in:
./instantclient_18_5/network/admin/

run:




