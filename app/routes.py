from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services import run_pareto_analysis

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/analyze", response_class=HTMLResponse)
async def analyze(request: Request, owner: str = Form(...), repo: str = Form(...), token: str = Form(...)):
    summary = run_pareto_analysis(owner, repo, token)

    files_json        = summary["files"]
    contributors_json = summary["contributors"]

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "files": files_json,
            "contributors": contributors_json,
            "charts": ["file_changes_pareto.png", "contributor_activity_pareto.png"],
        },
    )


