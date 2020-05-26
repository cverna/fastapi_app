import aiofiles

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class DnfTransaction(BaseModel):
    id: int
    command: str
    date: str


async def read_history():
    transactions = []
    async with aiofiles.open("history.txt") as f:
        async for line in f:
            transactions.append(DnfTransaction(
                id=line.split("|")[0].strip(" "),
                command=line.split("|")[1].strip(" "),
                date=line.split("|")[2].strip(" ")
            ))
    return transactions


@app.get("/")
async def read_root():
    return await read_history()
