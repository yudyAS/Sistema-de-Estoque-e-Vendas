# Inserir Produtos
produtos = []

# Cadastro de produtos
def cadastrar_produto():
    cod = int(input("Digite o código do produto: "))
    nome = input("Digite o nome do produto: ")
    catg = input("Digite a categoria do produto: ")
    preco = float(input("Digite o preço (R$): "))
    qtd = int(input("Digite a quantidade: "))

    inserir_ordenado({"codigo": cod, "nome": nome, "catg": catg, "preco": preco, "qtd": qtd})

# Metodo de inserção ordenada, que insere o produto na lista e depois ordena a lista pelo código do produto.
def inserir_ordenado(produto):
    produtos.append(produto)
    produtos.sort(key=lambda x: x["cod"])
    print("Produto cadastrado com sucesso!")
    for produto in produtos:
        print(f"Código: {produto['codigo']}\nNome: {produto['nome']}\n"
            f"Categoria: {produto['catg']}\nPreço: {produto['preco']}\n"
            f"Quantidade: {produto['qtd']}")

# Buscar Produtos
# Vai bucar o produto utilizando o método de busca binária, que é mais eficiente para listas ordenadas.
def buscar_codigo():
    cod = int(input("Digite o código do produto: "))
    indice = busca_binaria(produtos, cod)

    if indice != -1:
        produto = produtos[indice]
        print(f"Código: {produto['codigo']}\nNome: {produto['nome']}\n"
            f"Categoria: {produto['catg']}\nPreço: {produto['preco']}\n"
            f"Quantidade: {produto['qtd']}")
    else:
        print("Produto não encontrado.")

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
    nome = input("Digite o nome do produto: ")
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            print(f"Código: {produto['codigo']}\nNome: {produto['nome']}\n"
                f"Categoria: {produto['catg']}\nPreço: {produto['preco']}\n"
                f"Quantidade: {produto['qtd']}")
        else:
            print("Produto não encontrado.")

def listar_produtos_codigo():
    for produto in produtos:
        print(f"Código: {produto['codigo']}\nNome: {produto['nome']}\n"
            f"Categoria: {produto['catg']}\nPreço: {produto['preco']}\n"
            f"Quantidade: {produto['qtd']}")

def listar_produtos_categoria():
    categoria = input("Digite a categoria do produto: ")
    encontrou = False
    for produto in produtos:
        if produto['catg'] == categoria:
            encontrou = True
            print(f"Código: {produto['codigo']}\nNome: {produto['nome']}\n"
                f"Categoria: {produto['catg']}\nPreço: {produto['preco']}\n"
                f"Quantidade: {produto['qtd']}")

    if not encontrou:
        print("Nenhum produto encontrado na categoria especificada")

while True:

    print("---------- MENU ---------")
    print("1 - Cadastrar Produto") #feito
    print("2 - Editar produto")
    print("3 - Remover produto")
    print("4 - Buscar produto por código")#feito
    print("5 - Buscar produto por nome")#feito
    print("6 - Registrar venda (reduz estoque, valida quantidade)") 
    print("7 - Listar produtos por código")#feito
    print("8 - Listar produtos por categoria")#feito
    print("9 - Relatório de estoque baixo (quantidade < limite configurável)")
    print("10 - Salvar e carregar dados em arquivo (CSV ou JSON)")
    print("0 - Sair")

    menu = int(input("Escolha a opção: "))

    match menu:
        case 1: 
            cadastrar_produto()
        case 2:
            print("cadastrar()")
        case 3:
            print("cadastrar()")
        case 4:
            buscar_codigo()
        case 5:
            buscar_nome()
        case 6:
            listar_produtos_codigo()
        case 7:
            listar_produtos_categoria()
        case 8:
            print("cadastrar()")
        case 9:
            print("cadastrar()")
        case 10:
            print("cadastrar()")
        case 0:
            print("Saindo")
            break