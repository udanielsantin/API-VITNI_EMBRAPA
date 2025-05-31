from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()

FAKE_USER = "daniel"
FAKE_PASS = "1234"

def verificar_credenciais(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != FAKE_USER or credentials.password != FAKE_PASS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
