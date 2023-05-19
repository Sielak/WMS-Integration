from typing import List
from pydantic import BaseModel



class GoodsOperationOrderHeader(BaseModel):
    GoodsOperationOrderNumber: str
    GoodsOperationOrderStatusId: int
    NumberOfItems: float
    ExecutedNumberOfItems: float

class Article(BaseModel):
    ArticleNumber: str

class FromArticleItemStatus(BaseModel):
    ArticleItemStatusCode: str

class ToArticleItemStatus(BaseModel):
    ArticleItemStatusCode: str

class GoodsOperationOrderLineInfo(BaseModel):
    GoodsOperationOrderLineNumber: str
    Article: Article
    FromArticleItemStatus: FromArticleItemStatus
    ToArticleItemStatus: ToArticleItemStatus
    NumberOfItems: float
    ExecutedNumberOfItems: float

class GoodsOperationOrderLines(BaseModel):
    GoodsOperationOrderLineInfo: List[GoodsOperationOrderLineInfo]

class GetGoodsOperationOrdersByQueryResponse(BaseModel):
    GoodsOperationOrderHeader: GoodsOperationOrderHeader
    GoodsOperationOrderLines: GoodsOperationOrderLines