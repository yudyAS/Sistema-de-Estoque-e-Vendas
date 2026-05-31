from arquivos import log_operacao
from estoque import produtos, busca_binaria, ler_inteiro, ler_float, ler_texto, pausar_paginacao


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
        log_operacao(f"Editar produto: código {codigo}, nome {novo_nome}, categoria {nova_categoria}, preço {nova_preco}, quantidade {nova_qtd}")

    else:
        print("Produto não encontrado.")

#Remover produto pelo codigo
def remover_produto():

    codigo = ler_inteiro("Digite o código do produto que deseja remover: ", min_value=1)

    indice = busca_binaria(produtos, codigo)

    if indice != -1:
        produto_removido = produtos.pop(indice)
        print(f"Produto {produto_removido['nome']} removido com sucesso!")
        log_operacao(f"Remover produto: código {codigo}, nome {produto_removido['nome']}")
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
    log_operacao(f"Registrar venda: código {codigo}, quantidade {quantidade_venda}, estoque restante {produtos[indice]['qtd']}")

#Relatorio de estoque baixo (quantidade < limite configuravel)
def relatorio_estoque_baixo():

    limite = ler_inteiro("Digite o limite mínimo de estoque: ", min_value=0)

    produtos_baixo = [produto for produto in produtos if produto["qtd"] < limite]
    encontrou = bool(produtos_baixo)

    print("\n--- RELATÓRIO DE ESTOQUE BAIXO ---")

    if not produtos_baixo:
        print("Nenhum produto com estoque baixo.")
        log_operacao(f"Relatório estoque baixo: limite {limite}, encontrados 0")
        return

    total = len(produtos_baixo)
    for i, produto in enumerate(produtos_baixo, start=1):
        print("-----------------------------")
        print(f"Código: {produto['codigo']}")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['catg']}")
        print(f"Preço: R$ {produto['preco']}")
        print(f"Quantidade: {produto['qtd']}")
        if not pausar_paginacao(i, total):
            break

    log_operacao(f"Relatório estoque baixo: limite {limite}, encontrados {total}")

def listar_produtos_codigo():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    total = len(produtos)
    for i, produto in enumerate(produtos, start=1):
        print("-----------------------------")
        print(f"Código: {produto['codigo']}\nNome: {produto['nome']}\n"
            f"Categoria: {produto['catg']}\nPreço: {produto['preco']}\n"
            f"Quantidade: {produto['qtd']}")
        if not pausar_paginacao(i, total):
            break

    log_operacao(f"Listar produtos por código: total {total}")

def listar_produtos_categoria():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    categoria = ler_texto("Digite a categoria do produto: ")
    produtos_categoria = [produto for produto in produtos if produto['catg'].lower() == categoria.lower()]

    if not produtos_categoria:
        print("Nenhum produto encontrado na categoria especificada")
        log_operacao(f"Listar produtos por categoria: categoria {categoria}, encontrados 0")
        return

    total = len(produtos_categoria)
    for i, produto in enumerate(produtos_categoria, start=1):
        print("-----------------------------")
        print(f"Código: {produto['codigo']}\nNome: {produto['nome']}\n"
            f"Categoria: {produto['catg']}\nPreço: {produto['preco']}\n"
            f"Quantidade: {produto['qtd']}")
        if not pausar_paginacao(i, total):
            break

    log_operacao(f"Listar produtos por categoria: categoria {categoria}, encontrados {total}")


def relatorio_preco_min_max():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    menor_preco = min(produtos, key=lambda produto: produto['preco'])
    maior_preco = max(produtos, key=lambda produto: produto['preco'])

    print("\n--- RELATÓRIO DE MENOR E MAIOR PREÇO ---")
    print("\nProduto com menor preço:")
    print(f"Código: {menor_preco['codigo']}\nNome: {menor_preco['nome']}\n"
          f"Categoria: {menor_preco['catg']}\nPreço: R$ {menor_preco['preco']}\n"
          f"Quantidade: {menor_preco['qtd']}")

    print("\nProduto com maior preço:")
    print(f"Código: {maior_preco['codigo']}\nNome: {maior_preco['nome']}\n"
          f"Categoria: {maior_preco['catg']}\nPreço: R$ {maior_preco['preco']}\n"
          f"Quantidade: {maior_preco['qtd']}")

    log_operacao(f"Relatório menor/maior preço: menor código {menor_preco['codigo']} preço {menor_preco['preco']}, maior código {maior_preco['codigo']} preço {maior_preco['preco']}")

