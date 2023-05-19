from pydantic import BaseModel


class WriteData(BaseModel):
    ProcesType: str = None
    foretagkod: str = "1210"
    Text6: str = "XML OK"
    Text7: str = ''
    ExecuteProcedure: str = 'Y'
    Message: str = ''
    EI: str = None