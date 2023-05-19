import models
from tests import helpers


def test_WriteData_model():
    dict_item_out = helpers.OUT_WriteData_full
    model = models.WriteData()
    assert model.ProcesType is None
    assert model.foretagkod == '1210'
    assert model.Text6 == "XML OK"
    assert model.Text7 == ''
    assert model.ExecuteProcedure == 'Y'
    assert model.Message == ''
    assert model.EI is None
    assert len(model.dict()) == 7
    assert dict_item_out == model.dict()

def test_webhook_co_min():
    dict_item = helpers.IN_webhook_co_min
    dict_item_out = helpers.OUT_webhook_co_min
    model = models.webhook_co(**dict_item)
    assert len(model.dict()) == 10
    assert dict_item_out == model.dict()

def test_webhook_co_full():
    dict_item = helpers.IN_webhook_co_full
    dict_item_out = helpers.OUT_webhook_co_full
    model = models.webhook_co(**dict_item)
    assert len(model.dict()) == 10
    assert dict_item_out == model.dict()

def test_GetOrderByOrderNumberResponse_minimal():
    dict_item = helpers.IN_GetOrderByOrderNumberResponse_minimal
    dict_item_out = helpers.OUT_GetOrderByOrderNumberResponse_minimal
    model = models.GetOrderByOrderNumberResponse(**dict_item)
    assert len(model.dict()) == 9
    assert len(model.Consignee.dict()) == 6
    assert len(model.GoodsInfo.dict()) == 9
    assert len(model.OrderInfo.dict()) == 10
    assert model.WarehouseInfo is None
    assert model.OrderCurrentShipmentInfo is None
    assert model.GoodsItems is None
    assert model.PickedOrderLines is None
    assert model.Transporter.TransporterName is None
    assert model.OrderShipments is None
    assert dict_item_out == model.dict()

def test_GetOrderByOrderNumberResponse_full():
    dict_item = helpers.IN_GetOrderByOrderNumberResponse_full
    dict_item_out = helpers.OUT_GetOrderByOrderNumberResponse_full
    model = models.GetOrderByOrderNumberResponse(**dict_item)
    assert len(model.dict()) == 9
    assert dict_item_out == model.dict()

def test_ProcessProductionOrder():
    dict_item = helpers.IN_ProcessProductionOrder_full
    dict_item_out = helpers.OUT_ProcessProductionOrder_full
    model = models.ProcessProductionOrder(**dict_item)
    assert len(model.dict()) == 5
    assert dict_item_out == model.dict()

def test_ProcessInOrder_minimal():
    dict_item = helpers.IN_ProcessInOrder_minimal
    dict_item_out = helpers.OUT_ProcessInOrder_minimal
    model = models.ProcessInOrder(**dict_item)
    result_dict = model.dict()
    assert len(result_dict) == 3
    assert model.InOrderSupplier is None
    assert len(model.InOrderLines.InOrderLine[0].dict()) == 15
    assert dict_item_out == result_dict

def test_ProcessInOrder_full():
    dict_item = helpers.IN_ProcessInOrder_full
    dict_item_out = helpers.OUT_ProcessInOrder_full
    model = models.ProcessInOrder(**dict_item)
    assert len(model.dict()) == 3
    assert len(model.InOrderLines.InOrderLine[0].dict()) == 15
    assert dict_item_out == model.dict()

def test_ProcessOrder_minimal():
    dict_item = helpers.IN_ProcessOrder_minimal
    dict_item_out = helpers.OUT_ProcessOrder_minimal
    model = models.CustomerOrder(**dict_item)
    assert len(model.dict()) == 3
    assert len(model.CustomerOrderLines.CustomerOrderLine[0].dict()) == 17
    assert dict_item_out == model.dict()

def test_ProcessOrder_full():
    dict_item = helpers.IN_ProcessOrder_full
    dict_item_out = helpers.OUT_ProcessOrder_full
    model = models.CustomerOrder(**dict_item)
    assert len(model.dict()) == 3
    assert len(model.CustomerOrderLines.CustomerOrderLine[0].dict()) == 17
    assert dict_item_out == model.dict()

def test_GetProductionOrdersByQueryResponse_minimal():
    dict_item = helpers.IN_GetProductionOrdersByQueryResponse_minimal
    dict_item_out = helpers.OUT_GetProductionOrdersByQueryResponse_minimal
    model = models.GetProductionOrdersByQueryResponse(**dict_item)
    assert len(model.dict()) == 2
    assert dict_item_out == model.dict()

def test_GetProductionOrdersByQueryResponse_full():
    dict_item = helpers.IN_GetProductionOrdersByQueryResponse_full
    dict_item_out = helpers.OUT_GetProductionOrdersByQueryResponse_full
    model = models.GetProductionOrdersByQueryResponse(**dict_item)
    print(model.dict())
    assert len(model.dict()) == 2
    assert dict_item_out == model.dict()