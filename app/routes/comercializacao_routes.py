from fastapi import APIRouter, Query
from app.scraper.comercializao import scrape_comercializacao

router = APIRouter(prefix="/scrape/comercializacao", tags=["Comercializacao"])

@router.get("")
def comercializacao(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_comercializacao(ano)}
