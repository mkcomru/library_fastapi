from pydantic import BaseModel
import enum


class Genre(str, enum.Enum):
    fantasy = "fantasy"
    science_fiction = "science_fiction"
    mystery = "mystery"
    romance = "romance"
    horror = "horror"
    thriller = "thriller"
    biography = "biography"
    autobiography = "autobiography"


class BookBase(BaseModel):
    title: str
    year: int
    genre: Genre
    rating: float
    publisher: str
    pages: int
    author_id: int


class BookRead(BookBase):
    id: int

    class Config:
        orm_mode = True















