from datetime import datetime

test_timestamp = datetime.strptime('2021-03-03T18:09:22.586Z', '%Y-%m-%dT%H:%M:%S.%f%z')

IN_webhook_co_min = {
        'webhookOrdersId': 1,
        'webhookEventId': 2,
        'system': 'sys1',
        'timestamp': test_timestamp,
        'orderId': 123,
        'orderNumber': '321',
        'goodsOwnerId': 74,
        'path': 'path/to/OnGoing'
    }

OUT_webhook_co_min = {
        'webhookOrdersId': 1,
        'webhookEventId': 2,
        'system': 'sys1',
        'timestamp': test_timestamp,
        'orderId': 123,
        'orderNumber': '321',
        'goodsOwnerId': 74,
        'path': 'path/to/OnGoing',
        'byUser': None,
        'byComputer': None
    }

IN_webhook_co_full = {
        'webhookOrdersId': 1,
        'webhookEventId': 2,
        'system': 'sys1',
        'timestamp': test_timestamp,
        'orderId': 123,
        'orderNumber': '321',
        'goodsOwnerId': 74,
        'path': 'path/to/OnGoing',
        'byUser': {
            'userId':162
        },
        'byComputer':{
            'computerId':1
            ,'computerName':'KTW-WKS-225'
        }
    }

OUT_webhook_co_full = {
        'webhookOrdersId': 1,
        'webhookEventId': 2,
        'system': 'sys1',
        'timestamp': test_timestamp,
        'orderId': 123,
        'orderNumber': '321',
        'goodsOwnerId': 74,
        'path': 'path/to/OnGoing',
        'byUser': {
            'userId':162
        },
        'byComputer':{
            'computerId':1
            ,'computerName':'KTW-WKS-225'
        }
    }

