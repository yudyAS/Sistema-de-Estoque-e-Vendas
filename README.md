# Sistema de Estoque e Vendas 🚀

Projeto 1 de Estrutura de Dados com interface de linha de comando para controlar produtos, vendas e relatórios.
O sistema usa vetores ordenados e não ordenados conforme os requisitos de busca e armazenamento.

## 🎯 Objetivo
Construir um sistema em Python que permita:
- cadastrar produtos com código único, nome, categoria, preço e quantidade;
- editar e remover produtos;
- buscar por código e por nome;
- registrar vendas com atualização de estoque;
- gerar relatórios de categoria, estoque baixo e menor/maior preço;
- salvar e carregar dados em arquivo JSON.

## ✅ Funcionalidades implementadas
- ✅ Cadastro de produto com código único e validação de entradas.
- ✅ Edição de nome, categoria, preço e quantidade.
- ✅ Remoção por código.
- ✅ Busca por código usando busca binária em vetor ordenado (`produtos_ordenados`).
- ✅ Busca por nome usando busca linear em vetor não ordenado (`produtos`).
- ✅ Registro de venda com verificação de estoque suficiente.
- ✅ Listagem de produtos ordenados por código.
- ✅ Listagem de produtos por categoria.
- ✅ Relatório de estoque baixo com limite configurável.
- ✅ Relatório de menor e maior preço.
- ✅ Salvamento/carregamento de dados em JSON.
- ✅ Logs simples de operações em `operacoes.log`.
- ✅ Paginação básica nas listagens longas.

## 🗂️ Estrutura de arquivos
- `main.py`: menu e fluxo da aplicação.
- `estoque.py`: cadastro, leitura, validação de dados e buscas.
- `produto.py`: edição, remoção, vendas e relatórios.
- `arquivos.py`: persistência de dados e logs.

## ▶️ Como executar
1. Abra o terminal na pasta do projeto.
2. Execute `python main.py`.
3. Use o menu para escolher as opções.
4. Para salvar ou carregar dados, escolha a opção 11 no menu principal.
## 🖥️ Exemplo de execução
```text
---------- MENU ---------
1 - Cadastrar Produto
2 - Editar produto
3 - Remover produto
4 - Buscar produto por código
5 - Buscar produto por nome
6 - Registrar venda (reduz estoque, valida quantidade)
7 - Listar produtos por código
8 - Listar produtos por categoria
9 - Relatório de estoque baixo (quantidade < limite configurável)
10 - Relatório de menor/maior preço
11 - Salvar e carregar dados em arquivo (CSV ou JSON)
0 - Sair
Escolha a opção: 1
Digite o código do produto: 10
Digite o nome do produto: Caneta
Digite a categoria do produto: Escritório
Digite o preço (R$): 2.50
Digite a quantidade: 100
Produto cadastrado com sucesso!

Escolha a opção: 4
Digite o código do produto: 10
Código: 10
Nome: Caneta
Categoria: Escritório
Preço: 2.5
Quantidade: 100

Escolha a opção: 11
1 - Salvar dados
2 - Carregar dados
Escolha a opção: 1
Dados salvos em: dados.json
```
## 📌 Exemplo de uso do menu
- `1` - Cadastrar produto
- `4` - Buscar produto por código
- `5` - Buscar produto por nome
- `6` - Registrar venda
- `7` - Listar produtos por código
- `11` - Salvar ou carregar dados

## 🧹 Observações sobre o estilo de código
- O projeto segue PEP 8 em grande parte:
  - funções e variáveis usam `snake_case`.
  - indentação é de 4 espaços.
  - imports estão organizados por módulo.
- O código está modularizado para separar responsabilidades.

## 📋 Requisitos atendidos
- Interface por terminal clara.
- Persistência de dados em arquivo JSON.
- Validação de entradas numéricas e de texto.
- Busca binária em vetor ordenado para código.
- Busca linear em vetor não ordenado para nome.
- Validação de código duplicado e estoque insuficiente.
- Preço positivo e quantidade não negativa.

## 📝 Observações finais
O armazenamento utiliza dois vetores em memória:
- `produtos`: vetor não ordenado, usado para busca por nome e relatórios gerais.
- `produtos_ordenados`: vetor ordenado por código, usado para busca binária e listagem ordenada.

O sistema foi desenvolvido com foco em legibilidade, modularidade e transparência do comportamento esperado.