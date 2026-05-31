import json
import os
import time

from estoque import produtos

# Caminho padrão do arquivo de dados JSON.
CAMINHO_PADRAO = os.path.join(os.path.dirname(__file__), "dados.json")


def salvar_dados(caminho: str = CAMINHO_PADRAO) -> None:
    """Salva a lista de produtos em um arquivo JSON.

    O JSON preserva a estrutura de dicionário de cada produto e facilita
    a leitura/escrita com o Python sem precisar mapear colunas manualmente.
    """
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, indent=2, ensure_ascii=False)
    print(f"Dados salvos em: {caminho}")


def carregar_dados(caminho: str = CAMINHO_PADRAO) -> None:
    """Carrega produtos de um arquivo JSON para o vetor de produtos.

    O vetor é ordenado por código após o carregamento para manter a
    validade da busca binária usada em estoque.py.
    """
    if not os.path.isfile(caminho):
        print(f"Arquivo não encontrado: {caminho}")
        return

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except (json.JSONDecodeError, OSError) as erro:
        print(f"Erro ao carregar o arquivo: {erro}")
        return

    if not isinstance(dados, list):
        print("Formato do arquivo inválido: esperado uma lista de produtos.")
        return

    produtos.clear()
    produtos.extend(sorted(dados, key=lambda produto: produto.get("codigo", 0)))
    print(f"Dados carregados com sucesso de: {caminho}")
    time.sleep(2)
 