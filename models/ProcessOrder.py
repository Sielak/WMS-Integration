from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Optional, List
from enum import Enum

class OrderIdentification(str, Enum):
    GoodsOwnerOrderNumber = 'GoodsOwnerOrderNumber'
    ReferenceNumber = 'ReferenceNumber'
    SystemId = 'SystemId'
    GoodsOwnerOrderId = 'GoodsOwnerOrderId'

class OrderOperation(str, Enum):
    CreateOrUpdate = 'CreateOrUpdate'
    Create = 'Create'
    Update = 'Update'
    Remove = 'Remove'

class OrderTypeOperation(str, Enum):
    Find = 'Find'
    CreateOrFind = 'CreateOrFind'

class OrderTypeIdentification(str, Enum):
    OrderTypeCode = 'OrderTypeCode'
    OrderTypeName = 'OrderTypeName'

class CustomerOperation(str, Enum):
    Create = 'Create'
    CreateOrUpdate = 'CreateOrUpdate'
    CreateNotUpdate = 'CreateNotUpdate'
    Find = 'Find'

class CustomerIdentification(str, Enum):
    ExternalCustomerCode = 'ExternalCustomerCode'
    SystemId = 'SystemId'
    CustomerNumber = 'CustomerNumber'
    FullNameAndAddress = 'FullNameAndAddress'

class OrderLineIdentification(str, Enum):
    ExternalOrderLineCode = 'ExternalOrderLineCode'
    ArticleNumber = 'ArticleNumber'
    ArticleName = 'ArticleName'
    ExternalOrderLineId  = 'ExternalOrderLineId'
    SystemId  = 'SystemId'

class ArticleIdentification(str, Enum):
    ExternalOrderLineCode = 'ExternalOrderLineCode'
    ArticleNumber = 'ArticleNumber'
    ArticleName = 'ArticleName'
    ExternalOrderLineId  = 'ExternalOrderLineId'

class SubOrderLineSpecification(str, Enum):
    ArticleRegisterSpecification = 'ArticleRegisterSpecification'
    RequestSpecification = 'RequestSpecification'

class Identification(str, Enum):
    ArticleItemStatusCode = 'ArticleItemStatusCode'

class Operation(str, Enum):
    Find = 'Find'  
    FindOrCreate = 'FindOrCreate'

class WayOfDeliveryTypeOperation(str, Enum):
    CreateOrUpdate = 'CreateOrUpdate'  
    CreateOrFind = 'CreateOrFind'
    Find = 'Find'

class WayOfDeliveryTypeIdentification(str, Enum):
    Code = 'Code'  
    Name = 'Name'

class OrderType(BaseModel):
    OrderTypeOperation: OrderTypeOperation
    OrderTypeIdentification: OrderTypeIdentification
    OrderTypeName: str = Field(..., min_length=1, max_length=50)

    class Config:  
        use_enum_values = True

class Class(BaseModel):
    Name: str
    Code: str
    Comment: str = Field(None, min_length=1, max_length=500)

class Classes(BaseModel):
    Class: List[Class]

class OrderClasses(BaseModel):
    Operation: Operation
    Identification: str
    Classes: Optional[Classes]

    class Config:  
        use_enum_values = True

class WayOfDeliveryType(BaseModel):
    WayOfDeliveryTypeOperation: WayOfDeliveryTypeOperation
    WayOfDeliveryTypeIdentification: WayOfDeliveryTypeIdentification
    Name: str = Field(..., min_length=1, max_length=100)

    class Config:  
            use_enum_values = True

class OrderInfo(BaseModel):
    OrderIdentification: OrderIdentification
    OrderOperation: OrderOperation
    Communication: str = Field(None, min_length=1, max_length=100)
    ReferenceNumber:  str = Field(None, min_length=1, max_length=50)
    GoodsOwnerOrderNumber: str = Field(..., min_length=1, max_length=50)  # ... means required
    SalesCode: str = Field(None, min_length=1, max_length=500)
    OrderRemark: str = Field(None, min_length=1, max_length=500)
    ConsigneeOrderNumber: str = Field(None, min_length=1, max_length=150)
    WayOfDelivery: str = Field(None, min_length=1, max_length=50)
    TermsOfDelivery: str = Field(None, min_length=1, max_length=50)
    TermsOfPayment: str = Field(None, min_length=1, max_length=50)
    DeliveryInstruction: str = Field(None, min_length=1, max_length=300)
    TransporterOrderNumber: str = Field(None, min_length=1, max_length=150)
    DeliveryDate: date
    ArrivalDateFrom: Optional[date]
    ArrivalDate: Optional[date]
    WayBill: str = Field(None, min_length=1, max_length=50)
    Language: str = Field(None, min_length=1, max_length=20)
    OrderType: Optional[OrderType]
    ProductionCode: str = Field(None, min_length=1, max_length=30)
    OrderServicePointCode: str = Field(None, min_length=1, max_length=50)
    FreeText1: str = Field(None, min_length=1, max_length=300)
    FreeText2: str = Field(None, min_length=1, max_length=300)
    FreeText3: str = Field(None, min_length=1, max_length=300)
    MarketPlace: str = Field(None, min_length=1, max_length=100)
    MarketPlaceOrderNumber: str = Field(None, min_length=1, max_length=100)
    WarehouseInstruction: str = Field(None, min_length=1, max_length=500)
    OrderClasses: Optional[OrderClasses]
    WayOfDeliveryType: Optional[WayOfDeliveryType]

    class Config:  
        use_enum_values = True

class InvoiceAddress(BaseModel):
    Name: str = Field(None, min_length=1, max_length=200)
    Address: str = Field(None, min_length=1, max_length=200)
    Address2: str = Field(None, min_length=1, max_length=200)
    PostCode: str = Field(None, min_length=1, max_length=50)
    City: str = Field(None, min_length=1, max_length=200)
    CountryCode: str = Field(None, min_length=1, max_length=2)
    IsVisible: bool = True
    NotifyBySMS: bool = False
    NotifyByEmail: bool = False
    NotifyByTelephone: bool = False

class Customer(BaseModel):
    CustomerOperation: CustomerOperation
    CustomerIdentification: CustomerIdentification
    CustomerNumber: str = Field(..., min_length=1, max_length=50)
    Name: str = Field(..., min_length=1, max_length=200)
    Address: str = Field(None, min_length=1, max_length=200)
    Address2: str = Field(None, min_length=1, max_length=200)
    PostCode: str = Field(None, min_length=1, max_length=50)
    City: str = Field(None, min_length=1, max_length=200)
    CountryCode: str = Field(None, min_length=1, max_length=2)
    IsVisible: bool
    NotifyBySMS: bool
    NotifyByEmail: bool
    NotifyByTelephone: bool
    InvoiceAddress: Optional[InvoiceAddress]

    class Config:  
        use_enum_values = True   

class OrderLineArticleItemStatus(BaseModel):
    Identification: Identification
    Operation: Operation
    ArticleItemStatusCode: str = Field(..., min_length=1, max_length=100)
    IsLocked: bool = False

    class Config:  
        use_enum_values = True  

class CustomerOrderLine2(BaseModel):
    OrderLineIdentification: OrderLineIdentification
    ArticleIdentification: ArticleIdentification
    SubOrderLineSpecification: SubOrderLineSpecification
    DeliveryDate: date
    ExternalOrderLineCode: str = Field(None, min_length=1, max_length=40)
    OrderLineComment: str = Field('', min_length=1, max_length=300)
    ArticleNumber: str = Field(..., min_length=1, max_length=100)
    ArticleName: str = Field('', min_length=1, max_length=200)
    LinePrice: Optional[float]
    NumberOfItems: float
    CurrencyCode: str = Field(None, min_length=1, max_length=20)
    DoPick: bool
    ForcePickFullItems: bool
    OrderLineArticleItemStatus: OrderLineArticleItemStatus
    WarehouseInstruction: str = Field(None, min_length=1, max_length=300)
    CustomerArticleNumber: str = Field(None, min_length=1, max_length=100)

    class Config:  
        use_enum_values = True

class SubOrderLine(BaseModel):
    CustomerOrderLine: CustomerOrderLine2

class SubOrderLines(BaseModel):
    SubOrderLine: List[SubOrderLine]

class CustomerOrderLine(BaseModel):
    OrderLineIdentification: OrderLineIdentification
    ArticleIdentification: ArticleIdentification
    SubOrderLineSpecification: SubOrderLineSpecification
    DeliveryDate: date
    ExternalOrderLineCode: str = Field(None, min_length=1, max_length=40)
    OrderLineComment: str = Field(None, min_length=1, max_length=300)
    ArticleNumber: str = Field(..., min_length=1, max_length=100)
    ArticleName: str = Field(None, min_length=1, max_length=200)
    LinePrice: Optional[float]
    NumberOfItems: float
    CurrencyCode: str = Field(None, min_length=1, max_length=20)
    DoPick: bool
    ForcePickFullItems: bool
    OrderLineArticleItemStatus: OrderLineArticleItemStatus
    SubOrderLines: Optional[SubOrderLines]
    WarehouseInstruction: str = Field(None, min_length=1, max_length=300)
    CustomerArticleNumber: str = Field(None, min_length=1, max_length=100)

    class Config:  
        use_enum_values = True

class CustomerOrderLines(BaseModel):
    CustomerOrderLine: List[CustomerOrderLine]

    class Config:  
        use_enum_values = True  

class CustomerOrder(BaseModel):
    OrderInfo: OrderInfo
    Customer: Customer
    CustomerOrderLines: CustomerOrderLines

    class Config:  
        use_enum_values = True