from fastapi import APIRouter, Query
from app.scraper.importacao.importacao_espumantes import scrape_importacao_espumantes
from app.scraper.importacao.importacao_suco_de_uva import scrape_importacao_suco_de_uva
from app.scraper.importacao.importacao_uvas_frescas import scrape_importacao_uvas_frescas
from app.scraper.importacao.importacao_uvas_passas import scrape_importacao_uvas_passas
from app.scraper.importacao.importacao_vinhos_de_mesa import scrape_importacao_vinhos_de_mesa

router = APIRouter(prefix="/scrape/importacao", tags=["Importacao"])

@router.get("/espumantes")
def espumantes(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_importacao_espumantes(ano)}

@router.get("/suco_de_uva")
def suco(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_importacao_suco_de_uva(ano)}

@router.get("/uvas_frescas")
def uvas_frescas(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_importacao_uvas_frescas(ano)}

@router.get("/uvas_passas")
def uvas_passas(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_importacao_uvas_passas(ano)}

@router.get("/vinhos_de_mesa")
def vinhos(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_importacao_vinhos_de_mesa(ano)}
