from datetime import datetime

IN_GetOrderByOrderNumberResponse_minimal = {
        "Consignee": {
            "Id": 0,
            "NotifyByEmail": True,
            "NotifyBySms": True,
            "NotifyByTelephone": True,
            "CustomerNumber": "string"
        },
        "GoodsInfo": {
            "NumberOfGoodsItems": 0,
            "NumberOfPackages": 0,
            "SummedGoodsItemParcels": 0,
            "SummedGoodsItemWeight": 0,
            "SummedGoodsItemVolume": 0,
            "SummedGoodsItemLoadMeters": 0,
            "SummedGoodsItemArea": 0,
            "SummedArticleItemWeight": 0,
            "SummedArticleItemVolume": 0
        },
        "OrderInfo": {
            "OrderId": 0,
            "PickedNumberOfItems": 1.1,
            "OrderedNumberOfItems": 1.2            
        },
        "Transporter": {
            "TransporterName": None
        }
    }
    
OUT_GetOrderByOrderNumberResponse_minimal = {
    'Consignee': {
        'Id': 0, 
        'NotifyByEmail': True, 
        'NotifyBySms': True, 
        'NotifyByTelephone': True, 
        'CustomerNumber': 'string', 
        'CustomerNumberPallets': None
    }, 
    'GoodsInfo': {
        'NumberOfGoodsItems': 0, 
        'NumberOfPackages': 0, 
        'SummedGoodsItemParcels': 0, 
        'SummedGoodsItemWeight': 0.0, 
        'SummedGoodsItemVolume': 0.0, 
        'SummedGoodsItemLoadMeters': 0.0, 
        'SummedGoodsItemArea': 0.0, 
        'SummedArticleItemWeight': 0.0, 
        'SummedArticleItemVolume': 0.0
    }, 
    'OrderInfo': {
        'OrderId': 0, 
        'ReferenceNumber': None, 
        'GoodsOwnerOrderNumber': None, 
        'GoodsOwnerOrderId': None, 
        'WayOfDeliveryTypeName': None,
        'PickedNumberOfItems': 1.1, 
        'OrderedNumberOfItems': 1.2, 
        'BackOrderForOrderId': None, 
        'CurrentShipmentId': None,
        'OrderClasses': None
    }, 
    'WarehouseInfo': None, 
    'OrderCurrentShipmentInfo': None, 
    'GoodsItems': None, 
    'PickedOrderLines': None, 
    'Transporter': {
        'TransporterName': None
    }, 
    'OrderShipments': None
}

IN_GetOrderByOrderNumberResponse_full = {
        "Consignee": {
            "Id": 0,
            "NotifyByEmail": True,
            "NotifyBySms": True,
            "NotifyByTelephone": True,
            "CustomerNumber": "string"
        },
        "GoodsInfo": {
            "NumberOfGoodsItems": 1,
            "NumberOfPackages": 2,
            "SummedGoodsItemParcels": 3,
            "SummedGoodsItemWeight": 4.1,
            "SummedGoodsItemVolume": 5.1,
            "SummedGoodsItemLoadMeters": 6.1,
            "SummedGoodsItemArea": 7.1,
            "SummedArticleItemWeight": 8.1,
            "SummedArticleItemVolume": 9.1
        },
        "OrderInfo": {
            "OrderId": 0,
            "PickedNumberOfItems": 1.1,
            "OrderedNumberOfItems": 2.1,
        },
        "WarehouseInfo": {
            "Id": 0
        },
        "OrderCurrentShipmentInfo": {
            "StatusId": 0,
            "ShipmentPalletItems": [
                {
                    "Id": 0,
                    "IsTaPalletItem": True,
                    "IsReturnTaPalletItem": True,
                    "ParentPalletItemId": 0,
                    "PalletTypeCode": "string",
                }
            ]
        },
        "GoodsItems": {
            "GoodsItem": [
                {
                    "Id": 0
                }
            ]
        },
        "PickedOrderLines": {
            "PickedOrderLine": [
                {
                    "Article": {
                        "ArticleNumber": "string"
                    },
                    "OrderLineSystemId": 0,
                    "DeliveryDate": "2021-03-03T18:09:22.586Z",
                    "OrderedNumberOfItems": 1.1,
                    "PickedNumberOfItems": 2.1,
                    "IsParentLine": True,
                    "DoPick": True,
                    "IsPickedWithErrors": True
                }
            ]
        },
        "Transporter": {
            "TransporterName": None
        },
        "OrderShipments": {
            "OrderShipmentInfo": [
                {
                    "ShipmentId": 0,
                    "StatusId": 0
                }
            ]
        }
    }

OUT_GetOrderByOrderNumberResponse_full = {
    "Consignee": {
        "Id": 0,
        "NotifyByEmail": True,
        "NotifyBySms": True,
        "NotifyByTelephone": True,
        "CustomerNumber": "string",
        "CustomerNumberPallets": None
    },
    "GoodsInfo": {
        "NumberOfGoodsItems": 1,
        "NumberOfPackages": 2,
        "SummedGoodsItemParcels": 3,
        "SummedGoodsItemWeight": 4.1,
        "SummedGoodsItemVolume": 5.1,
        "SummedGoodsItemLoadMeters": 6.1,
        "SummedGoodsItemArea": 7.1,
        "SummedArticleItemWeight": 8.1,
        "SummedArticleItemVolume": 9.1
    },
    "OrderInfo": {
        "OrderId": 0,
        "ReferenceNumber": None,
        "GoodsOwnerOrderNumber": None,
        "GoodsOwnerOrderId": None,
        'WayOfDeliveryTypeName': None,
        "PickedNumberOfItems": 1.1,
        "OrderedNumberOfItems": 2.1,
        "BackOrderForOrderId": None,
        "CurrentShipmentId": None,
        'OrderClasses': None
    },
    "WarehouseInfo": {
        "Name": None,
        "Code": None,
        "Id": 0
    },
    "OrderCurrentShipmentInfo": {
        "Waybill": None,
        "StatusId": 0,
        "ShipmentPalletItems": [
            {
                "Id": 0,
                "LabelId": None,
                "IsTaPalletItem": True,
                "IsReturnTaPalletItem": True,
                "Comment": None,
                "ParentPalletItemId": 0,
                "PalletTypeCode": "string",
                "TrackingUrl": None
            }
        ]
    },
    "GoodsItems": {
        "GoodsItem": [
            {
                "Id": 0,
                "GoodsItemLabelId": None,
                "PackageTypeName": None,
                "PackageTypeCode": None,
                "Area": None,
                "Weight": None,
                "Volume": None,
                "Height": None,
                "Length": None,
                "Width": None,
                "LoadMeters": None,
                "NumberOfItems": None,
                "NumberOfPackages": None,
                "ApprovedNumberOfPackages": None
            }
        ]
    },
    "PickedOrderLines": {
        "PickedOrderLine": [
            {
                "Article": {
                    "ArticleNumber": "string"
                },
                "OrderLineSystemId": 0,
                "DeliveryDate": datetime.strptime("2021-03-03T18:09:22.586Z", "%Y-%m-%dT%H:%M:%S.%f%z"),
                "LastPickingTime": None,
                "StartPickingTime": None,
                "OrderedNumberOfItems": 1.1,
                "PickedNumberOfItems": 2.1,
                "ExternalOrderLineCode": None,
                "ParentExternalOrderLineCode": None,
                "ParentOrderLineId": None,
                "IsParentLine": True,
                "DoPick": True,
                "RowPrice": None,
                "ReportedNumberOfItems": None,
                "AllocatedNumberOfItems": None,
                "AcknowledgedNumberOfItems": None,
                "OrderLineCaseNo": None,
                "CustomerArticleNumber": None,
                "PickOrderInfo": None,
                "ReportedReturnedNumberOfItems": None,
                "IsPickedWithErrors": True
            }
        ]
    },
    "Transporter": {
        "TransporterName": None
    },
    "OrderShipments": {
        "OrderShipmentInfo": [
            {
                "ShipmentId": 0,
                "WayBill": None,
                "StatusId": 0
            }
        ]
    }
}
