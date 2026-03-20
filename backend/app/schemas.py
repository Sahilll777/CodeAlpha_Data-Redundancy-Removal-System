from pydantic import BaseModel

class DataSchema(BaseModel):
    user_id: str
    email: str
    content: str