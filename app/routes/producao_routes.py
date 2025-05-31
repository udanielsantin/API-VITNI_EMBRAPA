from fastapi import APIRouter, Query
from app.scraper.producao import scrape_producao

router = APIRouter(prefix="/scrape/producao", tags=["Producao"])

@router.get("")
def get_scraped_producao(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_producao(ano)}
