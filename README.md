# API-VITNI_EMBRAPA

API desenvolvida com **FastAPI** para atender ao projeto VITNI da EMBRAPA. Esta API serve como backend para fornecer dados e processamentos específicos relacionados à área de pesquisa do projeto.

## 🚀 Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- Uvicorn (servidor ASGI)
- Python 3.x
- [BeutifulSoup, Pandas]

## Fluxograma da Arquitetura da API

![Fluxograma da API](docs/fluxo_arquitetura.png)

## 📁 Estrutura do Projeto

API-VITNI_EMBRAPA/  
├── app/  
│   ├── routes/           # Rotas da API organizadas por domínio(FastAPI)  
│   │   ├── comercializacao_routes.py  
│   │   ├── exportacao_routes.py  
│   │   ├── importacao_routes.py  
│   │   ├── processamento_routes.py  
│   │   └── producao_routes.py  
│   ├── scraper/               # Módulos de raspagem de dados  
│   │   ├── exportacao/  
│   │   ├── importacao/  
│   │   ├── processamento/  
│   │   ├── comercializacao.py  
│   │   └── producao.py  
│   ├── utils/                 # Utilitários e autenticação  
│   │   ├── auth.py  
│   │   ├── models.py  
│   │   └── security.py  
│   └── main.py                # Ponto de entrada da aplicação  
├── docs/                      # Documentação adicional (ex: OpenAPI, exemplos)  
├── venv/                      # Ambiente virtual  
├── requirements.txt           # Dependências do projeto  
├── .gitignore  
└── README.md  



## 🧭 Fluxo de Funcionamento

[Cliente] --> [Requisição HTTP] --> [FastAPI Router]
|
v
[Função Endpoint / Rota Específica]
|
v
[Processamento]
|
v
[Resposta JSON (status + dados)]
|
v
[Cliente]

## 🧪 Documentação Interativa

Swagger UI: https://api-vitni-embrapa.onrender.com/docs

## 🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests com melhorias, sugestões ou correções.

## ⚙️ Instalação 

1. Clone o repositório:

```bash
git clone https://github.com/udanielsantin/API-VITNI_EMBRAPA.git
cd API-VITNI_EMBRAPA
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## ▶️ Execução
Inicie o servidor com Uvicorn:

```bash
uvicorn app.main:app --reload
```

