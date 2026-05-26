from estoque import produtos, cadastrar_produto, inserir_ordenado, buscar_codigo, buscar_nome, busca_binaria

def editar_produto():

    codigo = int(input("Digite o código do produto: "))

    indice = busca_binaria(produtos, codigo)

    if indice != -1:

        print("Produto encontrado!")

        novo_nome = input("Novo nome: ")
        nova_categoria = input("Nova categoria: ")
        novo_preco = float(input("Novo preço: "))
        nova_qtd = int(input("Nova quantidade: "))

        # validações
        if novo_preco <= 0:
            print("Preço inválido.")
            return

        if nova_qtd < 0:
            print("Quantidade inválida.")
            return

        # Edição do produto
        produtos[indice]["nome"] = novo_nome
        produtos[indice]["catg"] = nova_categoria
        produtos[indice]["preco"] = novo_preco
        produtos[indice]["qtd"] = nova_qtd

        print("Produto editado com sucesso!")

    else:
        print("Produto não encontrado.")

#Remover produto pelo codigo
def remover_produto():

    codigo = int(input("Digite o código do produto que deseja remover: "))

    indice = busca_binaria(produtos, codigo)

    if indice != -1:
        produto_removido = produtos.pop(indice)
        print(f"Produto {produto_removido['nome']} removido com sucesso!")
    else:
        print("Produto não encontrado.")

#Registrar venda (reduz estoque, valida quantidade)
def registrar_venda():

    codigo = int(input("Digite o código do produto: "))

    indice = busca_binaria(produtos, codigo)

    if indice == -1:
        print("Produto não encontrado.")
        return

    quantidade_venda = int(input("Digite a quantidade vendida: "))

    if quantidade_venda <= 0:
        print("Quantidade inválida.")
        return

    if quantidade_venda > produtos[indice]["qtd"]:
        print("Estoque insuficiente.")
        return

    produtos[indice]["qtd"] -= quantidade_venda

    print("Venda registrada com sucesso!")
    print(f"Estoque restante: {produtos[indice]['qtd']}")

#Relatorio de estoque baixo (quantidade < limite configuravel)
def relatorio_estoque_baixo():

    limite = int(input("Digite o limite mínimo de estoque: "))

    encontrou = False

    print("\n--- RELATÓRIO DE ESTOQUE BAIXO ---")

    for produto in produtos:

        if produto["qtd"] < limite:
            encontrou = True

            print("-----------------------------")
            print(f"Código: {produto['codigo']}")
            print(f"Nome: {produto['nome']}")
            print(f"Categoria: {produto['catg']}")
            print(f"Preço: R$ {produto['preco']}")
            print(f"Quantidade: {produto['qtd']}")

    if not encontrou:
        print("Nenhum produto com estoque baixo.")

def listar_produtos_codigo():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    for produto in produtos:
        print("-----------------------------")
        print(f"Código: {produto['codigo']}\nNome: {produto['nome']}\n"
            f"Categoria: {produto['catg']}\nPreço: {produto['preco']}\n"
            f"Quantidade: {produto['qtd']}")

def listar_produtos_categoria():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    categoria = input("Digite a categoria do produto: ")
    encontrou = False
    for produto in produtos:
        if produto['catg'] == categoria:
            encontrou = True
            print("-----------------------------")
            print(f"Código: {produto['codigo']}\nNome: {produto['nome']}\n"
                f"Categoria: {produto['catg']}\nPreço: {produto['preco']}\n"
                f"Quantidade: {produto['qtd']}")

    if not encontrou:
        print("Nenhum produto encontrado na categoria especificada")