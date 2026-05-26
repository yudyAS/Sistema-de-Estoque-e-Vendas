from produto import listar_produtos_codigo, listar_produtos_categoria, remover_produto, registrar_venda, relatorio_estoque_baixo
from estoque import cadastrar_produto, inserir_ordenado, buscar_codigo, buscar_nome, busca_binaria
from arquivos import salvar_dados, carregar_dados

while True:

    print("---------- MENU ---------")
    print("1 - Cadastrar Produto") #feito
    print("2 - Editar produto")
    print("3 - Remover produto") #feito
    print("4 - Buscar produto por código")#feito
    print("5 - Buscar produto por nome")#feito
    print("6 - Registrar venda (reduz estoque, valida quantidade)") #feito
    print("7 - Listar produtos por código")#feito
    print("8 - Listar produtos por categoria")#feito
    print("9 - Relatório de estoque baixo (quantidade < limite configurável)") #feito
    print("10 - Salvar e carregar dados em arquivo (CSV ou JSON)") #feito
    print("0 - Sair")

    menu = int(input("Escolha a opção: "))

    match menu:
        case 1: 
            cadastrar_produto()
        case 2:
            print("cadastrar()")
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
            print("1 - Salvar dados")
            print("2 - Carregar dados")
            sub = int(input("Escolha a opção: "))
            if sub == 1:
                salvar_dados()
            elif sub == 2:
                carregar_dados()
            else:
                print("Opção inválida.")
        case 0:
            print("Saindo")
            break