from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum


class ArticleOperation(str, Enum):
    CreateOrUpdate = 'CreateOrUpdate'

class ArticleIdentification(str, Enum):
    SystemId = 'SystemId'
    ArticleNumber = 'ArticleNumber'
    ProductCode = 'ProductCode'
    ArticleName = 'ArticleName'

class ArticleGroupOperation(str, Enum):
    Find = 'Find'
    FindOrCreate = 'FindOrCreate'
    Clear = 'Clear'
    CreateOrUpdate = 'CreateOrUpdate'

class ArticleGroupIdentification(str, Enum):
    ArticleGroupCode = 'ArticleGroupCode'
    ArticleGroupName = 'ArticleGroupName'

class ArticleGroup(BaseModel):
    ArticleGroupOperation: ArticleGroupOperation
    ArticleGroupIdentification: ArticleGroupIdentification
    ArticleGroupName: str = Field('', min_length=1, max_length=100)

    class Config:  
        use_enum_values = True

class SupplierIdentificationType(str, Enum):
    SupplierNumber = 'SupplierNumber'
    SupplierName = 'SupplierName'
    FullNameAndAdress = 'FullNameAndAdress'

class SupplierOperation(str, Enum):
    CreateOrUpdate = 'CreateOrUpdate'
    Find = 'Find'
    CreateOrFind = 'CreateOrFind'

# class TypeOperation(str, Enum):
#     CreateOrUpdate = 'CreateOrUpdate'
#     Find = 'Find'
#     FindOrCreate = 'FindOrCreate'

# class TypeIdentification(str, Enum):
#     Code = 'Code'
#     Name = 'Name'

class MainSupplier(BaseModel):
    SupplierIdentificationType: SupplierIdentificationType
    SupplierOperation: SupplierOperation
    SupplierName: str = Field('', min_length=1, max_length=200)

    class Config:  
        use_enum_values = True

class Language(BaseModel):
    LanguageCode: str = Field(..., min_length=1, max_length=50)

class ArticleName(BaseModel):
    Language: Language
    ArticleName: str = Field(..., min_length=1, max_length=200)

class ArticleNames(BaseModel):
    ArticleName: List[ArticleName]

class SubArticle(BaseModel):
    ArticleOperation: str = 'CreateOrUpdate'
    ArticleIdentification: ArticleIdentification
    ArticleNumber: str = Field(None, min_length=1, max_length=100)
    ArticleName: str = Field(None, min_length=1, max_length=200)
    BarCode: Optional[str] = None
    ArticleDescription: Optional[str] = None
    SupplierArticleNumber: Optional[str] = None
    ArticleUnitCode: str = Field(None, min_length=1, max_length=50)
    CountryOfOriginCode:  str = Field(None, min_length=1, max_length=2)
    StatisticsNumber: str = Field(None, min_length=1, max_length=100)
    NetWeight: float
    QuantityPerPallet: int
    QuantityPerPackage: int
    IsStockArticle: bool
    ArticleGroup: Optional[ArticleGroup]
    MainSupplier: Optional[MainSupplier]
    Price: float
    ArticleNames: Optional[ArticleNames]

    class Config:  
        use_enum_values = True

class StructureArticleDefinition(BaseModel):
    NumberOfItems: float 
    SubArticleDefinition: SubArticle

class StorageClass(BaseModel):
    Name: str = Field(None, min_length=1, max_length=100)

class ArticleStructureType(str, Enum):
    StructureArticle = 'StructureArticle'
    ProductionArticle = 'ProductionArticle'

class ArticleStructureSpecification(BaseModel):
    ArticleStructureType: ArticleStructureType
    StructureArticleDefinition: Optional[List[StructureArticleDefinition]]
    
    class Config:  
        use_enum_values = True

# class ArticleCategory(BaseModel):
#     TypeOperation: TypeOperation
#     TypeIdentification: TypeIdentification
#     Name: str = Field(..., min_length=1, max_length=200)  # ... means required

#     class Config:  
#         use_enum_values = True

class Article(BaseModel):
    ArticleOperation: ArticleOperation
    ArticleIdentification: ArticleIdentification
    ArticleNumber: str = Field(None, min_length=1, max_length=100)
    ArticleName: str = Field(None, min_length=1, max_length=200)
    BarCode: Optional[str] = Field(None, max_length=100)
    ArticleDescription: Optional[str] = None
    SupplierArticleNumber: Optional[str] = Field(None, min_length=1, max_length=200)
    ArticleUnitCode: str = Field(None, min_length=1, max_length=50)
    CountryOfOriginCode: str = Field(None, min_length=1, max_length=2)
    StatisticsNumber: str = Field(None, min_length=1, max_length=100)
    NetWeight: Optional[float]
    QuantityPerPallet: Optional[int]
    QuantityPerPackage: Optional[int]
    IsStockArticle: bool
    ArticleGroup: Optional[ArticleGroup]
    ArticleStructureSpecification: Optional[ArticleStructureSpecification]
    MainSupplier: Optional[MainSupplier]
    IsObsolete: bool = False
    SubQuantityPerItem: Optional[float]
    StorageClass: Optional[StorageClass]
    Price: float
    # ArticleCategory: ArticleCategory
    ArticleNames: Optional[ArticleNames]

    class Config:  
        use_enum_values = True
