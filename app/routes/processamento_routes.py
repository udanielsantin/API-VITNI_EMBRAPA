from fastapi import APIRouter, Query
from app.scraper.processamento.processamento_americanas_hibridas import scrape_processamento_americanas_hibridas
from app.scraper.processamento.processamento_sem_classificacao import scrape_processamento_sem_classificacao
from app.scraper.processamento.processamento_uvas_de_mesa import scrape_processamento_uvas_de_mesa
from app.scraper.processamento.processamento_viniferas import scrape_processamento_viniferas

router = APIRouter(prefix="/scrape/processamento", tags=["Processamento"])

@router.get("/americanas_hibridas")
def americanas_hibridas(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_processamento_americanas_hibridas(ano)}

@router.get("/sem_classificacao")
def sem_classificacao(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_processamento_sem_classificacao(ano)}

@router.get("/uvas_de_mesa")
def uvas_de_mesa(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_processamento_uvas_de_mesa(ano)}

@router.get("/viniferas")
def viniferas(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_processamento_viniferas(ano)}
