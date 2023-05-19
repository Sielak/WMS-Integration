from datetime import datetime

IN_GetProductionOrdersByQueryResponse_minimal = {
    "ProductionOrderHeader": {
        "GoodsOwnerId": 1,
        "Comment": "",
        "OrderNumber": "",
        "ProductionDate": "2021-04-22",
        "OrderedNumberOfItems": 1.1,
        "ProducedNumberOfItems": 1.2,
        "StartProductionTime": "2021-04-22T15:53:18",
        "EndProductionTime": "2021-04-22T16:53:18",
        "ProductionOrderId": 2,
        "ProductionOrderStatus": 3
    },
    "ProductionOrderLines": {
        "ProductionOrderLineInfo": [
            {
                "ArticleName": "DBAM",
                "ArticleNumber": "200088",
                "ProductionOrderLineId": 1,
                "OrderedNumberOfItems": 2.1,
                "ProducedNumberOfItems": 3.1,
                "ArticleUnitCode": "pcs",
                "ProductionOrderLineNumber": "10"
            }
        ]
    }
}

OUT_GetProductionOrdersByQueryResponse_minimal = {
    "ProductionOrderHeader": {
        "GoodsOwnerId": 1,
        "Comment": "",
        "OrderNumber": "",
        "ProductionDate": datetime.strptime("2021-04-22", "%Y-%m-%d").date(),
        "OrderedNumberOfItems": 1.1,
        "ProducedNumberOfItems": 1.2,
        "StartProductionTime": datetime.strptime("2021-04-22T15:53:18", "%Y-%m-%dT%H:%M:%S"),
        "EndProductionTime": datetime.strptime("2021-04-22T16:53:18", "%Y-%m-%dT%H:%M:%S"),
        "ProductionOrderId": 2,
        "ProductionOrderStatus": 3
    },
    "ProductionOrderLines": {
        "ProductionOrderLineInfo": [
            {
                "ArticleName": "DBAM",
                "ArticleNumber": "200088",
                "ProductionOrderLineId": 1,
                "OrderedNumberOfItems": 2.1,
                "ProducedNumberOfItems": 3.1,
                "ArticleUnitCode": "pcs",
                "Consumed": None,
                "Produced": None,
                "ProductionOrderLineNumber": "10",
                "ReportedNumberOfItems": None
            }
        ]
    }
}

IN_GetProductionOrdersByQueryResponse_full = {
    "ProductionOrderHeader": {
        "GoodsOwnerId": 1,
        "Comment": "",
        "OrderNumber": "",
        "ProductionDate": "2021-04-22",
        "OrderedNumberOfItems": 1.1,
        "ProducedNumberOfItems": 1.2,
        "StartProductionTime": "2021-04-22T15:53:18",
        "EndProductionTime": "2021-04-22T16:53:18",
        "ProductionOrderId": 2,
        "ProductionOrderStatus": 3
    },
    "ProductionOrderLines": {
        "ProductionOrderLineInfo": [
            {
                "ArticleName": "DBAM",
                "ArticleNumber": "200088",
                "ProductionOrderLineId": 1,
                "OrderedNumberOfItems": 2.1,
                "ProducedNumberOfItems": 3.1,
                "ArticleUnitCode": "pcs",
                "Consumed": {
                    "ProductionOrderLineConsumedInfo": [
                        {
                            "ArticleName": "DBAM",
                            "ArticleNumber": "200088",
                            "NumberOfItems": 1.1,
                            "ArticleUnitCode": "pcs",
                            "ProducedArticleItemId": 1
                        }
                    ]
                },
                "Produced": {
                    "ProductionOrderLineProducedInfo": [
                        {
                            "ArticleName": "DBAM5",
                            "ArticleNumber": "200089",
                            "NumberOfItems": 1.2,
                            "ArticleUnitCode": "pcs",
                            "ArticleItemId": 2
                        }
                    ]
                },
                "ProductionOrderLineNumber": "10"
            }
        ]
    }
}

OUT_GetProductionOrdersByQueryResponse_full = {
    "ProductionOrderHeader": {
        "GoodsOwnerId": 1,
        "Comment": "",
        "OrderNumber": "",
        "ProductionDate": datetime.strptime("2021-04-22", "%Y-%m-%d").date(),
        "OrderedNumberOfItems": 1.1,
        "ProducedNumberOfItems": 1.2,
        "StartProductionTime": datetime.strptime("2021-04-22T15:53:18", "%Y-%m-%dT%H:%M:%S"),
        "EndProductionTime": datetime.strptime("2021-04-22T16:53:18", "%Y-%m-%dT%H:%M:%S"),
        "ProductionOrderId": 2,
        "ProductionOrderStatus": 3
    },
    "ProductionOrderLines": {
        "ProductionOrderLineInfo": [
            {
                "ArticleName": "DBAM",
                "ArticleNumber": "200088",
                "ProductionOrderLineId": 1,
                "OrderedNumberOfItems": 2.1,
                "ProducedNumberOfItems": 3.1,
                "ArticleUnitCode": "pcs",
                "Consumed": {
                    "ProductionOrderLineConsumedInfo": [
                        {
                            "ArticleName": "DBAM",
                            "ArticleNumber": "200088",
                            "NumberOfItems": 1.1,
                            "ArticleUnitCode": "pcs",
                            "ProducedArticleItemId": 1
                        }
                    ]
                },
                "Produced": {
                    "ProductionOrderLineProducedInfo": [
                        {
                            "ArticleName": "DBAM5",
                            "ArticleNumber": "200089",
                            "NumberOfItems": 1.2,
                            "ArticleUnitCode": "pcs",
                            "ArticleItemId": 2
                        }
                    ]
                },
                "ProductionOrderLineNumber": "10",
                "ReportedNumberOfItems": None
            }
        ]
    }
}