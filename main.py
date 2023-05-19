from fastapi import FastAPI, Request, Response, status, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
from fastapi.logger import logger
from lib.converters import XMLConverter, InventoryListConverter, date2string_converter, decimal2float_converter
from lib.on_going import OnGoing
from lib.jeeves import Jeeves
from lib.mails import Mail
import models
import os
from datetime import date, datetime, timedelta
import pytz
from sentry_asgi import SentryMiddleware
import sentry_sdk
from sentry_sdk import capture_exception
import socket
import json


# Main config
if socket.gethostname() == 'bma-wms-101':
    environment = 'Prod'
else:
    environment = 'Test'
sentry_sdk.init(dsn="https://6f691d51dc4f449dbc9ee4b4c90822ad@o229295.ingest.sentry.io/5715694", environment=environment)
app = FastAPI()
security = HTTPBasic()

# Endpoints

@app.get("/config", status_code=200)
def get_config(credentials: HTTPBasicCredentials = Depends(security)):
    """Get all config in list form."""
    correct_username = secrets.compare_digest(credentials.username, "admin")
    correct_password = secrets.compare_digest(credentials.password, "gb5pHwPBuV4zPUJs")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    with open('config/config.json') as data_file:
        config = json.load(data_file)
        return config

@app.post("/addArticle", status_code=200)
def addArticle(model: models.Article, response: Response, foretagkod: str = '1210', debug: bool = False):
    # Send data to wms2.0
    try:
        result = OnGoing(model, 'ProcessArticle', debug, foretagkod).send_request()
        return result
    except Exception as e:
        response.status_code = status.HTTP_409_CONFLICT
        capture_exception(e)
        return {'info': str(e)}


@app.post("/addArticle_xml", status_code=200)
async def addArticle_xml(request: Request, response: Response, foretagkod: str = '1210', debug: bool = False):
    res = XMLConverter(await request.body())  # read body with XML
    try:
        force_list_tag = ('StructureArticleDefinition')
        model = models.Article(**res.convert(force_list_tag))  # initialize model with converted xml to dict
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        capture_exception(e)
        return {'info': str(e)}
    # Send data to wms2.0
    try:
        result = OnGoing(model, 'ProcessArticle', debug, foretagkod).send_request()
        return result
    except Exception as e:
        response.status_code = status.HTTP_409_CONFLICT
        capture_exception(e)
        return {'info': str(e)}


@app.post("/addSalesOrder")
def addSalesOrder(model: models.CustomerOrder, response: Response, foretagkod: str = '1210', debug: bool = False):
    # Send data to wms2.0
    try:
        result = OnGoing(model, 'ProcessOrder', debug, foretagkod).send_request()
        return result
    except Exception as e:
        response.status_code = status.HTTP_409_CONFLICT
        capture_exception(e)
        return {'info': str(e)}

@app.post("/addSalesOrder_xml", status_code=200)
async def addSalesOrder_xml(request: Request, response: Response, foretagkod: str = '1210', debug: bool = False):
    res = XMLConverter(await request.body())  # read body with XML
    try:
        force_list_tag = ('SubOrderLine', 'Class')

        result = res.convert(force_list_tag)
        for item in result['CustomerOrderLines']['CustomerOrderLine']:
            if item is None:
                result['CustomerOrderLines']['CustomerOrderLine'].remove(None)
        
        model = models.CustomerOrder(**result)  # initialize model with converted xml to dict
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        capture_exception(e)
        return {'info': str(e)}
    # Send data to wms2.0
    try:
        result = OnGoing(model, 'ProcessOrder', debug, foretagkod).send_request()
        return result
    except Exception as e:
        response.status_code = status.HTTP_409_CONFLICT
        capture_exception(e)
        return {'info': str(e)}

@app.post("/UploadOrderFile")
def UploadOrderFile(model: models.UploadOrderFile, response: Response, foretagkod: str = '1210', debug: bool = False):
    try:
        with open(model.file_path, 'rb') as file:
            file_content = file.read()
    except FileNotFoundError as e:
        response.status_code = status.HTTP_404_NOT_FOUND
        capture_exception(e)
        return {'info': f"No such file or directory: {model.file_path}"}
    try:
        filename = model.file_path.rsplit("/", 1)[1]
        model_for_ongoing = {
            "File": {
                "FileName": filename,
                "FileBytes": file_content,
                "MimeType": "application/pdf",
                "FileId": -1,
            },
            "GoodsOwnerId": 72,
            "OrderFileIdentificationType": "GoodsOwnerOrderNumber",
            "GoodsOwnerOrderNumber": model.order_number
        }
        result = OnGoing(model_for_ongoing, 'UploadOrderFile', debug, foretagkod).send_request()
        if debug is True:
            model_for_debug = model_for_ongoing
            model_for_debug['File']['FileBytes'] = "file in byte format"
            return {"model": model_for_ongoing, "info": result['info']}
        else:
            return result
    except Exception as e:
        response.status_code = status.HTTP_409_CONFLICT
        capture_exception(e)
        return {'info': str(e)}

@app.post("/addInOrder")
def addInOrder(model: models.ProcessInOrder, response: Response, foretagkod: str = '1210', debug: bool = False):
    # Send data to wms2.0
    try:
        result = OnGoing(model, 'ProcessInOrder', debug, foretagkod).send_request()
        return result
    except Exception as e:
        response.status_code = status.HTTP_409_CONFLICT
        capture_exception(e)
        return {'info': str(e)}

@app.post("/addInOrder_xml", status_code=200)
async def addInOrder_xml(request: Request, response: Response, foretagkod: str = '1210', debug: bool = False):
    res = XMLConverter(await request.body())  # read body with XML
    try:
        force_list_tag = ('InOrderLine', 'InOrderLineArticleItem')
        model = models.ProcessInOrder(**res.convert(force_list_tag))  # initialize model with converted xml to dict
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        capture_exception(e)
        return {'info': str(e)}
    # Send data to wms2.0
    try:
        result = OnGoing(model, 'ProcessInOrder', debug, foretagkod).send_request()
        return result
    except Exception as e:
        response.status_code = status.HTTP_409_CONFLICT
        capture_exception(e)
        return {'info': str(e)}

@app.post("/addProductionOrder")
def addProductionOrder(model: models.ProcessProductionOrder, response: Response, foretagkod: str = '1210', debug: bool = False):
    # Send data to wms2.0
    try:
        result = OnGoing(model, 'ProcessProductionOrder', debug, foretagkod).send_request()
        return result
    except Exception as e:
        response.status_code = status.HTTP_409_CONFLICT
        capture_exception(e)
        return {'info': str(e)}

@app.post("/addProductionOrder_xml", status_code=200)
async def addProductionOrder_xml(request: Request, response: Response, foretagkod: str = '1210', debug: bool = False):
    res = XMLConverter(await request.body())  # read body with XML
    try:
        force_list_tag = ('ProductionOrderLine')
        model = models.ProcessProductionOrder(**res.convert(force_list_tag))  # initialize model with converted xml to dict
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        capture_exception(e)
        return {'info': str(e)}
    # Send data to wms2.0
    try:
        result = OnGoing(model, 'ProcessProductionOrder', debug, foretagkod).send_request()
        return result
    except Exception as e:
        response.status_code = status.HTTP_409_CONFLICT
        capture_exception(e)
        return {'info': str(e)}

@app.post("/addReturnOrder", status_code=200)
def addReturnOrder(model: models.ReturnOrder, response: Response, foretagkod: str = '1210', debug: bool = False):
    # Send data to wms2.0
    try:
        result = OnGoing(model, 'ProcessReturnOrder', debug, foretagkod).send_request()
        return result
    except Exception as e:
        response.status_code = status.HTTP_409_CONFLICT
        capture_exception(e)
        return {'info': str(e)}


@app.post("/addReturnOrder_xml", status_code=200)
async def addReturnOrder_xml(request: Request, response: Response, foretagkod: str = '1210', debug: bool = False):
    res = XMLConverter(await request.body())  # read body with XML
    try:
        force_list_tag = ('ReturnOrderLine')
        model = models.ReturnOrder(**res.convert(force_list_tag))  # initialize model with converted xml to dict
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        capture_exception(e)
        return {'info': str(e)}
    # Send data to wms2.0
    try:
        result = OnGoing(model, 'ProcessReturnOrder', debug, foretagkod).send_request()
        return result
    except Exception as e:
        response.status_code = status.HTTP_409_CONFLICT
        capture_exception(e)
        return {'info': str(e)}

@app.post("/addCustomerOwnStockOrder", status_code=200)
def addCustomerOwnStockOrder(model: models.CustomerOwnStockOrder, response: Response, foretagkod: str = '1210', debug: bool = False):
    # Send data to wms2.0
    try:
        result = OnGoing(model, 'ProcessGoodsOperationOrder', debug, foretagkod).send_request()
        return result
    except Exception as e:
        response.status_code = status.HTTP_409_CONFLICT
        capture_exception(e)
        return {'info': str(e)}

@app.post("/GetOrderByOrderNumber")
def GetOrderByOrderNumber(webhook_model: models.webhook_co, response: Response, foretagkod: str = '1210', debug: bool = False):
    # TBD what to do when model fails?
    # Send data to wms2.0 
    try:
        result = OnGoing(webhook_model.orderNumber, 'GetOrderByOrderNumber', False, foretagkod).send_request()['info']
    except Exception as e:
        response.status_code = status.HTTP_409_CONFLICT
        capture_exception(e)
        return {'info': str(e)}
    if result != None :
        jeeves_data = models.WriteData()
        jeeves_data.ProcesType = 'GetOrderByOrderNumber'
        jeeves_data.foretagkod = foretagkod
        jeeves_data.ExecuteProcedure = 'N'
        jeeves_object = Jeeves()
        try:
            is_manafacturing_order = False
            classes_list = result['OrderInfo']['OrderClasses']['OrderClassInfo']
            for order_class in classes_list:
                if order_class['Name'] == "Manufacturing order":
                    is_manafacturing_order = True
        except TypeError:
            pass
        if is_manafacturing_order is True:
            jeeves_data.ProcesType = 'GetOrderByOrderNumber_manufacturing'
            jeeves_data.ExecuteProcedure = 'N'
        try:
            model = models.GetOrderByOrderNumberResponse.parse_obj(result)  # Check data from ongoing
            model_dict = model.dict()
            # check if webhook model variables are present
            if webhook_model.byComputer is None:
                computerName = 'NULL'
            else:
                computerName = webhook_model.byComputer.computerName
            if webhook_model.byUser is None:
                userId = 0
            else:
                userId = webhook_model.byUser.userId
            # add aditional info to data saved in jeeves
            model_dict['misc'] = {'computerName': computerName, "userId": userId}
            model_xml = XMLConverter(model_dict).convert_to_xml()  # parse JSON to XML    
            jeeves_data.Text7 = model_xml.replace('\'', '"')
            jeeves_object.insert2dp_data(jeeves_data)  # write xml to dp_data
        except Exception as e:
            response.status_code = status.HTTP_400_BAD_REQUEST
            jeeves_data.Text7 = str(result).replace('\'', '"')
            jeeves_data.ExecuteProcedure = 'N'
            jeeves_data.Text6 = "XML ERROR"
            jeeves_data.Message = e
            jeeves_object.insert2dp_data(jeeves_data)  # write xml to dp_data
            capture_exception(e)
            return {'info': str(e)}
        if debug is True:
            return {'info': result }
        return {'model': model, 'info': result}
    return {'model': webhook_model, 'info': result}

@app.get("/GetInOrdersByQuery", status_code=200)
async def GetInOrdersByQuery(response: Response, 
    foretagkod: str = '1210', 
    debug: bool = False,
    date_from: datetime = None, 
    date_to: datetime = None):
    if date_from is None or date_to is None:
        # create data model PROD
        server_now = datetime.now()  # server is in UTC timezone
        timezone = pytz.timezone("Europe/Warsaw")  # Ongoing have this same timezone
        time_now = server_now.astimezone(timezone) 
        if time_now.minute < 15:
            new_minutes = 45
            time_now -= timedelta(hours=1)
        elif time_now.minute < 30:
            new_minutes = 0
        elif time_now.minute < 45:
            new_minutes = 15
        else:
            new_minutes = 30
        date_from = time_now.replace(minute=new_minutes, second=0, microsecond=1)  # Change to full hours + 1 microsecond
        date_to = date_from.replace(microsecond=0) + timedelta(minutes = 15)
    model = {"LastReceiveTimeFrom": date_from, "LastReceiveTimeTo": date_to}
    # Send data to wms2.0
    try:
        result = OnGoing(model, 'GetInOrdersByQuery', False, foretagkod).send_request()['info']
    except Exception as e:
        response.status_code = status.HTTP_409_CONFLICT
        capture_exception(e)
        return {'info': str(e)}
    purchase_order_list = []
    if result != None :
        error = False
        for item in result['ReceivedInOrder']:
            is_manafacturing_order = False
            jeeves_data = models.WriteData()
            jeeves_data.ProcesType = 'GetInOrdersByQuery'
            jeeves_data.foretagkod = foretagkod
            jeeves_data.ExecuteProcedure = 'N'
            try:
                model = models.GetInOrdersByQueryResponse.parse_obj(item)  # Check data from ongoing
                if model.InOrderInfo.InOrderTypeName in ["Manufacturing order", "Forecast incl material", "Forecast excl material", "Subcontracting order"]:
                    is_manafacturing_order = True
                if model.InOrderInfo.InOrderIsReturnType is True:
                    jeeves_data.ProcesType = 'GetCreditInOrdersByQuery'
                model_xml = XMLConverter(model.dict()).convert_to_xml()  # parse JSON to XML 
                jeeves_data.Text7 = model_xml
                if is_manafacturing_order is False:
                    Jeeves().insert2dp_data(jeeves_data, endline=True)  # write xml to dp_data
            except Exception as e:
                capture_exception(e)
                jeeves_data.Text7 = str(item).replace('\'', '"')
                jeeves_data.ExecuteProcedure = 'N'
                jeeves_data.Text6 = "XML ERROR"
                jeeves_data.Message = e
                jeeves_data.EI = 'E'
                error = True
                if is_manafacturing_order is False:
                    Jeeves().insert2dp_data(jeeves_data)  # write xml to dp_data
            purchase_order_list.append(model.InOrderInfo.GoodsOwnerOrderNumber)
        if error is True:
            response.status_code = status.HTTP_400_BAD_REQUEST
        if debug is True:
            return {'purchase_order_list': purchase_order_list, 'info': result }
        result = 'All items saved in dp_data'  
    return {'purchase_order_list': purchase_order_list, 'info': result}

@app.get("/GetInventoryChanges", status_code=200)
async def GetInventoryChanges(response: Response, 
    foretagkod: str = '1210', 
    debug: bool = False,
    date_from: datetime = None, 
    date_to: datetime = None):
    if date_from is None or date_to is None:
        # create data model PROD
        server_now = datetime.now()  # server is in UTC timezone
        timezone = pytz.timezone("Europe/Warsaw")  # Ongoing have this same timezone
        time_now = server_now.astimezone(timezone) 
        if time_now.minute < 15:
            new_minutes = 45
            time_now -= timedelta(hours=1)
        elif time_now.minute < 30:
            new_minutes = 0
        elif time_now.minute < 45:
            new_minutes = 15
        else:
            new_minutes = 30
        date_from = time_now.replace(minute=new_minutes, second=0, microsecond=1)  # Change to full hours + 1 microsecond
        date_to = date_from.replace(microsecond=0) + timedelta(minutes = 15)
    model = {"FromDate": date_from, "ToTime": date_to}
    # Send data to wms2.0
    try:
        result = OnGoing(model, 'GetInventoryChanges', False, foretagkod).send_request()['info']
    except Exception as e:
        response.status_code = status.HTTP_409_CONFLICT
        capture_exception(e)
        return {'info': str(e), 'model': model}
    if result['InventoryChangeLines'] != None :
        changes_list = dict()
        errors = []
        # retrive inventory id from every transaction and group them in changes_list dict
        for item in result['InventoryChangeLines']['InventoryChangeLine']:
            transaction_id = item['InventoryTransactions']['InventoryTransaction'][0]['InventoryId']
            changes_list.setdefault(transaction_id, [])
            changes_list[transaction_id].append(item)
        # convert JSON to xml for every group and save it in Jeeves
        for key, value in changes_list.items():
            jeeves_data = models.WriteData()
            jeeves_data.ProcesType = 'GetInventoryChanges'
            jeeves_data.foretagkod = foretagkod
            error_handler = models.WriteData()
            error_handler.ProcesType = 'GetInventoryChanges'
            error_handler.foretagkod = foretagkod
            for item in value:    
                try:
                    model = models.InventoryChangeLine.parse_obj(item)
                    model_xml = XMLConverter(model.dict()).convert_to_xml()  # parse JSON to XML 
                    jeeves_data.Text7 += model_xml
                except Exception as e:
                    capture_exception(e)
                    error_handler.Text7 = str(item).replace('\'', '"')
                    error_handler.ExecuteProcedure = 'N'
                    error_handler.Text6 = "XML ERROR"
                    error_handler.Message = e
                    errors.append(error_handler)  # Store errors in separete list
            if jeeves_data.Text7 != '':
                Jeeves().insert2dp_data(jeeves_data)  # write xml to dp_data
        # If there are some errors change HTTP response and save all errors in Jeeves
        if len(errors) != 0:
            response.status_code = status.HTTP_400_BAD_REQUEST
            for item in errors:
                Jeeves().insert2dp_data(item)  # write xml to dp_data
        if debug is True:
            return {'info': result }
        result = 'All items saved in dp_data'
        
    return result

@app.get("/GetInventoryItems", status_code=200)
async def GetInventoryItems(response: Response, email: str = "ithelpdesk@hl-display.com", foretagkod: str = '1210', debug: bool = False):
    # Send data to wms2.0
    model = {'GetZeroStockArticles': False}
    try:
        raw_data = OnGoing(model, 'GetInventoryItems', False, foretagkod).send_request()['info']
    except Exception as e:
        response.status_code = status.HTTP_409_CONFLICT
        capture_exception(e)
        return {'info': str(e)}
    if debug is True:
        debug_data = []
        for row in raw_data['InventoryItemLines']['InventoryItemLine']:
            debug_data.append(row['Article']['ArticleNumber'])
        return {'data': debug_data}
    # convert data from ongoing to list of dicts
    parsed_data = InventoryListConverter(raw_data).convert(foretagkod)
    result = Jeeves().check_stock_balance(parsed_data)
    email_object = Mail(email).stock_balance(result)  # send email
    # save log to dp_data
    jeeves_data = models.WriteData()
    jeeves_data.ProcesType = 'GetInventoryItems'
    jeeves_data.foretagkod = foretagkod
    jeeves_data.ExecuteProcedure = 'N'
    jeeves_data.EI = 'I' 
    jeeves_data.Message = email_object.replace('\'', '"')  # need to change all ' to " to mitigate problems with running procedure on db
    Jeeves().insert2dp_data(jeeves_data)
    
    return {'data': email_object}

@app.get("/GetProductionOrdersByQuery", status_code=200)
async def GetProductionOrdersByQuery(
    response: Response, 
    foretagkod: str = '1210', 
    debug: bool = False, 
    date_from: datetime = None, 
    date_to: datetime = None,
    output: models.Output = 'json'):
    if date_from is None and date_to is None:
        # create data model PROD
        server_now = datetime.now()  # server is in UTC timezone
        timezone = pytz.timezone("Europe/Warsaw")  # Ongoing have this same timezone
        time_now = server_now.astimezone(timezone) 
        if time_now.minute < 15:
            new_minutes = 45
            time_now -= timedelta(hours=1)
        elif time_now.minute < 30:
            new_minutes = 0
        elif time_now.minute < 45:
            new_minutes = 15
        else:
            new_minutes = 30
        date_from = time_now.replace(minute=new_minutes, second=0, microsecond=1)  # Change to full hours + 1 microsecond
        date_to = date_from.replace(microsecond=0) + timedelta(minutes = 15)
    query_model = {
        "LastProductionTimeFrom": date_from, 
        "LastProductionTimeTo": date_to, 
        "ProductionOrderSpecialFilters": {
            "OnlyProductionOrdersWithLinesToReport": True
        }
    }
     # Send data to wms2.0
    try:
        result = OnGoing(query_model, 'GetProductionOrdersByQuery', False, foretagkod).send_request()['info']
    except Exception as e:
        response.status_code = status.HTTP_409_CONFLICT
        capture_exception(e)
        return {'info': str(e)}
    if result != None :
        error = False
        for production_order in result['ProductionOrderInfo']:
            jeeves_data = models.WriteData()
            jeeves_data.ProcesType = 'GetProductionOrdersByQuery'
            jeeves_data.foretagkod = foretagkod
            try:
                model = models.GetProductionOrdersByQueryResponse.parse_obj(production_order)  # Check data from ongoing
                if output == 'xml':
                    model_xml = XMLConverter(model.dict()).convert_to_xml()  # parse JSON to XML 
                    jeeves_data.Text7 = model_xml
                else:
                    json_str = json.dumps(model.dict(), default=date2string_converter)
                    jeeves_data.Text7 = json_str
            except Exception as e:
                capture_exception(e)
                jeeves_data.Text7 = str(production_order).replace('\'', '"')
                jeeves_data.ExecuteProcedure = 'N'
                jeeves_data.Text6 = "XML ERROR"
                jeeves_data.Message = e
                jeeves_data.EI = 'E'
                error = True
            Jeeves().insert2dp_data(jeeves_data)  # write xml to dp_data
        if error is True:
            response.status_code = status.HTTP_400_BAD_REQUEST
        if debug is True:
            return {'query_model': query_model, 'model': model, 'results': result}
        result = 'All items saved in dp_data'

    return {'info': query_model, 'results': result}

@app.get("/GetGoodsOperationOrdersByQuery", status_code=200)
async def GetGoodsOperationOrdersByQuery(
    response: Response, 
    foretagkod: str = '1210', 
    debug: bool = False):
    jeeves_object = Jeeves()
    orders_from_jeeves = jeeves_object.fetch_data_about_COG_orders(foretagkod)
    orders_list = []
    error = False
    for order in orders_from_jeeves:
        # Send data to wms2.0
        orders_list.append(order[0])
        model = {'GoodsOperationOrderNumbersToGet': {"string": order[0]}}
        try:
            result = OnGoing(model, 'GetGoodsOperationOrdersByQuery', debug, foretagkod).send_request()['info']
        except Exception as e:
            response.status_code = status.HTTP_409_CONFLICT
            capture_exception(e)
            return {'error info': str(e)}
        if result is not None:
            try:
                jeeves_data = models.WriteData()
                jeeves_data.ProcesType = 'GetGoodsOperationOrdersByQuery'
                jeeves_data.foretagkod = foretagkod
                one_result = result['GoodsOperationOrderInfo'][0]
                result_model = models.GetGoodsOperationOrdersByQueryResponse.parse_obj(one_result)
                if result_model.GoodsOperationOrderHeader.GoodsOperationOrderStatusId == 500:
                    json_str = json.dumps(result_model.dict(), default=decimal2float_converter)
                    jeeves_data.Text7 = json_str
                    jeeves_object.insert2dp_data(jeeves_data)
            except Exception as e:
                capture_exception(e)
                jeeves_data.Text7 = "error parsing data for order {}".format(order[0])
                jeeves_data.ExecuteProcedure = 'N'
                jeeves_data.Text6 = "JSON ERROR"
                jeeves_data.Message = e
                jeeves_data.EI = 'E'
                error = True
                jeeves_object.insert2dp_data(jeeves_data)
    if error is True:
        response.status_code = status.HTTP_400_BAD_REQUEST
        
    return {'info': orders_list}


# Sentry config
app = SentryMiddleware(app)
# Uvicorn config
if __name__ == "__main__":
    import uvicorn
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if dir_path == "/home/ubuntu/dev/wms2.0":
        port = 8001
    else:
        port = 8000
    log_config = uvicorn.config.LOGGING_CONFIG
    log_config["formatters"]["default"]["fmt"] = "%(asctime)s [%(name)s] %(levelprefix)s %(message)s"
    log_config["formatters"]["access"]["fmt"] = '%(asctime)s [%(name)s] %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s'
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True, debug=True, log_config=log_config)
