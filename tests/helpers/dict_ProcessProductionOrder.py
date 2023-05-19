from datetime import datetime

IN_ProcessProductionOrder_full = {
        "ProductionOrderIdentification": "ProductionOrderNumber",
        "ProductionOrderNumber": "00001_integration",
        "ProductionDate": "2021-04-15",
        "ProductionOrderLines": {
            "ProductionOrderLine": [
                {
                    "ProductionOrderLineIdentification": "ProductionOrderLineNumber",
                    "ToProduceNumberOfItems": 1.1,
                    "ArticleNumber": "150829",
                    "ProductionOrderLineNumber": "10"
                }
            ]
        }
    }
OUT_ProcessProductionOrder_full = {
        "ProductionOrderIdentification": "ProductionOrderNumber",
        "ProductionOrderNumber": "00001_integration",
        "ProductionOrderComment": None,
        "ProductionDate": datetime.strptime("2021-04-15", "%Y-%m-%d").date(),
        "ProductionOrderLines": {
            "ProductionOrderLine": [
                {
                    "ProductionOrderLineIdentification": "ProductionOrderLineNumber",
                    "ToProduceNumberOfItems": 1.1,
                    "ArticleNumber": "150829",
                    "ProductionOrderLineNumber": "10"
                }
            ]
        }
    }