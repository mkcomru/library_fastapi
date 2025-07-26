from sqlalchemy.orm import DeclarativeBase, mapped_column
from typing import Annotated


int_primary_key = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]

class Base(DeclarativeBase):
    pass



