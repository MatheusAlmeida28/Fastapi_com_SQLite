from pydantic import BaseModel
from typing import Optional

class Gameschemas(BaseModel):
    id:Optional[int] = None
    name:Optional[str] = None
    multiplatform:Optional[bool] = None
    price:Optional[float] = None
    for_sale:Optional[bool] = None

    class config:
        orm_mode=True