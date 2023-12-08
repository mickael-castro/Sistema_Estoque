import sys
from enum import IntEnum, unique
from datetime import date

id = 0
vendas_id = 0
perdas_id = 0

@unique
class Funcionalidade(IntEnum):
    VENDER = 1
    CADASTRO = 2
    RELATORIO = 3
    CONTROLE = 4

class Venda:
    def __init__(self, produtos_vendidos, ganho_total, custo_total):
        global vendas_id
        vendas_id += 1
        self.id = vendas_id
        self.produtos_vendidos = produtos_vendidos
        self.ganho_total = ganho_total
        self.custo_total = custo_total
        self.data = date.today()

class Perda:
    def __init__(self, produtos_perdidos, perda_total):
        global perdas_id
        perdas_id += 1
        self.id = perdas_id
        self.produtos_perdidos = produtos_perdidos  # Adicione esta linha
        self.perda_total = perda_total
        self.data = date.today()

class Produto:
    def __init__(self, nome, custo, preco, quantidade, validade=None):
        self.modificar_id()
        self.id = id

        self.nome = nome
        self.custo = custo
        self.preco = preco
        self.validade = validade
        self.quantidade = quantidade

    def modificar_id(self):
        global id
        id = id + 1

class Estoque:
    def __init__(self):
        self.carrinho = []
        self.total_ganhos = 0.0
        self.total_custos = 0.0
        self.produtos = []
        self.vendas = []
        self.perdas = []

        arroz = Produto('Saco de Arroz (1 Kg)', 5.4,  10.8, 10, date(2023, 12, 1))
        self.produtos.append(arroz)

        feijao = Produto('Saco de Feijao (1 Kg)', 4.25, 8.5, 10, date(2023, 12, 12))
        self.produtos.append(feijao)

        macarrao = Produto('Saco de Macarrão (500 g)', 2.90 , 5.8, 10, date(2023, 12, 12))
        self.produtos.append(macarrao)

        carne = Produto('Peça de maminha (1 Kg)', 12.5, 25.0, 10, date(2023, 12, 10))
        self.produtos.append(carne)

        pano = Produto('Pano de prato', 25, 50.0, 10)
        self.produtos.append(pano)

    def escolha_funcao(self):
        while True:
            print("Escolha entre as opções abaixo de funcionalidades:")
            for funcionalidade in Funcionalidade:
                print(f'{funcionalidade.value} - {funcionalidade.name.capitalize()}')

            escolha = input("Digite o número correspondente à funcionalidade que você deseja usar ou '0' para Cancelar: ")
            print()

            if escolha == "0":
                break

            try:
                escolha = int(escolha)
            except ValueError:
                print("Digite um número válido.")
                continue

            if escolha == Funcionalidade.VENDER.value:
                self.vender()
            elif escolha == Funcionalidade.CADASTRO.value:
                self.cadastro_produto()
            elif escolha == Funcionalidade.RELATORIO.value:
                self.relatorio_vendas()
                self.relatorio_perdas()
                self.relatorio_geral()
            elif escolha == Funcionalidade.CONTROLE.value:
                self.controle()
            else:
                print("Funcionalidade não encontrada")
                print()

    def cadastro_produto(self):
        from datetime import datetime

        while True:
            novo_produto = input("Digite o nome do produto a cadastrar (ou '0' para cancelar): ")
            print()

            if novo_produto == "0":
                break

            novo_custo = input("Digite o custo deste produto: ")
            print()
            try:
                custo = float(novo_custo)
            except ValueError:
                print("Digite um valor válido para o custo.")
                print()
                continue

            novo_preco = input("Digite o preço deste produto: ")
            print()
            try:
                preco = float(novo_preco)
            except ValueError:
                print("Digite um valor válido para o preço.")
                print()
                continue

            data_validade_str = input(
                "Digite a data de validade no formato (DD/MM/AAAA) ou pressione Enter para não definir uma data de validade: ")

            if data_validade_str.strip():  # Verifica se foi fornecida uma data de validade
                try:
                    data_validade = datetime.strptime(data_validade_str, "%d/%m/%Y").date()
                except ValueError:
                    print("Digite uma data válida no formato correto (DD/MM/AAAA).")
                    print()
                    continue
            else:
                data_validade = None  # Define como None se nenhuma data for fornecida

            nova_quantidade = input("Digite a quantidade deste produto: ")
            print()
            try:
                quantidade = int(nova_quantidade)
            except ValueError:
                print("Digite uma quantidade válida.")
                print()
                continue

            produto = Produto(novo_produto, custo, preco, quantidade, data_validade)
            self.produtos.append(produto)

            print(f'Produto {produto.nome} cadastrado com sucesso.')
            print()

    def vender(self):
        while True:
            print("Catálogo de produtos:")
            print("ID  | Quantidade | Nome do Produto             | Preço      | Validade ")
            for produto in self.produtos:
                if produto.validade is not None:
                    print(
                        f"{produto.id:2} | {produto.quantidade:2} | {produto.nome:30} | R${produto.preco:.2f} | {produto.validade.strftime('%d/%m/%Y')}")
                else:
                    print(
                        f"{produto.id:2} | {produto.quantidade:2} | {produto.nome:30} | R${produto.preco:.2f} | Sem validade")
            escolha = input("Digite o id do produto que deseja vender (ou `0` para encerrar): ")
            print()

            if escolha == "0":
                break

            escolha = int(escolha)

            selecao = None  # Inicializa selecao como None

            for produto in self.produtos:
                if produto.id == escolha:
                    selecao = produto
                    break  # Para o loop após encontrar o produto correspondente

            if selecao is not None:
                qtd_desejada = input("Digite a quantidade desejada (ou `0` para cancelar seleção de produto): ")
                print()

                if qtd_desejada == "0":
                    print("Seleção de produto cancelada.")
                    print()
                    continue

                qtd_desejada = int(qtd_desejada)

                while qtd_desejada > selecao.quantidade:
                    qtd_desejada = int(input(f"Há apenas {selecao.quantidade} unidades de {selecao.nome}. "
                                             f"Digite novamente a quantidade desejada (ou `0` para cancelar seleção de produto):"))
                    print()
                    if qtd_desejada == 0:
                        print("Seleção de produto cancelada.")
                        print()
                        break
                if qtd_desejada != 0:
                    # Atualiza a quantidade no catálogo
                    selecao.quantidade -= qtd_desejada
                    self.carrinho.append((selecao, qtd_desejada))
                    print(f"{qtd_desejada} unidades de {selecao.nome} adicionadas ao carrinho. ")
                    print()

            else:
                print("Produto não encontrado no catálogo. Tente novamente. ")
                print()

        print("\nResumo da compra")
        print("ID  | Quantidade | Nome do Produto             | Preço Unitário | Preço Total ")
        for produto, quantidade in self.carrinho:
            preco_total = produto.preco * quantidade
            custo_total = produto.custo * quantidade
            print(
                f"{produto.id:2} | {quantidade:2} | {produto.nome:30} | R${produto.preco:.2f} | R${preco_total:.2f} ")

            self.total_custos += custo_total
            self.total_ganhos += preco_total

        print(f"Total da Compra: R${self.total_ganhos}")

        confirmacao = input("Você deseja confirmar a venda? (s ou n)")
        print()

        if confirmacao == "n":
            # Cancele a venda e reverta as alterações no estoque
            for produto, quantidade in self.carrinho:
                produto.quantidade += quantidade

            self.carrinho = []
            self.total_ganhos = 0.0
            self.total_custos = 0.0

            print("A venda foi cancelada. O estoque foi restaurado.")
            print()
        elif confirmacao == "s":
            venda = Venda(self.carrinho, self.total_ganhos, self.total_custos)
            self.vendas.append(venda)

            self.carrinho = []
            self.total_ganhos = 0.0
            self.total_custos = 0.0

            print("A venda foi registrada com sucesso")
            print()

        escolha2 = input("Você deseja escolher outra funcionalidade? (s ou n)")

        if escolha2.lower() == "n":
            sys.exit()
        elif escolha2.lower() == "s":
            self.escolha_funcao()

    def relatorio_vendas(self):
        if len(self.vendas) == 0:
            print("Nenhuma venda registrada.")
        else:
            print("Relatório de Vendas:")
            print("ID  | Quantidade | Nome do Produto             | Preço Unitário | Preço Total ")
            for venda in self.vendas:
                print(f" {venda.id}")
                print(f"Data da Venda: {venda.data.strftime('%d/%m/%Y')}")
                print("Produtos Vendidos:")
                for produto, quantidade in venda.produtos_vendidos:
                    print(f"{produto.nome} - Quantidade: {quantidade} - Preço Unitário: R${produto.preco:.2f}")
                print(f"Total de Custos da Venda: R${venda.custo_total:.2f}")
                print(f"Total de Ganhos da Venda: R${venda.ganho_total:.2f}")
                print()

    def relatorio_perdas(self):
        if len(self.perdas) == 0:
            print("Nenhuma perda registrada.")
        else:
            print("Relatório de Perdas:")
            for perda in self.perdas:
                print(f"ID da Perda: {perda.id}")
                print(f"Data da Perda: {perda.data.strftime('%d/%m/%Y')}")
                print("Produtos Perdidos:")
                for produto, quantidade in perda.produtos_perdidos:
                    print(f"{produto.nome} - Quantidade: {quantidade} - Custo Unitário: R${produto.custo:.2f}")
                print(f"Total de Perdas: R${perda.perda_total:.2f}")
                print()

    def relatorio_geral(self):
        ganhou = 0
        gastou = 0
        perdeu = 0
        for perda in self.perdas:
            perdeu = perdeu + perda.perda_total

        for venda in self.vendas:
            ganhou = ganhou + venda.ganho_total
            gastou = gastou + venda.custo_total

        lucro = ganhou - (gastou + perdeu)
        print("Relatório Geral:")
        print(f"Ganhou-se: R${ganhou:.2f}")
        print(f"Gastou-se: R${gastou:.2f}")
        print(f"Perdeu-se: R${perdeu:.2f}")
        print()

        print(f"Lucro final: R${lucro:.2f}")
        print()

    def controle(self):
        agora = date.today()
        for produto in self.produtos:
            if produto.validade is not None and produto.validade < agora:
                print(
                    f"{produto.id:2} | {produto.quantidade:2} | {produto.nome:30} | R${produto.preco:.2f} | {produto.validade.strftime('%d/%m/%Y') if produto.validade else 'Sem validade'}")

        delete = input("Você deseja deletar o registro dos produtos inválidos? (s ou n)")

        if delete == 's':
            for produto in self.produtos:
                if produto.validade is not None and produto.validade < agora:
                    perda = Perda([(produto, produto.quantidade)], produto.custo * produto.quantidade)  # Modifique esta linha
                    self.perdas.append(perda)
                    del self.produtos[self.produtos.index(produto)]

                elif delete == 'n':
                    print("Não deletou nenhum produto inválido")

            escolha = input('Você deseja deletar algum outro produto mesmo assim? (s ou n)')
            if escolha.lower() == 's':
                self.deletar()


    def deletar(self):
        while True:
            print("Catálogo de produtos:")
            print("ID  | Quantidade | Nome do Produto             | Preço      | Validade ")
            for produto in self.produtos:
                print(
                    f"{produto.id:2} | {produto.quantidade:2} | {produto.nome:30} | R${produto.preco:.2f} | {produto.validade.strftime('%d/%m/%Y') if produto.validade else 'Sem validade'}")
            escolha = int(input("Qual o id do produto que você deseja deletar? "))

            produto_encontrado = False
            for produto in self.produtos:
                if produto.id == escolha:
                    produto_encontrado = True
                    confirmacao = input(f"Você realmente deseja deletar o produto '{produto.nome}'? (s ou n) ")
                    if confirmacao.lower() == 's':
                        # Deleta o produto
                        del self.produtos[self.produtos.index(produto)]
                        print("O produto foi deletado.")
                    break

            if not produto_encontrado:
                print("Produto não encontrado. Tente novamente.")

            escolha2 = input("Você deseja deletar mais algum produto? (s ou n) ")

            if escolha2.lower() == 'n':
                break


if __name__ == "__main__":
    estoque = Estoque()
    estoque.escolha_funcao()