IN_ProcessInOrder_minimal = {
        "InOrderInfo": {
            "InOrderIdentification": "GoodsOwnerOrderNumber",
            "InOrderOperation": "CreateOrUpdate"
        },
        "InOrderLines": {
            "InOrderLine": [
                {
                    "OrderLineIdentification": "ExternalOrderLineCode",
                    "ArticleIdentification": "ArticleNumber",
                    "NumberOfItems": 1.1,
                    "InOrderLineArticleItemStatus": {
                        "InOrderLineArticleItemStatusIdentification": "ArticleItemStatusCode"
                    }

                }
            ]
        }
    }

OUT_ProcessInOrder_minimal = {
        "InOrderInfo": {
            "InOrderIdentification": "GoodsOwnerOrderNumber",
            "InOrderOperation": "CreateOrUpdate",
            "GoodsOwnerOrderNumber": None,
            "SupplierOrderNumber": None,
            "GoodsOwnerReference": None,
            "ReferenceNumber": None,
            "WayOfDelivery": None,
            "OrderRemark": None,
            "InDate": None,
            "OrderDate": None,
            "OrderStatusUpdated": None,
            "InOrderType": None,
            "InOrderIsReturnType": False,
            "InvoiceNumber": None,
            "InOrderFreeDecimal1": None,
            "Warehouse": None,
            "WayOfDeliveryType": None,
            "FreeText1": None
        },
        "InOrderSupplier": None,
        "InOrderLines": {
            "InOrderLine": [
                {
                    "OrderLineIdentification": "ExternalOrderLineCode",
                    "ArticleIdentification": "ArticleNumber",
                    "ExternalOrderLineCode": None,
                    "Indate": None,
                    "OrderLineComment": None,
                    "ArticleNumber": None,
                    "ArticleName": None,
                    "CurrencyCode": "NOK",
                    "NumberOfItems": 1.1,
                    "RowPrice": None,
                    "SupplierNumberOfItems": None,
                    "InOrderLineFreeDecimal1": None,
                    "InOrderLineArticleItemStatus": {
                        "InOrderLineArticleItemStatusIdentification": "ArticleItemStatusCode",
                        "ArticleItemStatusId": None,
                        "ArticleItemStatusCode": None
                    },
                    "InOrderLineType": None,
                    "Items": None
                }
            ]
        }
    }

IN_ProcessInOrder_full = {
        "InOrderInfo": {
            "InOrderIdentification": "GoodsOwnerOrderNumber",
            "InOrderOperation": "CreateOrUpdate",
            "InOrderType": {
                "InOrderTypeOperation": "CreateOrFind",
                "InOrderTypeIdentification": "InOrderTypeName"
            },
            "Warehouse": {},
            "WayOfDeliveryType": {
                "WayOfDeliveryTypeOperation": "CreateOrUpdate",
                "WayOfDeliveryTypeIdentification": "Name"
            }
        },
        "InOrderSupplier": {
            "InOrderSupplierIdentificationType": "SupplierName",
            "InOrderSupplierOperation": "CreateOrUpdate",
            "SupplierGroup": {
                "SupplierGroupOperation": "FindOrCreate"
            },
            "Address": {}
        },
        "InOrderLines": {
            "InOrderLine": [
                {
                    "OrderLineIdentification": "ExternalOrderLineCode",
                    "ArticleIdentification": "ArticleNumber",
                    "NumberOfItems": 1.1,
                    "InOrderLineArticleItemStatus": {
                        "InOrderLineArticleItemStatusIdentification": "ArticleItemStatusCode"
                    },
                    "InOrderLineType": {
                        "InOrderLineTypeIdentificationType": "InOrderLineTypeName",
                        "InOrderLineTypeOperation": "CreateOrUpdate",
                        "InOrderLineTypeCode": "Test_InOrderLineTypeCode",
                        "InOrderLineTypeName": "Test_InOrderLineTypeName"
                    },
                    "Items": {
                        "InOrderLineArticleItem": [
                            {
                                "Serial": "Test_Serial",
                                "ContainerNo": "Test_ContainerNo",
                                "Volume": 1.1,
                                "Weight": 1.2,
                                "Length": 1.3,
                                "Width": 1.4,
                                "Height": 1.5,
                                "InOrderLineArticleItemStatus": {
                                    "InOrderLineArticleItemStatusIdentification": "ArticleItemStatusCode"
                                },
                                "NumberOfItems": 2.0
                            }
                        ]
                    }
                }
            ]
        }
    }
OUT_ProcessInOrder_full = {
        "InOrderInfo": {
            "InOrderIdentification": "GoodsOwnerOrderNumber",
            "InOrderOperation": "CreateOrUpdate",
            "GoodsOwnerOrderNumber": None,
            "SupplierOrderNumber": None,
            "GoodsOwnerReference": None,
            "ReferenceNumber": None,
            "WayOfDelivery": None,
            "OrderRemark": None,
            "InDate": None,
            "OrderDate": None,
            "OrderStatusUpdated": None,
            "InOrderType": {
                "InOrderTypeOperation": "CreateOrFind",
                "InOrderTypeIdentification": "InOrderTypeName",
                "InOrderTypeName": None
            },
            "InOrderIsReturnType": False,
            "InvoiceNumber": None,
            "InOrderFreeDecimal1": None,
            "Warehouse": {
                "InOrderWarehouseIdentification": None,
                "InOrderWarehouseOperation": "Find",
                "WarehouseCode": None,
                "WarehouseName": None,
                "WarehouseId": None
            },
            "WayOfDeliveryType": {
                "WayOfDeliveryTypeOperation": "CreateOrUpdate",
                "WayOfDeliveryTypeIdentification": "Name",
                "Name": None
            },
            "FreeText1": None
        },
        "InOrderSupplier": {
            "InOrderSupplierIdentificationType": "SupplierName",
            "InOrderSupplierOperation": "CreateOrUpdate",
            "SupplierNumber": None,
            "SupplierName": None,
            "SupplierGroup": {
                "SupplierGroupOperation": "FindOrCreate",
                "SupplierGroupCode": None
            },
            "Address": {
                "Name": None,
                "Address": None,
                "Address2": None,
                "PostCode": None,
                "City": None,
                "CountryCode": None,
                "DeliveryInstruction": None,
                "IsVisible": None,
                "NotifyBySMS": False,
                "NotifyByEmail": False,
                "NotifyByTelephone": False
            }
        },
        "InOrderLines": {
            "InOrderLine": [
                {
                    "OrderLineIdentification": "ExternalOrderLineCode",
                    "ArticleIdentification": "ArticleNumber",
                    "ExternalOrderLineCode": None,
                    "Indate": None,
                    "OrderLineComment": None,
                    "ArticleNumber": None,
                    "ArticleName": None,
                    "CurrencyCode": "NOK",
                    "NumberOfItems": 1.1,
                    "RowPrice": None,
                    "SupplierNumberOfItems": None,
                    "InOrderLineFreeDecimal1": None,
                    "InOrderLineArticleItemStatus": {
                        "InOrderLineArticleItemStatusIdentification": "ArticleItemStatusCode",
                        "ArticleItemStatusId": None,
                        "ArticleItemStatusCode": None
                    },
                    "InOrderLineType": {
                        "InOrderLineTypeIdentificationType": "InOrderLineTypeName",
                        "InOrderLineTypeOperation": "CreateOrUpdate",
                        "InOrderLineTypeCode": "Test_InOrderLineTypeCode",
                        "InOrderLineTypeName": "Test_InOrderLineTypeName"
                    },
                    "Items": {
                        "InOrderLineArticleItem": [
                            {
                                "Serial": "Test_Serial",
                                "ContainerNo": "Test_ContainerNo",
                                "Volume": 1.1,
                                "Weight": 1.2,
                                "Length": 1.3,
                                "Width": 1.4,
                                "Height": 1.5,
                                "NumberOfItems": 2.0
                            }
                        ]
                    }
                }
            ]
        }
    }