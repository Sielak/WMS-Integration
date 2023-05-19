from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from enum import Enum

class byUser(BaseModel):
    userId: Optional[int]

class byComputer(BaseModel):
    computerId: Optional[int]
    computerName: Optional[str]

class webhook_co(BaseModel):
    webhookOrdersId: int
    webhookEventId: int
    system: str
    timestamp: datetime
    orderId: int
    orderNumber: str
    goodsOwnerId: int
    path: str
    byUser: Optional[byUser]
    byComputer: Optional[byComputer]

class Consignee(BaseModel):
    Id: int
    NotifyByEmail: bool
    NotifyBySms: bool
    NotifyByTelephone: bool
    CustomerNumber: str = Field(..., min_length=1, max_length=50)
    CustomerNumberPallets: str = Field(None, min_length=1, max_length=50)


class GoodsInfo(BaseModel):
    NumberOfGoodsItems: int
    NumberOfPackages: int
    SummedGoodsItemParcels: int
    SummedGoodsItemWeight: float
    SummedGoodsItemVolume: float
    SummedGoodsItemLoadMeters: float
    SummedGoodsItemArea: float
    SummedArticleItemWeight: float
    SummedArticleItemVolume: float

class Operation(str, Enum):
    Find = 'Find'  
    FindOrCreate = 'FindOrCreate'

class OrderClassInfo(BaseModel):
    Name: str
    Code: str

class OrderClasses(BaseModel):
    OrderClassInfo: List[OrderClassInfo]
    
class OrderInfo(BaseModel):
    OrderId: int
    ReferenceNumber: str = Field(None, min_length=1, max_length=50)  # '' means optional
    GoodsOwnerOrderNumber: str = Field(None, min_length=1, max_length=50)  # '' means optional
    GoodsOwnerOrderId: str = Field(None, min_length=1, max_length=40)  # '' means optional
    WayOfDeliveryTypeName: str = Field(None, min_length=1, max_length=200)  # '' means optional
    PickedNumberOfItems: float
    OrderedNumberOfItems: float
    BackOrderForOrderId: Optional[int]
    CurrentShipmentId: Optional[int]
    OrderClasses: Optional[OrderClasses]


class WarehouseInfo(BaseModel):
    Name: str = Field(None, min_length=1, max_length=300)
    Code: str = Field(None, min_length=1, max_length=50)
    Id: int


class OrderShipmentPalletItemInfo(BaseModel):
    Id: int
    LabelId: str = Field(None, min_length=1, max_length=30)
    IsTaPalletItem: bool
    IsReturnTaPalletItem: bool
    Comment: str = Field(None, min_length=1, max_length=300)
    ParentPalletItemId: int
    PalletTypeCode: str
    TrackingUrl: str = Field(None, min_length=1, max_length=300)


class OrderCurrentShipmentInfo(BaseModel):
    Waybill: str = Field(None, min_length=1, max_length=50)
    StatusId: int
    ShipmentPalletItems: List[OrderShipmentPalletItemInfo]


class GoodsItem(BaseModel):
    Id: int
    GoodsItemLabelId: Optional[str]
    PackageTypeName: str = Field(None, min_length=1, max_length=100)
    PackageTypeCode: str = Field(None, min_length=1, max_length=50)
    Area: Optional[float]
    Weight: Optional[float]
    Volume: Optional[float]
    Height: Optional[float]
    Length: Optional[float]
    Width: Optional[float]
    LoadMeters: Optional[float]
    NumberOfItems: Optional[int]
    NumberOfPackages: Optional[int]
    ApprovedNumberOfPackages: Optional[int]


class GoodsItems(BaseModel):
    GoodsItem: List[GoodsItem]


class Article(BaseModel):
    ArticleNumber: str


class PickOrderInfo(BaseModel):
    PickOrderId: int
    BinIndex: int


class PickedOrderLine(BaseModel):
    Article: Article
    OrderLineSystemId: int
    DeliveryDate: datetime
    LastPickingTime: Optional[datetime]
    StartPickingTime: Optional[datetime]
    OrderedNumberOfItems: float
    PickedNumberOfItems: float
    ExternalOrderLineCode: str = Field(None, min_length=1, max_length=40)
    ParentExternalOrderLineCode: str = Field(None, min_length=1, max_length=40)
    ParentOrderLineId: Optional[int]
    IsParentLine: bool
    DoPick: bool
    RowPrice: Optional[float]
    ReportedNumberOfItems: Optional[float]
    AllocatedNumberOfItems: Optional[float]
    AcknowledgedNumberOfItems: Optional[float]
    OrderLineCaseNo: str = Field(None, min_length=1, max_length=100)
    CustomerArticleNumber: str = Field(None, min_length=1, max_length=100)
    PickOrderInfo: Optional[PickOrderInfo]
    ReportedReturnedNumberOfItems: Optional[float]
    IsPickedWithErrors: bool


class PickedOrderLines(BaseModel):
    PickedOrderLine: List[PickedOrderLine]


class InOrderInfo(BaseModel):
    InOrderId: int
    InOrderLineId: int


class ArticleItemPalletItemInfo(BaseModel):
    Id: int
    TypeCode: str = Field(None, min_length=1, max_length=50)
    LabelId: str = Field(None, min_length=1, max_length=30)
    # Parent: str = Field(None, min_length=1, max_length=30)
    Serial: str = Field(None, min_length=1, max_length=100)
    TypeLength: Optional[float]
    TypeWidth: Optional[float]
    TypeHeight: Optional[float]
    TypeWeight: Optional[float]


class PickedArticleItem(BaseModel):
    Article: Article
    ArticleItemId: int
    InDate: datetime
    Serial: str = Field(None, min_length=1, max_length=128)
    ExternalOrderLineCode: str = Field(None, min_length=1, max_length=40)
    LabelId: str = Field(None, min_length=1, max_length=30)
    NumberOfItems: float
    GoodsItemId: Optional[int]
    IsPicked: bool
    Returned: bool
    ShipmentId: Optional[int]
    ReturnDate: Optional[datetime]
    PickedTime: datetime
    OrderLineSystemId: int
    Weight: Optional[float]
    ArticleItemPalletItemInfo: Optional[ArticleItemPalletItemInfo]
    ReturnCauseCode: str = Field(None, min_length=1, max_length=100)
    ReturnCauseName: str = Field(None, min_length=1, max_length=200)
    Location: str = Field(None, min_length=1, max_length=50)
    LocationTypeCode: str = Field(None, min_length=1, max_length=50)
    InOrderInfo: Optional[InOrderInfo]
    PickedByUserId: int
    PickedByUserName: str = Field(None, min_length=1, max_length=50)
    WarehouseCode: str = Field(None, min_length=1, max_length=50)


class PickedArticleItems(BaseModel):
    PickedArticleItem: List[PickedArticleItem]


class Transporter(BaseModel):
    TransporterName: str = Field(None, min_length=1, max_length=80)


class OrderPalletItemInfo(BaseModel):
    Id: int
    TypeId: Optional[int]
    LabelId: str = Field(None, min_length=1, max_length=30)
    PalletTypeCode: str = Field(None, min_length=1, max_length=30)
    PalletTypeName: str = Field(None, min_length=1, max_length=30)
    NumberOfItems: float
    Length: Optional[float]
    Width: Optional[float]
    Height: Optional[float]
    Volume: Optional[float]
    Weight: Optional[float]
    IsReturnType: bool
    LoadMeters: Optional[float]
    ParentPalletItemId: Optional[float]


class OrderPalletItems(BaseModel):
    OrderPalletItemInfo: List[OrderPalletItemInfo]


class OrderShipmentInfo(BaseModel):
    ShipmentId: int
    WayBill: str = Field(None, min_length=1, max_length=50)
    StatusId: int


class OrderShipments(BaseModel):
    OrderShipmentInfo: List[OrderShipmentInfo]


class GetOrderByOrderNumberResponse(BaseModel):
    Consignee: Consignee
    GoodsInfo: GoodsInfo
    OrderInfo: OrderInfo
    WarehouseInfo: Optional[WarehouseInfo]
    OrderCurrentShipmentInfo: Optional[OrderCurrentShipmentInfo]
    GoodsItems: Optional[GoodsItems]
    PickedOrderLines: Optional[PickedOrderLines]    
    Transporter: Transporter
    OrderShipments: Optional[OrderShipments]
    # PickedArticleItems: Optional[PickedArticleItems]
    # OrderPalletItems: Optional[OrderPalletItems]
