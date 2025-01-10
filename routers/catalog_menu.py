from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader

router = APIRouter()

env = Environment(loader=FileSystemLoader('templates'))
"""
Здесь создается маршрутизатор APIRouter() для определения маршрутов вашего API, 
а также инициализируется окружение Jinja2 для работы с шаблонами HTML, хранящимися в директории templates.
"""

@router.get("/catalog/iphone")
def read_architecture(request: Request):
    template = env.get_template('iphone.html')
    return HTMLResponse(content=template.render(request=request), status_code=200)


@router.get("/catalog/ipad")
def read_improvement(request: Request):
    template = env.get_template('ipad.html')
    return HTMLResponse(content=template.render(request=request), status_code=200)


@router.get("/catalog/macbook")
def read_commercial_interiors(request: Request):
    template = env.get_template('macbook.html')
    return HTMLResponse(content=template.render(request=request), status_code=200)


@router.get("/catalog/watch")
def read_residential_interiors(request: Request):
    template = env.get_template('watch.html')
    return HTMLResponse(content=template.render(request=request), status_code=200)

"""
Каждый из этих маршрутов представляет собой отдельный эндпоинт, который возвращает определенный HTML-шаблон
Когда пользователь отправляет GET-запрос на путь /catalog/iphone, функция read_architecture загружает шаблон iphone.html 
из директории templates, рендерит его с использованием данных из запроса и возвращает ответ в виде HTML-кода со статусом 200 
(успешная обработка).

В целом, этот код определяет несколько маршрутов для каталога товаров (iPhone, iPad, MacBook, Watch), 
каждый из которых возвращает соответствующий HTML-шаблон. Эти маршруты могут быть добавлены в основное приложение
 FastAPI с помощью метода include_router(), как было показано в предыдущем примере.

"""