from datetime import datetime

IN_ProcessOrder_minimal = {
        "OrderInfo": {
            "OrderIdentification": "GoodsOwnerOrderNumber",
            "OrderOperation": "CreateOrUpdate",
            "GoodsOwnerOrderNumber": "000001",
            "DeliveryDate": "2021-04-19",
        },
        "Customer": {
            "CustomerOperation": "CreateOrUpdate",
            "CustomerIdentification": "CustomerNumber",
            "CustomerNumber": "185432",
            "Name": "Stark Johansson AB",
            "IsVisible": False,
            "NotifyBySMS": False,
            "NotifyByEmail": False,
            "NotifyByTelephone": False
        },
        "CustomerOrderLines": {
            "CustomerOrderLine": [
                {
                    "OrderLineIdentification": "ExternalOrderLineCode",
                    "ArticleIdentification": "ArticleNumber",
                    "SubOrderLineSpecification": "ArticleRegisterSpecification",
                    "DeliveryDate": "2021-04-19",
                    "ExternalOrderLineCode": "10",
                    "ArticleNumber": "200088",
                    "LinePrice": 1.1,
                    "NumberOfItems": 1.2,
                    "CurrencyCode": "SEK",
                    "DoPick": True,
                    "ForcePickFullItems": False,
                    "OrderLineArticleItemStatus": {
                        "Identification": "ArticleItemStatusCode",
                        "Operation": "Find",
                        "ArticleItemStatusCode": "string"
                    }
                }
            ]
        }
    }

OUT_ProcessOrder_minimal = {
    "OrderInfo": {
        "OrderIdentification": "GoodsOwnerOrderNumber",
        "OrderOperation": "CreateOrUpdate",
        "Communication": None,
        "ReferenceNumber": None,
        "GoodsOwnerOrderNumber": "000001",
        "SalesCode": None,
        "OrderRemark": None,
        "OrderServicePointCode": None,
        "ConsigneeOrderNumber": None,
        "WayOfDelivery": None,
        "TermsOfDelivery": None,
        "TermsOfPayment": None,
        "TransporterOrderNumber": None,
        "DeliveryInstruction": None,
        "DeliveryDate": datetime.strptime("2021-04-19", "%Y-%m-%d").date(),
        "ArrivalDate": None,
        "ArrivalDateFrom": None,
        "Language": None,
        "OrderType": None,
        "ProductionCode": None,
        "FreeText1": None,
        "FreeText2": None,
        "FreeText3": None,
        "MarketPlace": None,
        "MarketPlaceOrderNumber": None,
        "WarehouseInstruction": None,
        "WayBill": None,
        "OrderClasses": None,
        "WayOfDeliveryType": None
    },
    "Customer": {
        "CustomerOperation": "CreateOrUpdate",
        "CustomerIdentification": "CustomerNumber",
        "CustomerNumber": "185432",
        "Name": "Stark Johansson AB",
        "Address": None,
        "Address2": None,
        "PostCode": None,
        "City": None,
        "CountryCode": None,
        "IsVisible": False,
        "NotifyBySMS": False,
        "NotifyByEmail": False,
        "NotifyByTelephone": False,
        "InvoiceAddress": None
    },
    "CustomerOrderLines": {
        "CustomerOrderLine": [
            {
                "OrderLineIdentification": "ExternalOrderLineCode",
                "ArticleIdentification": "ArticleNumber",
                "SubOrderLineSpecification": "ArticleRegisterSpecification",
                "DeliveryDate": datetime.strptime("2021-04-19", "%Y-%m-%d").date(),
                "ExternalOrderLineCode": "10",
                "OrderLineComment": None,
                "ArticleNumber": "200088",
                "ArticleName": None,
                "LinePrice": 1.1,
                "NumberOfItems": 1.2,
                "CurrencyCode": "SEK",
                "DoPick": True,
                "ForcePickFullItems": False,
                "OrderLineArticleItemStatus": {
                    "Identification": "ArticleItemStatusCode",
                    "Operation": "Find",
                    "ArticleItemStatusCode": "string",
                    "IsLocked": False
                },
                "SubOrderLines": None,
                "WarehouseInstruction": None,
                "CustomerArticleNumber": None
            }
        ]
    }
}

IN_ProcessOrder_full = {
        "OrderInfo": {
            "OrderIdentification": "GoodsOwnerOrderNumber",
            "OrderOperation": "CreateOrUpdate",
            "GoodsOwnerOrderNumber": "000001",
            "DeliveryDate": "2021-04-19",
            "ArrivalDate": "2021-04-20",
            "ArrivalDateFrom": "2021-04-21",
            "OrderType": {
                "OrderTypeOperation": "CreateOrFind",
                "OrderTypeIdentification": "OrderTypeName",
                "OrderTypeName": "test_OrderTypeName"
            },
            "OrderClasses": {
                "Operation": "FindOrCreate",
                "Identification": "test_Identification",
                "Classes": {
                    "Class": [
                        {
                           "Name": "test_ClassName",
                            "Code": "test_ClassCode"
                        }
                    ]
                }
            },
            "WayOfDeliveryType": {
                "WayOfDeliveryTypeOperation": "CreateOrFind",
                "WayOfDeliveryTypeIdentification": "Name",
                "Name": "test_WayOfDeliveryTypeName"
            }
        },
        "Customer": {
            "CustomerOperation": "CreateOrUpdate",
            "CustomerIdentification": "CustomerNumber",
            "CustomerNumber": "185432",
            "Name": "Stark Johansson AB",
            "IsVisible": False,
            "NotifyBySMS": False,
            "NotifyByEmail": False,
            "NotifyByTelephone": False,
            "InvoiceAddress": {
                "Name": "Test_client"
            }
        },
        "CustomerOrderLines": {
            "CustomerOrderLine": [
                {
                    "OrderLineIdentification": "ExternalOrderLineCode",
                    "ArticleIdentification": "ArticleNumber",
                    "SubOrderLineSpecification": "ArticleRegisterSpecification",
                    "DeliveryDate": "2021-04-19",
                    "ExternalOrderLineCode": "10",
                    "ArticleNumber": "200088",
                    "LinePrice": 1.1,
                    "NumberOfItems": 1.2,
                    "CurrencyCode": "SEK",
                    "DoPick": True,
                    "ForcePickFullItems": False,
                    "OrderLineArticleItemStatus": {
                        "Identification": "ArticleItemStatusCode",
                        "Operation": "Find",
                        "ArticleItemStatusCode": "string"
                    },
                    "SubOrderLines": {
                        "SubOrderLine": [
                            {
                                "CustomerOrderLine": {
                                    "OrderLineIdentification": "ExternalOrderLineCode",
                                    "ArticleIdentification": "ArticleNumber",
                                    "SubOrderLineSpecification": "ArticleRegisterSpecification",
                                    "DeliveryDate": "2021-04-19",
                                    "ExternalOrderLineCode": "10",
                                    "ArticleNumber": "200089",
                                    "LinePrice": 1.1,
                                    "NumberOfItems": 1.2,
                                    "CurrencyCode": "SEK",
                                    "DoPick": True,
                                    "ForcePickFullItems": False,
                                    "OrderLineArticleItemStatus": {
                                        "Identification": "ArticleItemStatusCode",
                                        "Operation": "Find",
                                        "ArticleItemStatusCode": "string"
                                    }
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }

OUT_ProcessOrder_full = {
    "OrderInfo": {
        "OrderIdentification": "GoodsOwnerOrderNumber",
        "OrderOperation": "CreateOrUpdate",
        "Communication": None,
        "ReferenceNumber": None,
        "GoodsOwnerOrderNumber": "000001",
        "SalesCode": None,
        "OrderRemark": None,
        "OrderServicePointCode": None,
        "ConsigneeOrderNumber": None,
        "WayOfDelivery": None,
        "TermsOfDelivery": None,
        "TermsOfPayment": None,
        "TransporterOrderNumber": None,
        "DeliveryInstruction": None,
        "DeliveryDate": datetime.strptime("2021-04-19", "%Y-%m-%d").date(),
        "ArrivalDate": datetime.strptime("2021-04-20", "%Y-%m-%d").date(),
        'ArrivalDateFrom': datetime.strptime("2021-04-21", "%Y-%m-%d").date(),
        "Language": None,
        "OrderType": {
            "OrderTypeOperation": "CreateOrFind",
            "OrderTypeIdentification": "OrderTypeName",
            "OrderTypeName": "test_OrderTypeName"
        },
        "ProductionCode": None,
        "FreeText1": None,
        "FreeText2": None,
        "FreeText3": None,
        "MarketPlace": None,
        "MarketPlaceOrderNumber": None,
        "WarehouseInstruction": None,
        "WayBill": None,
        "OrderClasses": {
            "Operation": "FindOrCreate",
            "Identification": "test_Identification",
            "Classes": {
                "Class": [
                    {
                        "Name": "test_ClassName",
                        "Code": "test_ClassCode",
                        "Comment": None
                    }   
                ]
            }
        },
        "WayOfDeliveryType": {
            "WayOfDeliveryTypeOperation": "CreateOrFind",
            "WayOfDeliveryTypeIdentification": "Name",
            "Name": "test_WayOfDeliveryTypeName"
        }
    },
    "Customer": {
        "CustomerOperation": "CreateOrUpdate",
        "CustomerIdentification": "CustomerNumber",
        "CustomerNumber": "185432",
        "Name": "Stark Johansson AB",
        "Address": None,
        "Address2": None,
        "PostCode": None,
        "City": None,
        "CountryCode": None,
        "IsVisible": False,
        "NotifyBySMS": False,
        "NotifyByEmail": False,
        "NotifyByTelephone": False,
        'InvoiceAddress': {
            "Name": "Test_client",
            "Address": None,
            "Address2": None,
            "PostCode": None,
            "City": None,
            "CountryCode": None,
            "IsVisible": True,
            "NotifyBySMS": False,
            "NotifyByEmail": False,
            "NotifyByTelephone": False
        }
    },
    "CustomerOrderLines": {
        "CustomerOrderLine": [
            {
                "OrderLineIdentification": "ExternalOrderLineCode",
                "ArticleIdentification": "ArticleNumber",
                "SubOrderLineSpecification": "ArticleRegisterSpecification",
                "DeliveryDate": datetime.strptime("2021-04-19", "%Y-%m-%d").date(),
                "ExternalOrderLineCode": "10",
                "OrderLineComment": None,
                "ArticleNumber": "200088",
                "ArticleName": None,
                "LinePrice": 1.1,
                "NumberOfItems": 1.2,
                "CurrencyCode": "SEK",
                "DoPick": True,
                "ForcePickFullItems": False,
                "OrderLineArticleItemStatus": {
                    "Identification": "ArticleItemStatusCode",
                    "Operation": "Find",
                    "ArticleItemStatusCode": "string",
                    "IsLocked": False
                },
                "SubOrderLines": {
                    "SubOrderLine": [
                        {
                            "CustomerOrderLine": {
                                "OrderLineIdentification": "ExternalOrderLineCode",
                                "ArticleIdentification": "ArticleNumber",
                                "SubOrderLineSpecification": "ArticleRegisterSpecification",
                                "DeliveryDate": datetime.strptime("2021-04-19", "%Y-%m-%d").date(),
                                "ExternalOrderLineCode": "10",
                                "OrderLineComment": "",
                                "ArticleNumber": "200089",
                                "ArticleName": '',
                                "LinePrice": 1.1,
                                "NumberOfItems": 1.2,
                                "CurrencyCode": "SEK",
                                "DoPick": True,
                                "ForcePickFullItems": False,
                                "OrderLineArticleItemStatus": {
                                    "Identification": "ArticleItemStatusCode",
                                    "Operation": "Find",
                                    "ArticleItemStatusCode": "string",
                                    "IsLocked": False
                                },
                                "WarehouseInstruction": None,
                                "CustomerArticleNumber": None
                            }
                        }
                    ]
                },
                "WarehouseInstruction": None,
                "CustomerArticleNumber": None
            }
        ]
    }
}