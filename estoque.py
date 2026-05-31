# Inserir Produtos
import time


def ler_inteiro(prompt, min_value=None, positive_only=False):
    while True:
        valor = input(prompt).strip()
        if not valor:
            print("Entrada vazia. Digite um número inteiro.")
            continue
        try:
            numero = int(valor)
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")
            continue
        if positive_only and numero <= 0:
            print("Digite um número inteiro maior que zero.")
            continue
        if min_value is not None and numero < min_value:
            print(f"Digite um número inteiro maior ou igual a {min_value}.")
            continue
        return numero


def ler_float(prompt, min_value=None, positive_only=False):
    while True:
        valor = input(prompt).strip()
        if not valor:
            print("Entrada vazia. Digite um número.")
            continue
        try:
            numero = float(valor)
        except ValueError:
            print("Valor inválido. Digite um número.")
            continue
        if positive_only and numero <= 0:
            print("Digite um número maior que zero.")
            continue
        if min_value is not None and numero < min_value:
            print(f"Digite um número maior ou igual a {min_value}.")
            continue
        return numero


def ler_texto(prompt):
    while True:
        texto = input(prompt).strip()
        if texto:
            return texto
        print("Entrada vazia. Digite um texto válido.")


def pausar_paginacao(item_num, total, page_size=5):
    if item_num % page_size == 0 and item_num < total:
        resposta = input("Pressione Enter para continuar ou Q para sair... ").strip().lower()
        return resposta != "q"
    return True


produtos = []
produtos_ordenados = []

# Cadastro de produtos
def cadastrar_produto():
    cod = ler_inteiro("Digite o código do produto: ", min_value=1)
    nome = ler_texto("Digite o nome do produto: ")
    catg = ler_texto("Digite a categoria do produto: ")
    preco = ler_float("Digite o preço (R$): ", min_value=0.01)
    qtd = ler_inteiro("Digite a quantidade: ", min_value=0)

    # Validações
    if preco <= 0:
        print("Preço inválido. O preço deve ser maior que zero.")
        time.sleep(2)
        return
    if qtd < 0:
        print("Quantidade inválida. A quantidade não pode ser negativa.")
        time.sleep(2)
        return
    if busca_binaria(produtos_ordenados, cod) != -1:
        print("Código já existe. Por favor, use um código único.")
        time.sleep(2)
        return

    produto = {"codigo": cod, "nome": nome, "catg": catg, "preco": preco, "qtd": qtd}
    produtos.append(produto)
    inserir_ordenado(produto)
    from arquivos import log_operacao
    log_operacao(f"Cadastrar produto: código {cod}, nome {nome}, categoria {catg}, preço {preco}, quantidade {qtd}")

# Metodo de inserção ordenada, que insere o produto na lista ordenada por código.
def inserir_ordenado(produto):
    produtos_ordenados.append(produto)
    produtos_ordenados.sort(key=lambda x: x["codigo"])
    print("Produto cadastrado com sucesso!")
    for produto in produtos:
        print(f"Código: {produto['codigo']}\nNome: {produto['nome']}\n"
            f"Categoria: {produto['catg']}\nPreço: {produto['preco']}\n"
            f"Quantidade: {produto['qtd']}")

# Buscar Produtos
# Vai bucar o produto utilizando o método de busca binária, que é mais eficiente para listas ordenadas.
def buscar_codigo():
    from arquivos import log_operacao

    cod = ler_inteiro("Digite o código do produto: ", min_value=1)
    indice = busca_binaria(produtos_ordenados, cod)

    if indice != -1:
        produto = produtos_ordenados[indice]
        print(f"Código: {produto['codigo']}\nNome: {produto['nome']}\n"
            f"Categoria: {produto['catg']}\nPreço: {produto['preco']}\n"
            f"Quantidade: {produto['qtd']}")
        log_operacao(f"Buscar produto por código: código {cod}, encontrado")
    else:
        print("Produto não encontrado.")
        log_operacao(f"Buscar produto por código: código {cod}, não encontrado")

# Método de busca que divide a lista em partes para encontrar o produto mais rapidadamente.
def busca_binaria(lista, codigo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio]["codigo"] == codigo:
            return meio
        elif lista[meio]["codigo"] < codigo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1

def buscar_nome():
    from arquivos import log_operacao

    nome = ler_texto("Digite o nome do produto: ")
    encontrou = False
    
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            encontrou = True
            print(f"Código: {produto['codigo']}\nNome: {produto['nome']}\n"
                f"Categoria: {produto['catg']}\nPreço: {produto['preco']}\n"
                f"Quantidade: {produto['qtd']}")
    
    if not encontrou:
        print("Produto não encontrado.")
        log_operacao(f"Buscar produto por nome: nome {nome}, não encontrado")
    else:
        log_operacao(f"Buscar produto por nome: nome {nome}, encontrado")