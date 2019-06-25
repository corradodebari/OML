Install cx_oracle and use pandas on Autonomous ADWH

Instant client download from: https://www.oracle.com/database/technologies/instant-client/downloads.html
        instantclient-basic-linux.x64-18.5.0.0.0dbru.zip

https://gist.github.com/kimus/10012910

sudo apt-get install build-essential unzip python-dev libaio-dev
export ORACLE_HOME=$(pwd)/instantclient_18_5

update ~/.bashrc :

export ORACLE_HOME=/home/ubuntu/instantclient_18_5
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME

create or update:
 /etc/ld.so.conf.d/oracle.conf
putting this line:
/home/ubuntu/instantclient_18_5

#sudo ldconfig 
#pip install cx_oracle

download wallet and unzip

copy all the files in:
#cp wallet/* ./instantclient_18_5/network/admin/

run:
