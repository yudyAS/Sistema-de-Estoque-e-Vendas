from produto import listar_produtos_codigo, listar_produtos_categoria
from estoque import cadastrar_produto, inserir_ordenado, buscar_codigo, buscar_nome, busca_binaria
from arquivos import salvar_dados, carregar_dados

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