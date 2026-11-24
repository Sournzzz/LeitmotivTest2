from pydantic import BaseModel 
from datetime import date

class Author(BaseModel):
    name : str 
    last_name : str 

class Book(BaseModel): 
    title : str
    genre: str
    publishing_date : date
    