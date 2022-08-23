from pydantic import BaseModel


class PayloadModel(BaseModel):
    bucket_name: str
    directory: str
