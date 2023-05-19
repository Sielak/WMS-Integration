# Overview
### Description
This project is used to integrate Jeeves and OnGoing WMS.  
It use [FastAPI](https://fastapi.tiangolo.com/) to create endpoints and [Zeep](https://docs.python-zeep.org/en/master/) to make SOAP requests to OnGoing.  
From Jeeves DB it uses `q_hl_dp_data` to store integration logs from and to OnGoing.  
### Process description
**Jeeves to OnGoing**
1. Jeeves Trigger (insert small amount of data to `q_hl_dp_data`)
2. Job `WMS2 - Transfer to OnGoing` have 3 steps (Article, InOrders, Orders) every with two actions  
2.1 Generate XML based on data in `q_hl_dp_data` and save it in that table (Text7)  
2.2 Send HTTP request to FastAPI with this XML from `q_hl_dp_data`  
4. Result is saved in this same row in `q_hl_dp_data` (column ResultXML and/or Message)  

**OnGoing to Jeeves**  
1. HTTP request is triggered (from job or wso2 webhook)
2. FastApi fetch data from OnGoing and saves it in `q_hl_dp_data`
3. The appropriate procedure is run on the database side to update jeeves
4. Result of such update is logged in `q_hl_dp_data` (column EI / Message)

### Dependencies
Linux server
```
Mapped network drives in media folder that are used in endpoint UploadOrderFile
current PDM folder --> //ew1-fil-101/OneJeeves/edm/erp/
```
SQL DB
```
jobs:
    WMS2 - Transfer to OnGoing
    WMS2 - GetInOrdersByQuery
    WMS2 - GetInventoryChanges
    WMS2 - GetInventoryItems
views:
    WMS2_stock_balance
procedures:
    q_hl_wms2_doStockTransactions
    q_hl_wms2_doStockTransactions_xarsm
    q_hl_wms2_doStockTransactions_xinvj
    q_hl_wms2_generateProcessArticleXML
    q_hl_wms2_generateProcessInOrderXML
    q_hl_wms2_generateProcessOrderXML
    q_hl_wms2_transfer_articlexml
    q_hl_wms2_transfer_inorderxml
    q_hl_wms2_transfer_orderXML
    q_hl_wms2_updatePO
    q_hl_wms2_updateSO
sql user with roles:
    db_datareader
    db_datawriter
    public
```
Jeeves
```
jvss CUSTOM_HL559 ON
envconfig
```
WSO2
```
Endpoint for OnGoing visible from outside of HL network passing request internally:

https://esb-endpoint-703.hl-display.com/services/WMS_OnGoingWebHook_2_PythonAPI/{{env}}/{{foretagkod}}

Routing logic:

IF {{env}} == PROD:
	IF {{foretagkod}} == 0000:
		GET --> {{url_for_prod}}/openapi.json
	ELSE
		POST --> {{url_for_prod}}/GetOrderByOrderNumber?foretagkod={{foretagkod_value}}
ELIF {{env}} == UAT:
	IF {{foretagkod}} == 0000:
		GET --> {{url_for_UAT}}/openapi.json
	ELSE
		POST --> {{url_for_UAT}}/GetOrderByOrderNumber?foretagkod={{foretagkod_value}}
ELSE:
	IF {{foretagkod}} == 0000:
		GET --> {{url_for_TEST}}/openapi.json
	ELSE
		POST --> {{url_for_TEST}}/GetOrderByOrderNumber?foretagkod={{foretagkod_value}}
```
# Structure
`main.py` --> Main file with API endpoints  
`gunicorn.py` --> File used for running FastAPI on prod using Gunicorn  
`config/` --> folder for configuration file  
`lib/` --> folder for classes used in API  
`models/` --> folder for pydantic models  
`cache/` --> folder for various temp files  
# Contributing
### Configure project
```bash
git clone git@gitlab.hl-display.com:root/wms2.0.git
python -m venv venv
source /venv/bin/activate
pip install -r requirements.txt
# Change login and pass in config.json
python main.py
```
### Debug
```python
logger.warning("Text for debug")
```
### Testing
All test should be created in `WMS2.0/test` folder.  
To run all test you need to activate virtual env and go to `WMS2.0` directory and run  
```python
coverage run --source=. -m pytest
coverage report -m
```
# Deployment
## Already configured machine
1. edit config file (if needed)
```bash
nano /home/ubuntu/.config/wms2.0/config_prod.json
```
2. Run Jenkins job `WMS2.0/Upgrade_prod_version`
## New machine
1. Add new service to systemd
```bash
sudo nano /etc/systemd/system/wms2.0.service
```
```bash
# wms2.0.service
# For running Gunicorn based application with a config file - TutLinks.com
#
# This file is referenced from official repo of TutLinks.com
# https://github.com/windson/fastapi/blob/fastapi-postgresql-caddy-ubuntu-deploy/gunicorn.service
#

[Unit]
Description=Gunicorn Web Server as Unit Service Systemd
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/opt/wms2.0
Environment="PATH=/home/ubuntu/virtual_environments/venv_wms2.0/bin"
ExecStart=/home/ubuntu/virtual_environments/venv_wms2.0/bin/gunicorn --config /opt/wms2.0/gunicorn.py main:app

[Install]
WantedBy=multi-user.target

```
```bash
sudo systemctl daemon-reload
```
2. edit config file
```bash
nano /home/ubuntu/.config/wms2.0/config_prod.json
```
3. Run Jenkins job `WMS2.0/Upgrade_prod_version`
4. Mount PDM shared drive in `/media` folder
   1. Create new folder `/media/pdm`
   2. Add new line in `/etc/fstab`
   ```
   //ew1-fil-101/OneJeeves/edm/erp /media/pdm  cifs  username=s-hlit,password=<PUT_PASSWORD_HERE>,uid=1001,iocharset=iso8859-1,vers=1.0  0  0
   ```
   3. Run below command to mount drives
   ```
   sudo mount /media/pdm/
   ```