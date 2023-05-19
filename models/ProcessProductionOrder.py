from datetime import date
from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum


class ProductionOrderIdentification(str, Enum):
    ProductionOrderNumber = 'ProductionOrderNumber'

class ProductionOrderLineIdentification(str, Enum):
    ProductionOrderLineNumber = 'ProductionOrderLineNumber'

class ProductionOrderLine(BaseModel):
    ProductionOrderLineIdentification: ProductionOrderLineIdentification
    ToProduceNumberOfItems: float
    ArticleNumber: str = Field(..., min_length=1, max_length=100)
    ProductionOrderLineNumber: str = Field(..., min_length=1, max_length=50)

    class Config:  
        use_enum_values = True

class ProductionOrderLines(BaseModel):
    ProductionOrderLine: List[ProductionOrderLine]

class ProcessProductionOrder(BaseModel):
    ProductionOrderIdentification: ProductionOrderIdentification
    ProductionOrderNumber: str = Field(..., min_length=1, max_length=50)
    ProductionOrderComment: Optional[str] = Field(None, min_length=1, max_length=200)
    ProductionDate: date
    ProductionOrderLines: ProductionOrderLines

    class Config:  
        use_enum_values = True