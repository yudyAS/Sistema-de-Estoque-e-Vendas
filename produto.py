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

#Registrar venda (reduz estoque, valida quantidade)

#Relatorio de estoque baixo (quantidade < limite configuravel)

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