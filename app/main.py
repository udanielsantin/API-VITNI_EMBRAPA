from fastapi import FastAPI, Query

# Produção
from app.scraper.producao import scrape_producao

# Processamento
from app.scraper.processamento_americanas_hibridas import (
    scrape_processamento_americanas_hibridas,
)
from app.scraper.processamento_sem_classificacao import (
    scrape_processamento_sem_classificacao,
)
from app.scraper.processamento_uvas_de_mesa import scrape_processamento_uvas_de_mesa
from app.scraper.processamento_viniferas import scrape_processamento_viniferas

# Comercialização
from app.scraper.comercializao import scrape_comercializacao

# Importação
from app.scraper.importacao_espumantes import scrape_importacao_espumantes
from app.scraper.importacao_suco_de_uva import scrape_importacao_suco_de_uva
from app.scraper.importacao_uvas_frescas import scrape_importacao_uvas_frescas
from app.scraper.importacao_uvas_passas import scrape_importacao_uvas_passas
from app.scraper.importacao_vinhos_de_mesa import scrape_importacao_vinhos_de_mesa

# Exportação
from app.scraper.exportacao_espumantes import scrape_exportacao_espumantes
from app.scraper.exportacao_suco_de_uva import scrape_exportacao_suco_de_uva
from app.scraper.exportacao_uvas_frescas import scrape_exportacao_uvas_frescas
from app.scraper.exportacao_vinhos_de_mesa import scrape_exportacao_vinhos_de_mesa

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "API do VITNI Embrapa está online!"}


# Produção
@app.get("/scrape/producao")
def get_scraped_producao(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_producao(ano)}


# Processamento
@app.get("/scrape/processamento/americanas_hibridas")
def get_scraped_americanas_hibridas(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_processamento_americanas_hibridas(ano)}


@app.get("/scrape/processamento/sem_classificacao")
def get_scraped_sem_classificacao(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_processamento_sem_classificacao(ano)}


@app.get("/scrape/processamento/uvas_de_mesa")
def get_scraped_uvas_de_mesa(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_processamento_uvas_de_mesa(ano)}


@app.get("/scrape/processamento/viniferas")
def get_scraped_viniferas(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_processamento_viniferas(ano)}


# Comercialização
@app.get("/scrape/comercializacao")
def get_scraped_comercializacao(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_comercializacao(ano)}


# Importação
@app.get("/scrape/importacao/espumantes")
def get_scraped_importacao_espumantes(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_importacao_espumantes(ano)}


@app.get("/scrape/importacao/suco_de_uva")
def get_scraped_importacao_suco(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_importacao_suco_de_uva(ano)}


@app.get("/scrape/importacao/uvas_frescas")
def get_scraped_importacao_uvas_frescas(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_importacao_uvas_frescas(ano)}


@app.get("/scrape/importacao/uvas_passas")
def get_scraped_importacao_uvas_passas(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_importacao_uvas_passas(ano)}


@app.get("/scrape/importacao/vinhos_de_mesa")
def get_scraped_importacao_vinhos_de_mesa(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_importacao_vinhos_de_mesa(ano)}


# Exportação
@app.get("/scrape/exportacao/espumantes")
def get_scraped_exportacao_espumantes(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_exportacao_espumantes(ano)}


@app.get("/scrape/exportacao/suco_de_uva")
def get_scraped_exportacao_suco(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_exportacao_suco_de_uva(ano)}


@app.get("/scrape/exportacao/uvas_frescas")
def get_scraped_exportacao_uvas_frescas(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_exportacao_uvas_frescas(ano)}


@app.get("/scrape/exportacao/vinhos_de_mesa")
def get_scraped_exportacao_vinhos_de_mesa(ano: int = Query(...)):
    return {"status": "ok", "dados": scrape_exportacao_vinhos_de_mesa(ano)}
