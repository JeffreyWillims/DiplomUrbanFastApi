from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import main_menu, catalog_menu
import asyncio
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(main_menu.router)

app.include_router(catalog_menu.router)

if __name__ == "__main__":
    asyncio.run(uvicorn.run(app, host="127.0.0.1", port=8000, loop="asyncio"))