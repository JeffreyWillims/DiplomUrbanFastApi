from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader

router = APIRouter()

env = Environment(loader=FileSystemLoader('templates'))


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