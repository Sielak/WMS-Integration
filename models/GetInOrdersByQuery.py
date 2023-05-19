from typing import List, Optional
from pydantic import BaseModel, Field


class InOrderInfo(BaseModel):
    InOrderId: int
    GoodsOwnerOrderNumber: str
    AdvisedNumberOfItems: float
    ReceivedNumberOfItems: float
    InOrderTypeName: Optional[str]
    InOrderTypeCode: Optional[str]
    InOrderIsReturnType: bool
    InOrderFreeDecimal1: Optional[float]

class GoodsOwner(BaseModel):
    GoodsOwnerCode: str = Field(None, min_length=1, max_length=300)

class WsiSystem(BaseModel):
    GoodsOwnerId: int

class Article(BaseModel):
    ArticleNumber: str

class ReceivedInOrderLine(BaseModel):
    Article: Article
    ExternalOrderLineCode: str = Field(None, min_length=1, max_length=300)
    AdvisedNumberOfItems: float
    ReceivedNumberOfItems: float
    CreatedNumberOfItems: float
    InOrderLineId: int
    ParentInOrderLineId: Optional[int]

class ReceivedInOrderLines(BaseModel):
    ReceivedInOrderLine: List[ReceivedInOrderLine]        

class GetInOrdersByQueryResponse(BaseModel):
    InOrderInfo: InOrderInfo
    GoodsOwner: GoodsOwner
    WsiSystem: WsiSystem
    ReceivedInOrderLines: ReceivedInOrderLines
    Warehouse: Optional[str]
    