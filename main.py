from fastapi import FastAPI, Query
from typing import Annotated 

app = FastAPI()

@app.get("/books")
async def get_books(
    q: Annotated[
        str, Query(min_length = 5, max_length = 50)
        ]
):
    pass 

