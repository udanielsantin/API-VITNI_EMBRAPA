from fastapi import FastAPI, Depends, HTTPException, status
from app.routes import (
    producao_router,
    processamento_router,
    comercializacao_router,
    importacao_router,
    exportacao_router,
)
from app.utils.auth import get_current_user, authenticate_user, fake_users_db
from app.utils.models import UserCreate, Token
from app.utils.security import get_password_hash, create_access_token
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI(title="API VITNI Embrapa")

# 🔐 Protege com JWT em todas as rotas
app.include_router(producao_router, dependencies=[Depends(get_current_user)])
app.include_router(processamento_router, dependencies=[Depends(get_current_user)])
app.include_router(comercializacao_router, dependencies=[Depends(get_current_user)])
app.include_router(importacao_router, dependencies=[Depends(get_current_user)])
app.include_router(exportacao_router, dependencies=[Depends(get_current_user)])

# 🔓 Rota pública
@app.get("/")
def root():
    return {"message": "API do VITNI Embrapa está online!"}

# 🔓 Registro
@app.post("/register")
def register(user: UserCreate):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Usuário já existe")
    fake_users_db[user.username] = {
        "username": user.username,
        "hashed_password": get_password_hash(user.password)
    }
    return {"msg": "Usuário criado com sucesso"}

# 🔓 Login/token
@app.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}
