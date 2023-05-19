from unittest.mock import patch
import pytest
from lib.on_going import OnGoing
from xml.etree import ElementTree
from pydantic import BaseModel


class ModelForTests(BaseModel):
    model_name: str
    foretagkod: str

def basic_data():
    root = ElementTree.Element("root")
    root.append( ElementTree.Element("test of return value") )

    return root

def test_ongoing_init2():
    res = OnGoing('model', 'service2', False, '1600')
    print(res.config)
    assert res.service_name == 'service2'

# TODO add test for init
# TODO add test of send_request()

# TEST NORMAL REQUEST

@pytest.fixture
def mocked_zeep_normal(mocker):
    # mock
    mock_zeep = mocker.patch('zeep.Client')
    
    return mock_zeep

def test_ongoing_ProcessProductionOrder(mocked_zeep_normal):
    # basic data
    model = ModelForTests(model_name='ProcessProductionOrder', foretagkod='1600')
    mocked_zeep_normal().service['ProcessProductionOrder'].return_value = 'Test return value'
    # test
    result = OnGoing(model, 'ProcessProductionOrder', False, '1600').normal_request()
    assert result['info'] == 'Test return value'
    assert mocked_zeep_normal().service.__getitem__.call_args_list[0][0][0] == 'ProcessProductionOrder'

def test_ongoing_ProcessInOrder(mocked_zeep_normal):
    # It is this same for ProcessInOrder and ProcessOrder
    # basic data
    model = ModelForTests(model_name='ProcessInOrder', foretagkod='1600')
    mocked_zeep_normal().service['ProcessInOrder'].return_value = 'Test return value'
    # test
    result = OnGoing(model, 'ProcessInOrder', False, '1600').normal_request()
    assert result['info'] == 'Test return value'
    assert mocked_zeep_normal().service.__getitem__.call_args_list[0][0][0] == 'ProcessInOrder'

def test_ongoing_GetInOrdersByQuery(mocked_zeep_normal):
    # basic data
    model = 'GetInOrdersByQuery'
    mocked_zeep_normal().service[model].return_value = 'Test return value'
    # test
    result = OnGoing(model, 'GetInOrdersByQuery', False, '1600').normal_request()
    assert result['info'] == 'Test return value'
    assert mocked_zeep_normal().service.__getitem__.call_args_list[0][0][0] == 'GetInOrdersByQuery'

# TODO add rest of tests

# TEST DEBUG REQUEST

@pytest.fixture
def mocked_zeep(mocker):
    # basic data
    root = ElementTree.Element("root")
    root.append( ElementTree.Element("test of return value") )
    # mock
    mock_zeep = mocker.patch('zeep.Client')
    mock_zeep().create_message.return_value = root
    return mock_zeep

def test_ongoing_ProcessArticle_debug(mocked_zeep):
    # basic data
    model = ModelForTests(model_name = 'ProcessArticle', foretagkod = '1210')
    # test
    result = OnGoing(model, 'ProcessArticle', False, '1600').debug_request()
    assert 'art' in mocked_zeep().create_message.call_args[1]
    assert result['model'] == model
    assert result['info'] == b'<root><test of return value /></root>'

def test_ongoing_ProcessProductionOrder_debug(mocked_zeep):
    # basic data
    model = ModelForTests(model_name = 'ProcessProductionOrder', foretagkod = '1210')
    # test
    result = OnGoing(model, 'ProcessProductionOrder', False, '1600').debug_request()
    assert 'ProductionOrder' in mocked_zeep().create_message.call_args[1]
    assert result['model'] == model
    assert result['info'] == b'<root><test of return value /></root>'

def test_ongoing_GetInOrdersByQuery_debug(mocked_zeep):
    # basic data
    model = 'GetInOrdersByQuery'
    # test
    result = OnGoing(model, 'GetInOrdersByQuery', False, '1600').debug_request()
    assert 'query' in mocked_zeep().create_message.call_args[1]
    assert result['model'] == model
    assert result['info'] == b'<root><test of return value /></root>'
    
def test_ongoing_GetInventoryChanges_debug(mocked_zeep):
    # basic data
    model = 'GetInventoryChanges'
    # test
    result = OnGoing(model, 'GetInventoryChanges', False, '1600').debug_request()
    assert 'query' in mocked_zeep().create_message.call_args[1]
    assert result['model'] == model
    assert result['info'] == b'<root><test of return value /></root>'

def test_ongoing_GetOrderByOrderNumber_debug(mocked_zeep):
    # basic data
    model = 'GetOrderByOrderNumber'
    # test
    result = OnGoing(model, 'GetOrderByOrderNumber', False, '1600').debug_request()
    assert 'OrderNumber' in mocked_zeep().create_message.call_args[1]
    assert result['model'] == model
    assert result['info'] == b'<root><test of return value /></root>'

def test_ongoing_ProcessReturnOrder_debug(mocked_zeep):
    # basic data
    model = ModelForTests(model_name = 'ProcessReturnOrder', foretagkod = '1210')
    # test
    result = OnGoing(model, 'ProcessReturnOrder', False, '1600').debug_request()
    assert 'ReturnOrder' in mocked_zeep().create_message.call_args[1]
    assert result['model'] == model
    assert result['info'] == b'<root><test of return value /></root>'

def test_ongoing_GetInventoryByQuery_debug(mocked_zeep):
    # basic data
    model = 'GetInventoryByQuery'
    # test
    result = OnGoing(model, 'GetInventoryByQuery', False, '1600').debug_request()
    assert 'GetInventoryQuery' in mocked_zeep().create_message.call_args[1]
    assert result['model'] == model
    assert result['info'] == b'<root><test of return value /></root>'

def test_ongoing_SalesOrder_debug(mocked_zeep):
    # basic data
    model = ModelForTests(model_name = 'SalesOrder', foretagkod = '1210')
    # test
    result = OnGoing(model, 'SalesOrder', False, '1600').debug_request()
    assert 'co' in mocked_zeep().create_message.call_args[1]
    assert result['model'] == model
    assert result['info'] == b'<root><test of return value /></root>'