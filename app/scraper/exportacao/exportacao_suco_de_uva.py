# web scraping for the export data from the website of EMBRAPA vitibrasil Produção
import requests
from bs4 import BeautifulSoup
from pprint import pprint


def scrape_exportacao_suco_de_uva(ano):
    # URL base
    base_url = (
        "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_06"
    )

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

    for linha in tabela.find_all("tr"):
        # Ignora se estiver dentro de um <tfoot> ou se tiver a classe 'tb_total'
        if linha.find_parent("tfoot") or "tb_total" in linha.get("class", []):
            continue

        colunas = linha.find_all("td")
        if len(colunas) != 3:
            continue

        pais = colunas[0].text.strip()
        quantidade = colunas[1].text.strip().replace(".", "").replace(",", ".")
        valor = colunas[2].text.strip().replace(".", "").replace(",", ".")

        quantidade = None if quantidade == "-" else quantidade
        valor = None if valor == "-" else valor

        dados.append(
            {
                "ano": ano,
                "pais": pais,
                "quantidade_kg": float(quantidade) if quantidade else None,
                "valor_usd": float(valor) if valor else None,
            }
        )

    return dados


if __name__ == "__main__":
    ano = 2024  # Ano para filtrar
    resultados = scrape_exportacao_suco_de_uva(ano)
    pprint(resultados)  # Exibe os dados com o ano
