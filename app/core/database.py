from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine 
from app.core.config import settings


library_engine = create_engine(settings.LIBRARY_DB_URL)

session = sessionmaker(bind=library_engine)






