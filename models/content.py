from sqlalchemy import Column , String , Integer 
from .databse import Base
from pydantic import BaseModel

class PostModel (Base):
    __tablename__ = 'app_crud'
    id = Column(Integer , primary_key = True )
    title = Column(String  ,nullable = False )
    content = Column(String, nullable = False )

class PostSchema (BaseModel):
    title : str
    content : str 
    

