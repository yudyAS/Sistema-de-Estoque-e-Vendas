from produto import listar_produtos_codigo, listar_produtos_categoria, remover_produto, registrar_venda, relatorio_estoque_baixo, relatorio_preco_min_max, editar_produto
from estoque import cadastrar_produto, buscar_codigo, buscar_nome
from arquivos import salvar_dados, carregar_dados

while True:

    print("---------- MENU ---------")
    print("1 - Cadastrar Produto") #feito
    print("2 - Editar produto") #feito
    print("3 - Remover produto") #feito
    print("4 - Buscar produto por código")#feito
    print("5 - Buscar produto por nome")#feito
    print("6 - Registrar venda (reduz estoque, valida quantidade)") #feito
    print("7 - Listar produtos por código")#feito
    print("8 - Listar produtos por categoria")#feito
    print("9 - Relatório de estoque baixo (quantidade < limite configurável)") #feito
    print("10 - Relatório de menor/maior preço")
    print("11 - Salvar e carregar dados em arquivo (CSV ou JSON)") #feito
    print("0 - Sair")

    escolha = input("Escolha a opção: ").strip()
    if not escolha.isdigit():
        print("Opção inválida. Digite um número entre 0 e 11.")
        continue

    menu = int(escolha)

    match menu:
        case 1: 
            cadastrar_produto()
        case 2:
            editar_produto()
        case 3:
            remover_produto()
        case 4:
            buscar_codigo()
        case 5:
            buscar_nome()
        case 6:
            registrar_venda()
        case 7:
            listar_produtos_codigo()
        case 8:
            listar_produtos_categoria()
        case 9:
            relatorio_estoque_baixo()
        case 10:
            relatorio_preco_min_max()
        case 11:
            print("1 - Salvar dados")
            print("2 - Carregar dados")
            sub = input("Escolha a opção: ").strip()
            if not sub.isdigit():
                print("Opção inválida.")
                continue
            sub = int(sub)
            if sub == 1:
                salvar_dados()
            elif sub == 2:
                carregar_dados()
            else:
                print("Opção inválida.")
        case 0:
            print("Saindo")
            break