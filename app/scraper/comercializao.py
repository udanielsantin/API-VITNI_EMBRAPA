# web scraping for the export data from the website of EMBRAPA vitibrasil Produção
import requests
from bs4 import BeautifulSoup
from pprint import pprint


def scrape_comercializacao(ano):
    # URL base
    base_url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04"

    # Parâmetro do ano na URL
    params = {"ano": ano}  # Inclui o ano como parâmetro

    # Fazendo a requisição GET com o ano
    response = requests.get(base_url, params=params)
    response.raise_for_status()  # Para verificar se a requisição foi bem-sucedida

    # Usando BeautifulSoup para processar o HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Encontrando a tabela com os dados
    tabela = soup.find("table", {"class": "tb_base tb_dados"})

    dados = []
    grupo_produto = None
    linhas = tabela.find_all("tr")
    total_linhas = len(linhas)
    i = 0

    while i < total_linhas:
        linha = linhas[i]
        colunas = linha.find_all("td")

        if not colunas:
            i += 1
            continue

        td_class = colunas[0].get("class", [])

        # Caso seja um grupo de produto (tb_item)
        if "tb_item" in td_class:
            grupo_produto = colunas[0].text.strip().title()

            # Verifica se a próxima linha também é tb_item (para capturar como produto)
            if i + 1 < total_linhas:
                prox_linha = linhas[i + 1]
                prox_colunas = prox_linha.find_all("td")
                prox_classes = prox_colunas[0].get("class", []) if prox_colunas else []

                if "tb_item" in prox_classes:
                    quantidade = colunas[1].text.strip() if len(colunas) > 1 else ""
                    dados.append(
                        {
                            "ano": ano,
                            "grupo_produto": grupo_produto,
                            "produto": grupo_produto,
                            "quantidade_kg": quantidade,
                        }
                    )
            i += 1
            continue

        # Linhas com produtos (tb_subitem)
        if "tb_subitem" in td_class and grupo_produto:
            produto = colunas[0].text.strip()
            quantidade = colunas[1].text.strip() if len(colunas) > 1 else ""

            if produto and "total" not in produto.lower():
                dados.append(
                    {
                        "ano": ano,
                        "grupo_produto": grupo_produto,
                        "produto": produto,
                        "quantidade_kg": quantidade,
                    }
                )

        i += 1

    return dados


if __name__ == "__main__":
    ano = 2023  # Ano para filtrar
    resultados = scrape_comercializacao(ano)
    pprint(resultados)  # Exibe os dados com o ano
