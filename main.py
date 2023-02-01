from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from router import router
from sources import db


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await db.setup()


@app.on_event("shutdown")
async def shutdown_event():
    await db.release()


app.include_router(router)
# app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", log_level="info")
