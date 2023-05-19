from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum


class ReturnCustomerOrderIdentification(str, Enum):
    OrderId = 'OrderId'
    OrderNumber = 'OrderNumber'

class ReturnOrderIdentification(str, Enum):
    CustomerOrder = 'CustomerOrder'
    ReturnOrderNumber = 'ReturnOrderNumber'

class ReturnOrderLineIdentification(str, Enum):
    ExternalOrderLineCode = 'ExternalOrderLineCode'
    ArticleNumber = 'ArticleNumber'
    OrderLineId = 'OrderLineId'

class ReturnCauseOperation(str, Enum):
    FindOrCreate = 'FindOrCreate'
    Find = 'Find'
    SetUnknown = 'SetUnknown'

class ReturnCause(BaseModel):
    ReturnCauseOperation: ReturnCauseOperation
    ReturnCauseCode: str
    ReturnCauseName: str

    class Config:  
        use_enum_values = True

class ReturnOrderLine(BaseModel):
    ReturnOrderLineIdentification: ReturnOrderLineIdentification
    ToBeReturnedNumberOfItems: float
    ReturnOrderRowNumber: str
    ExternalOrderLineCode: str
    OrderLineId: Optional[int]
    ArticleNumber: str = Field(..., min_length=1, max_length=50)
    ReturnCause: Optional[ReturnCause]

    class Config:  
        use_enum_values = True

class ReturnOrderLines(BaseModel):
    ReturnOrderLine: List[ReturnOrderLine]

    class Config:  
        use_enum_values = True

class ReturnOrder(BaseModel):		
    ReturnCustomerOrderIdentification: ReturnCustomerOrderIdentification
    ReturnOrderIdentification: str
    ReturnCause: Optional[ReturnCause]
    CustomerOrderNumber: str
    ReturnOrderComment: Optional[str]
    ReturnOrderLines: ReturnOrderLines
    ReturnOrderNumber: str

    class Config:  
        use_enum_values = True
