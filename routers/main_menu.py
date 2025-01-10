from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from jinja2 import Template, Environment, FileSystemLoader

router = APIRouter()

env = Environment(loader=FileSystemLoader('templates'))

"""
Здесь мы создаем маршрутизатор APIRouter() для определения маршрутов нашего API и 
настраиваем окружение Jinja2 для работы с шаблонами HTML, находящимися в директории templates.
"""

@router.get("/")
def read_home_page():
    with open("templates/home_page.html", "r", encoding="utf-8") as f:
        template = Template(f.read())
    return HTMLResponse(content=template.render(request={"path": "/"}), status_code=200)


@router.get("/catalog")
def catalog(request: Request):
    template = env.get_template('catalog.html')
    return HTMLResponse(content=template.render(request=request), status_code=200)


@router.get("/contacts")
def read_contacts():
    with open("templates/contacts.html", "r", encoding="utf-8") as f:
        template = Template(f.read())
    return HTMLResponse(content=template.render(request={"path": "/contacts"}), status_code=200)


@router.get("/warranty")
def read_services(request: Request):
    template = env.get_template('warranty.html')
    return HTMLResponse(content=template.render(request=request), status_code=200)

"""
. Функция открывает файл home_page.html из директории templates, считывает его содержимое и преобразует в шаблон Jinja2. 
Затем она рендерит этот шаблон с параметром "path": "/" и возвращает результат в виде HTML-ответа с кодом состояния 200 (успех).

Этот код определяет несколько маршрутов для веб-приложения: главная страница, каталог товаров, контакты и гарантия.
 Каждый маршрут рендерит соответствующий HTML-шаблон и возвращает его клиенту.
"""