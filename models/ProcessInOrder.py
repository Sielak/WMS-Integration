from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum
from datetime import datetime

class IdentifyTheInorder(str, Enum):
    ExternalOrderCode  = 'ExternalOrderCode'
    GoodsOwnerOrderNumber = 'GoodsOwnerOrderNumber'
    SystemId = 'SystemId'

class OrderOperation(str, Enum):
    CreateOrUpdate = 'CreateOrUpdate'
    Create = 'Create'
    Remove = 'Remove'

class WayOfDeliveryTypeOperation(str, Enum):
    CreateOrUpdate = 'CreateOrUpdate'
    Find = 'Find'

class WayOfDeliveryTypeIdentification(str, Enum):
    Code = 'Code'
    Name = 'Name'

class WayOfDeliveryType(BaseModel):
    WayOfDeliveryTypeOperation: WayOfDeliveryTypeOperation
    WayOfDeliveryTypeIdentification: WayOfDeliveryTypeIdentification
    Name: str = Field(None, min_length=1, max_length=100)
    
    class Config:  
        use_enum_values = True

class InOrderTypeOperation(str, Enum):
    Find = 'Find'
    CreateOrFind = 'CreateOrFind'

class InOrderTypeIdentification(str,Enum):
    Code = 'Code'
    Name = 'Name'
    InOrderTypeName = 'InOrderTypeName'

class InOrderType(BaseModel):
    InOrderTypeOperation: InOrderTypeOperation
    InOrderTypeIdentification: InOrderTypeIdentification
    InOrderTypeName: str = Field(None, min_length=1, max_length=100)

    class Config:  
        use_enum_values = True

class InOrderWarehouseIdentification(str, Enum):
    WarehouseCode = 'WarehouseCode'
    WarehouseName = 'WarehouseName'
    WarehouseId = 'WarehouseId'

class Warehouse(BaseModel):
    InOrderWarehouseIdentification: Optional[InOrderWarehouseIdentification]
    InOrderWarehouseOperation: Optional[str] = Field('Find', min_length=1, max_length=50)
    WarehouseCode: Optional[str] = Field(None, min_length=1, max_length=50)
    WarehouseName: str = Field(None, min_length=1, max_length=20)
    WarehouseId: Optional[int]
    
    class Config:  
        use_enum_values = True

class InOrderInfo(BaseModel):
    InOrderIdentification: IdentifyTheInorder
    InOrderOperation: OrderOperation
    GoodsOwnerOrderNumber: Optional[str] = Field(None, min_length=1, max_length=50)
    SupplierOrderNumber: Optional[str] = Field(None, min_length=1, max_length=50)
    GoodsOwnerReference: Optional[str] = Field(None, min_length=1, max_length=100)
    ReferenceNumber: Optional[str] = Field(None, min_length=1, max_length=50)
    WayOfDelivery: Optional[str] = Field(None, min_length=1, max_length=50)
    OrderRemark: Optional[str] = Field(None, min_length=1, max_length=1000)
    InDate: Optional[datetime]   
    OrderDate: Optional[datetime]
    OrderStatusUpdated: Optional[int]
    InOrderType: Optional[InOrderType]
    InOrderIsReturnType: Optional[bool] = False
    InvoiceNumber: Optional[str] = Field(None, min_length=1, max_length=100)
    InOrderFreeDecimal1: Optional[float]
    Warehouse: Optional[Warehouse]
    WayOfDeliveryType: Optional[WayOfDeliveryType]
    FreeText1: Optional[str] = Field(None, min_length=1, max_length=300)

    class Config:  
        use_enum_values = True


class InOrderSupplierIdentificationType(str, Enum):
    SupplierNumber = 'SupplierNumber'
    FullNameAndAdress = 'FullNameAndAdress'
    SupplierName = 'SupplierName'

class InOrderSupplierOperation(str, Enum):
    CreateOrUpdate = 'CreateOrUpdate'
    Find = 'Find'

class SupplierGroupOperation(str, Enum):
    FindOrCreate = 'FindOrCreate'
    Clear = 'Clear'

class InOrderSupplierSupplierGroup(BaseModel):
    SupplierGroupOperation: SupplierGroupOperation
    SupplierGroupCode: str =  Field(None, min_length=1, max_length=50)

    class Config:  
        use_enum_values = True

class Address(BaseModel):
    Name: str =  Field(None, min_length=1, max_length=200)
    Address: str =  Field(None, min_length=1, max_length=200)
    Address2: str =  Field(None, min_length=1, max_length=200)
    PostCode: str =  Field(None, min_length=1, max_length=50)
    City: str =  Field(None, min_length=1, max_length=200)
    CountryCode: str =  Field(None, min_length=1, max_length=2)
    DeliveryInstruction: str =  Field(None, min_length=1, max_length=200)
    IsVisible: Optional[bool]
    NotifyBySMS: Optional[bool] = False
    NotifyByEmail: Optional[bool] = False
    NotifyByTelephone: Optional[bool] = False

class InOrderSupplier(BaseModel):
    InOrderSupplierIdentificationType: InOrderSupplierIdentificationType
    InOrderSupplierOperation: InOrderSupplierOperation
    SupplierNumber: Optional[str] = Field(None, min_length=1, max_length=200)
    SupplierName: Optional[str] = Field(None, min_length=1, max_length=200)
    SupplierGroup: Optional[InOrderSupplierSupplierGroup]
    Address: Optional[Address]
    
    class Config:  
        use_enum_values = True


class OrderLineIdentification(str, Enum):
    ExternalOrderLineCode = 'ExternalOrderLineCode'
    ArticleNumber = 'ArticleNumber'
    ArticleName = 'ArticleName'
    ExternalOrderLineId = 'ExternalOrderLineId'
    SystemId = 'SystemId'

class ArticleIdentification(str, Enum):
    ArticleNumber = 'ArticleNumber'
    SystemId = 'SystemId'
    ProductCode = 'ProductCode'
    ArticleName = 'ArticleName'

class InOrderLineArticleItemStatusIdentification(str, Enum):
    ArticleItemStatusCode = 'ArticleItemStatusCode'
    ArticleItemStatusId = 'ArticleItemStatusId'

class InOrderLineTypeIdentificationType(str, Enum):
    InOrderLineTypeName = 'InOrderLineTypeName'
    InOrderLineTypeCode = 'InOrderLineTypeCode'

class InOrderLineTypeOperation(str, Enum):
    CreateOrUpdate = 'CreateOrUpdate'
    Find = 'Find'

class InOrderLineArticleItemStatus(BaseModel):
    InOrderLineArticleItemStatusIdentification: InOrderLineArticleItemStatusIdentification
    ArticleItemStatusId: Optional[int]
    ArticleItemStatusCode: str = Field(None, min_length=1, max_length=50)

    class Config:  
        use_enum_values = True

class InOrderLineType(BaseModel):
    InOrderLineTypeIdentificationType: InOrderLineTypeIdentificationType
    InOrderLineTypeOperation: InOrderLineTypeOperation
    InOrderLineTypeCode: str
    InOrderLineTypeName: str

    class Config:  
        use_enum_values = True

class InOrderLineArticleItem(BaseModel):
    Serial: str = Field(None, min_length=1, max_length=128)
    ContainerNo: str = Field(None, min_length=1, max_length=50)
    Volume: Optional[float]
    Weight: Optional[float]
    Length: Optional[float]
    Width: Optional[float]
    Height: Optional[float]
    # InOrderLineArticleItemStatus: InOrderLineArticleItemStatus
    NumberOfItems: Optional[float]

class Items(BaseModel):
    InOrderLineArticleItem: List[InOrderLineArticleItem]

class InOrderLine(BaseModel):
    OrderLineIdentification: OrderLineIdentification
    ArticleIdentification: ArticleIdentification
    ExternalOrderLineCode: Optional[str] = Field(None, min_length=1, max_length=40)
    Indate: Optional[datetime]
    OrderLineComment: Optional[str] = Field(None, min_length=1, max_length=150)
    ArticleNumber: str = Field(None, min_length=1, max_length=100)
    ArticleName: str = Field(None, min_length=1, max_length=200)
    CurrencyCode: Optional[str] = Field('NOK', min_length=1, max_length=20)
    NumberOfItems: float
    RowPrice: Optional[float]
    SupplierNumberOfItems: Optional[float]
    InOrderLineFreeDecimal1: Optional[float]
    InOrderLineArticleItemStatus: InOrderLineArticleItemStatus
    InOrderLineType: Optional[InOrderLineType]
    Items: Optional[Items]

    class Config:  
        use_enum_values = True

class InOrderLines(BaseModel):
    InOrderLine: List[InOrderLine]

class ProcessInOrder(BaseModel):
    InOrderInfo: InOrderInfo
    InOrderSupplier: Optional[InOrderSupplier]
    InOrderLines: InOrderLines
    

