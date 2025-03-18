from sqlalchemy.orm import DeclarativeBase
from typing import Annotated
from sqlalchemy.orm import mapped_column


int_primary_key = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]

class Base(DeclarativeBase):
    pass
