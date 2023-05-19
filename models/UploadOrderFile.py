from pydantic import BaseModel


class UploadOrderFile(BaseModel):
    order_number: str
    file_path: str
