from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum


class GoodsOperationOrderIdentification(str, Enum):
    GoodsOperationOrderNumber = 'GoodsOperationOrderNumber'

class GoodsOperationOrderLineIdentification(str, Enum):
    GoodsOperationOrderLineNumber = 'GoodsOperationOrderLineNumber'

class GoodsOperationOrderLineOperation(str, Enum):
    CreateOrUpdate = 'CreateOrUpdate'

class GoodsOperationOrderLineArticleIdentification(str, Enum):
    ArticleNumber = 'ArticleNumber'

class GoodsOperationOrderLineArticleOperation(str, Enum):
    Find = 'Find'
    CreateOrUpdate = 'CreateOrUpdate'

class Identification(str, Enum):
    ArticleItemStatusCode = 'ArticleItemStatusCode'

class Operation(str, Enum):
    Find = 'Find'
    CreateOrUpdate = 'CreateOrUpdate'

class ArticleItemStatus(BaseModel):
    Identification: Identification
    Operation: Operation
    ArticleItemStatusCode: str = Field(..., min_length=1, max_length=50)

    class Config:  
        use_enum_values = True

class GoodsOperationOrderLine(BaseModel):
    GoodsOperationOrderLineIdentification: GoodsOperationOrderLineIdentification
    GoodsOperationOrderLineOperation: GoodsOperationOrderLineOperation
    GoodsOperationOrderLineArticleIdentification: GoodsOperationOrderLineArticleIdentification
    GoodsOperationOrderLineArticleOperation: GoodsOperationOrderLineArticleOperation
    ArticleNumber: str = Field(..., min_length=1, max_length=100)
    NumberOfItems: float
    GoodsOperationOrderLineNumber: str = Field(..., min_length=1, max_length=100)    
    GoodsOperationOrderLineComment: str = Field(None, min_length=1, max_length=500)
    FromArticleItemStatus: Optional[ArticleItemStatus]
    ToArticleItemStatus: Optional[ArticleItemStatus]
    
    class Config:  
        use_enum_values = True

class GoodsOperationOrderLines(BaseModel):
    GoodsOperationOrderLine: List[GoodsOperationOrderLine]

class CustomerOwnStockOrder(BaseModel):
    GoodsOperationOrderIdentification: GoodsOperationOrderIdentification
    GoodsOperationOrderNumber: str = Field(..., min_length=1, max_length=100)
    GoodsOperationOrderComment: str = Field(None, min_length=1, max_length=500)
    GoodsOperationOrderReferenceNumber: str = Field(None, min_length=1, max_length=50)
    GoodsOperationOrderLines: GoodsOperationOrderLines
    
    class Config:  
        use_enum_values = True