from bs4 import BeautifulSoup
import requests

url = "https://comunicaapi.pje.jus.br/api/v1/comunicacao"

response = requests.get(url, params={
    "pagina": 1,
    "itensPorPagina": 1,
    # seus filtros aqui (OAB, tribunal, data...)
})

item = response.json()["items"][0]


def limpar_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text("\n", strip=True)


processo = {
    "numero_processo": item["numeroprocessocommascara"],
    "tipo_comunicacao": item["tipoComunicacao"],
    "tribunal": item["siglaTribunal"],
    "orgao": item["nomeOrgao"],
    "classe": item["nomeClasse"],
    "data_disponibilizacao": item["datadisponibilizacao"],
    "advogados": [
        {
            "nome": adv["advogado"]["nome"],
            "oab": f'{adv["advogado"]["uf_oab"]}{adv["advogado"]["numero_oab"]}'
        }
        for adv in item["destinatarioadvogados"]
    ],
    "texto": limpar_html(item["texto"]),
    "link_documento": item["link"],
}
