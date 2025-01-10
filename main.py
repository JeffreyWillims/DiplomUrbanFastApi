from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import main_menu, catalog_menu
import asyncio
import uvicorn

app = FastAPI()  # Создание приложения FastAPI. Этот код создает экземпляр приложения FastAPI.
                # Это основной объект, который будет обрабатывать все запросы к вашему API.

app.mount("/static", StaticFiles(directory="static"), name="static")  # Подключение статических файлов
                                #Эта строка подключает директорию для хранения статических файлов (например, изображений,
                                # CSS-файлов, JavaScript). Все файлы, находящиеся в папке static, будут доступны через URL /static/....

app.include_router(main_menu.router) # Подключение роутов

app.include_router(catalog_menu.router)

""" Эти строки добавляют маршруты (routes) из других модулей (main_menu и catalog_menu), чтобы они стали частью основного приложения. 
Маршруты определяют, какие функции будут вызываться при обращении к определенным URL-адресам."""


if __name__ == "__main__":
    asyncio.run(uvicorn.run(app, host="127.0.0.1", port=8000, loop="asyncio"))

""" 
Эта часть кода запускает сервер Uvicorn, который будет обслуживать ваше приложение FastAPI. Сервер слушает порт 8000 на локальном хосте (127.0.0.1),
используя асинхронный цикл событий (loop="asyncio").
Таким образом, весь этот код создает простое веб-приложение на основе FastAPI, которое может служить основой для разработки RESTful API.
"""