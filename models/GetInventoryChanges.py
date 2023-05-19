from typing import List
from pydantic import BaseModel, Field
from datetime import datetime

class Article(BaseModel):
    Name: str = Field(None, min_length=1, max_length=200)
    ArticleNumber: str = Field(..., min_length=1, max_length=100)
    ArticleUnitCode: str = Field(None, min_length=1, max_length=50)


class InventoryTransaction(BaseModel): 
    InventoryChangesNumberOfItems: float   
    InventoryTime: datetime	
    InventoryId: int	
    InventoryItemComment: str = Field(None, min_length=1, max_length=100)
    Location: str = Field(None, min_length=1, max_length=50)
    InventoryAdjustmentCauseCode: str = Field(None, min_length=1, max_length=50)
    InventoryAdjustmentCauseName: str = Field(None, min_length=1, max_length=50)
    ArticleItemStatusCode: str = Field(None, min_length=1, max_length=50)
    ArticleItemStatusName: str = Field(None, min_length=1, max_length=50)
    WarehouseCode: str = Field(None, min_length=1, max_length=50)
    WarehouseId: int

class InventoryTransactions(BaseModel):
    InventoryTransaction: List[InventoryTransaction]

class InventoryChangeLine(BaseModel):
    Article: Article
    InventoryChangesNumberOfItems: float
    InventoryTransactions: InventoryTransactions

