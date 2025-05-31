from fastapi import FastAPI, Depends
from app.routes import (
    producao_router,
    processamento_router,
    comercializacao_router,
    importacao_router,
    exportacao_router,
)
from app.utils.auth import verificar_credenciais
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException

app = FastAPI(title="API VITNI Embrapa")

# 🔐 Aplica autenticação simples em todas as rotas dos módulos
app.include_router(producao_router, dependencies=[Depends(verificar_credenciais)])
app.include_router(processamento_router, dependencies=[Depends(verificar_credenciais)])
app.include_router(comercializacao_router, dependencies=[Depends(verificar_credenciais)])
app.include_router(importacao_router, dependencies=[Depends(verificar_credenciais)])
app.include_router(exportacao_router, dependencies=[Depends(verificar_credenciais)])


# 🔓 Rota pública
@app.get("/")
def root():
    return {"message": "API do VITNI Embrapa está online!"}
