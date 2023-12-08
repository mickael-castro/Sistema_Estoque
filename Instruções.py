"""
1.  Funcionalidades:(Mickael e Clara)
   - O sistema oferece quatro funcionalidades principais representadas pela enumeração  Funcionalidade:
      -  VENDER  (1): Realizar vendas.
      -  CADASTRO  (2): Cadastrar novos produtos no estoque.
      -  RELATÓRIO  (3): Gerar relatórios de vendas, de perdas e um relatório geral.
      -  CONTROLE  (4): Realizar controle de produtos pela validade ou excluir o registro de um produto

2.  Classes: (Mickael e Clara)
   - O código define quatro classes principais:
      - Estoque: Representa o estoque com atributos carrinho (lista dos produtos a serem vendidos), total_ganhos,
      total_custos, produtos (lista dos produtos disponíveis em estoque), vendas (lista que guarda as vendas
      realizadas para registro) e perdas (lista que guarda as perdas para registro) e os métodos escolha_funcao,
      cadastro_produto, vender, relatorio_vendas, relatorio_perdas, relatorio_geral, controle e deletar.
      - Produto: Representa um produto no estoque com atributos como nome, custo, preço, quantidade e validade.
      - Venda: Representa uma transação de venda, registrando produtos vendidos, ganho total, custo total e data.
      - Perda: Representa uma transação de perda, registrando produtos perdidos, perda total e data.

3.  Estoque Inicial: (Mickael)
   - Ao iniciar o programa, é criada uma instância da classe Estoque que inicializa o estoque com alguns produtos.

4.  Menu de Funcionalidades: (Mickael e Clara)
   - O programa apresenta um menu de funcionalidades para o usuário, que pode escolher entre as opções disponíveis
   digitando o número correspondente.
   - As funcionalidades incluem venda de produtos, cadastro de novos produtos, geração de relatórios e controle
   de estoque.

5.  Cadastro de Produtos: (Mickael e Clara)
   - A opção de cadastro de produtos permite ao usuário adicionar novos produtos ao estoque, especificando nome,
   custo, preço, validade (opcional) e quantidade.

6.  Venda de Produtos: (Mickael)
   - A opção de venda permite ao usuário selecionar produtos do catálogo, especificar a quantidade desejada e
   finalizar a venda.

7.  Relatórios: (Clara)
   - O sistema gera relatórios de vendas, perdas e um relatório geral, exibindo informações relevantes sobre
   cada transação.

8.  Controle de Estoque: (Clara)
   - O controle de estoque verifica produtos vencidos e oferece a opção de deletar esses produtos do catálogo.

9.  Encerramento do Programa: (Mickael e Clara)
   - O programa continua em execução até que o usuário escolha sair digitando "0" ou escolha não continuar
   após uma funcionalidade específica.

10.  Execução:
   - O código finaliza com a criação de uma instância da classe  Estoque e a chamada da função escolha_funcao(),
    iniciando assim a interação do usuário com o sistema.

Para executar o projeto, basta seguir os comandos prescritos no terminal do programa. Tendo para cada sessão,
um código de id que representa uma funcionalidade presente.

"""