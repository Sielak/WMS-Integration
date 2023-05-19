import json
from typing import List, Optional
from pydantic import BaseModel, Field
from enum import Enum
from datetime import date, datetime


class Output(str, Enum):
    xml = "xml"
    json = "json"

class ProductionOrderHeader(BaseModel):
    GoodsOwnerId: int
    Comment: str
    OrderNumber: str
    ProductionDate: date
    OrderedNumberOfItems: float
    ProducedNumberOfItems: float
    StartProductionTime: datetime
    EndProductionTime: datetime
    ProductionOrderId: int
    ProductionOrderStatus: int

class ProductionOrderLineConsumedInfo(BaseModel):
    ArticleName: str
    ArticleNumber: str
    NumberOfItems: float
    ArticleUnitCode: str
    ProducedArticleItemId: int

class Consumed(BaseModel):
    ProductionOrderLineConsumedInfo: List[ProductionOrderLineConsumedInfo]

class ProductionOrderLineProducedInfo(BaseModel):
    ArticleName: str
    ArticleNumber: str
    NumberOfItems: float
    ArticleUnitCode: str
    ArticleItemId: int

class Produced(BaseModel):
    ProductionOrderLineProducedInfo: List[ProductionOrderLineProducedInfo]

class ProductionOrderLineInfo(BaseModel):
    ArticleName: str
    ArticleNumber: str
    ProductionOrderLineId: int
    OrderedNumberOfItems: float
    ProducedNumberOfItems: float
    ArticleUnitCode: str
    Consumed: Optional[Consumed]
    Produced: Optional[Produced]
    ProductionOrderLineNumber: str
    ReportedNumberOfItems: Optional[float]

class ProductionOrderLines(BaseModel):
    ProductionOrderLineInfo: List[ProductionOrderLineInfo]        

class GetProductionOrdersByQueryResponse(BaseModel):
    ProductionOrderHeader: ProductionOrderHeader
    ProductionOrderLines: ProductionOrderLines
 