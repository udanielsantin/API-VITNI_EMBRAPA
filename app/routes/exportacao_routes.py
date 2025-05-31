from fastapi import APIRouter, Query
from app.scraper.exportacao.exportacao_espumantes import scrape_exportacao_espumantes
from app.scraper.exportacao.exportacao_suco_de_uva import scrape_exportacao_suco_de_uva
from app.scraper.exportacao.exportacao_uvas_frescas import scrape_exportacao_uvas_frescas
from app.scraper.exportacao.exportacao_vinhos_de_mesa import scrape_exportacao_vinhos_de_mesa

router = APIRouter(prefix="/scrape/exportacao", tags=["Exportacao"])

@router.get("/espumantes")
def espumantes(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_exportacao_espumantes(ano)}

@router.get("/suco_de_uva")
def suco(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_exportacao_suco_de_uva(ano)}

@router.get("/uvas_frescas")
def uvas_frescas(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_exportacao_uvas_frescas(ano)}

@router.get("/vinhos_de_mesa")
def vinhos(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_exportacao_vinhos_de_mesa(ano)}
