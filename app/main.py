from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from app.routes import router

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

import json
templates.env.filters["tojson"] = lambda value: json.dumps(value)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(router)
