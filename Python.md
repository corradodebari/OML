# Use Python/Pandas to access Oracle Autonomous DB
This note helps who wants to setup an environment for Machine Learning project in Python leveranging dataset on Oracle Autonomous DB. This works on a Ubuntu 18.x and uses ["cx_oracle"](https://oracle.github.io/python-cx_Oracle/) Python libraries to connect Oracle DB and 

## 1. Install cx_oracle 
Instant client download from: https://www.oracle.com/database/technologies/instant-client/downloads.html
        instantclient-basic-linux.x64-18.5.0.0.0dbru.zip

https://gist.github.com/kimus/10012910
```
sudo apt-get install build-essential unzip python-dev libaio-dev
export ORACLE_HOME=$(pwd)/instantclient_18_5
```
update ~/.bashrc :
```
export ORACLE_HOME=/home/ubuntu/instantclient_18_5
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME
```
create or update:
 /etc/ld.so.conf.d/oracle.conf
putting this line:
/home/ubuntu/instantclient_18_5

```
#sudo ldconfig 
#pip install cx_oracle
```
download wallet and unzip

copy all the files in:
#cp wallet/* ./instantclient_18_5/network/admin/

run:

["How To Train an Object Detection Classifier for Multiple Objects Using TensorFlow (GPU) on Windows 10"](https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10#3-gather-and-label-pictures) I've defined a Docker image to simplify the training phase.    
To proceed you need to follow these steps:

## 1. Get a Cloud Node
Get a certified cloud image for [NVIDIA GPU Cloud](https://ngc.nvidia.com) on [Oracle Cloud Infrastructure](https://docs.cloud.oracle.com/iaas/Content/Compute/References/ngcimage.htm):

* US Region: **us-ashburn-1** 
*ocid1.image.oc1.iad.aaaaaaaaikn6ub6heefqxbe5fkiv4otbfe6ivza6y7di5khnkxkyvf2bkdta*
* EU Region: **eu-frankfurt-1**  
*ocid1.image.oc1.eu-frankfurt-1.aaaaaaaauwuafl6uze6bnusphnn6y2mr5y7ajavx4kza7glyrqggxlnbo4zq*    

These are Ubuntu 16.04.3 images, with **nvidia-docker** pre-configured to use GPU shapes: no other configurations needed.

## 2. Github project download
With command:
```
#git clone https://github.com/corradodebari/Object-Detection.git
```


