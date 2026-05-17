from estoque import produtos

#Editar produto (nome, preco, quantidade, categoria)

#Remover produto pelo codigo

#Registrar venda (reduz estoque, valida quantidade)

#Relatorio de estoque baixo (quantidade < limite configuravel)

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