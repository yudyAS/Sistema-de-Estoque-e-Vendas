from estoque import produtos, busca_binaria, ler_inteiro, ler_float, ler_texto

def editar_produto():

    codigo = ler_inteiro("Digite o código do produto: ", min_value=1)

    indice = busca_binaria(produtos, codigo)

    if indice != -1:

        print("Produto encontrado!")

        novo_nome = ler_texto("Novo nome: ")
        nova_categoria = ler_texto("Nova categoria: ")
        novo_preco = ler_float("Novo preço: ", min_value=0.01)
        nova_qtd = ler_inteiro("Nova quantidade: ", min_value=0)

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

    codigo = ler_inteiro("Digite o código do produto que deseja remover: ", min_value=1)

    indice = busca_binaria(produtos, codigo)

    if indice != -1:
        produto_removido = produtos.pop(indice)
        print(f"Produto {produto_removido['nome']} removido com sucesso!")
    else:
        print("Produto não encontrado.")

#Registrar venda (reduz estoque, valida quantidade)
def registrar_venda():

    codigo = ler_inteiro("Digite o código do produto: ", min_value=1)

    indice = busca_binaria(produtos, codigo)

    if indice == -1:
        print("Produto não encontrado.")
        return

    quantidade_venda = ler_inteiro("Digite a quantidade vendida: ", min_value=1)

    if quantidade_venda > produtos[indice]["qtd"]:
        print("Estoque insuficiente.")
        return

    produtos[indice]["qtd"] -= quantidade_venda

    print("Venda registrada com sucesso!")
    print(f"Estoque restante: {produtos[indice]['qtd']}")

#Relatorio de estoque baixo (quantidade < limite configuravel)
def relatorio_estoque_baixo():

    limite = ler_inteiro("Digite o limite mínimo de estoque: ", min_value=0)

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

    categoria = ler_texto("Digite a categoria do produto: ")
    encontrou = False
    for produto in produtos:
        if produto['catg'].lower() == categoria.lower():
            encontrou = True
            print("-----------------------------")
            print(f"Código: {produto['codigo']}\nNome: {produto['nome']}\n"
                f"Categoria: {produto['catg']}\nPreço: {produto['preco']}\n"
                f"Quantidade: {produto['qtd']}")

    if not encontrou:
        print("Nenhum produto encontrado na categoria especificada")
