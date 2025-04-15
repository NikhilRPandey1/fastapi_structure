from fastapi import  FastAPI
from api.accounts.router import account
from db.session import engine
from db.base import Base


app = FastAPI(debug=True, title="Fast API Structure")

app.include_router(account, prefix="/api")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)