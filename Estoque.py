import sys
from enum import IntEnum, unique
from datetime import date

id = 0

@unique
class Funcionalidade(IntEnum):
    VENDER = 1
    CADASTRO = 2
    RELATORIO = 3
    CONTROLE = 4

class Produto:
    def __init__(self, nome, preco, validade=None, quantidade=int):
        self.modificar_id()
        self.id = id

        self.nome = nome
        self.preco = preco
        self.validade = validade
        self.quantidade = quantidade

    def modificar_id(self):
        global id
        id = id + 1

class Estoque:
    def __init__(self):
        self.carrinho = []
        self.total = 0.0
        self.produtos = []
        self.catalogo = []

        arroz = Produto('Saco de Arroz (1 Kg)', 10.8, date(2023, 12, 1), 10)
        self.produtos.append(arroz)

        feijao = Produto('Saco de Feijao (1 Kg)', 8.5, date(2023, 12, 12), 10)
        self.produtos.append(feijao)

        macarrao = Produto('Saco de Macarrão (500 g)', 5.8, date(2023, 12, 1), 10)
        self.produtos.append(macarrao)

        carne = Produto('Peça de maminha (1 Kg)', 25.0, date(2023, 12, 10), 10)
        self.produtos.append(carne)

        pano = Produto('Pano de prato "Me traga café que eu me expresso"', 50.0, None, 10)
        self.produtos.append(pano)

    def escolha_funcao(self):
        while True:
            print("Escolha entre as opções abaixo de funcionalidades:")
            for funcionalidade in Funcionalidade:
                print(f'{funcionalidade.value} - {funcionalidade.name.capitalize()}')

            escolha = input("Digite o número correspondente à funcionalidade que você deseja usar ou '0' para Cancelar: ")

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
            elif escolha == Funcionalidade.CONTROLE.value:
                self.controle()
            else:
                print("Funcionalidade não encontrada ou não implementada :(")

    def cadastro_produto(self):
        from datetime import datetime

        while True:
            novo_produto = input("Digite o nome do produto a cadastrar (ou '0' para cancelar): ")

            if novo_produto == "0":
                break

            novo_preco = input("Digite o preço deste produto: ")
            try:
                preco = float(novo_preco)
            except ValueError:
                print("Digite um valor válido para o preço.")
                continue

            data_validade_str = input(
                "Digite a data de validade no formato (DD/MM/AAAA) ou pressione Enter para não definir uma data de validade: ")
            if data_validade_str.strip():  # Verifica se foi fornecida uma data de validade
                try:
                    data_validade = datetime.strptime(data_validade_str, "%d/%m/%Y").date()
                except ValueError:
                    print("Digite uma data válida no formato correto (DD/MM/AAAA).")
                    continue
            else:
                data_validade = None  # Define como None se nenhuma data for fornecida

            nova_quantidade = input("Digite a quantidade deste produto: ")
            try:
                quantidade = int(nova_quantidade)
            except ValueError:
                print("Digite uma quantidade válida.")
                continue

            produto = Produto(novo_produto, preco, data_validade, quantidade)
            self.produtos.append(produto)

            print(f'Produto {produto.nome} cadastrado com sucesso.')

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

                if qtd_desejada == "0":
                    print("Seleção de produto cancelada.")
                    continue

                qtd_desejada = int(qtd_desejada)

                while qtd_desejada > selecao.quantidade:
                    qtd_desejada = int(input(f"Há apenas {selecao.quantidade} unidades de {selecao.nome}. "
                                             f"Digite novamente a quantidade desejada (ou `0` para cancelar seleção de produto):"))
                    if qtd_desejada == 0:
                        print("Seleção de produto cancelada.")
                        break
                if qtd_desejada != 0:
                    # Atualiza a quantidade no catálogo
                    selecao.quantidade -= qtd_desejada
                    self.carrinho.append((selecao, qtd_desejada))
                    print(f"{qtd_desejada} unidades de {selecao.nome} adicionadas ao carrinho. ")

            else:
                print("Produto não encontrado no catálogo. Tente novamente. ")

        print("\nResumo da compra")
        print("ID  | Quantidade | Nome do Produto             | Preço Unitário | Preço Total ")
        for produto, quantidade in self.carrinho:
            preco_total = produto.preco * quantidade
            print(
                f"{produto.id:2} | {quantidade:2} | {produto.nome:30} | R${produto.preco:.2f} | R${preco_total:.2f} ")

            self.total += preco_total

        print(f"Total da Compra: R${self.total}")

        confirmacao = input("Você deseja confirmar a venda? (s ou n)")

        if confirmacao == "s":
            self.carrinho = []
            #fazer registro de venda
            print("A venda foi registrada com sucesso")
        elif confirmacao == "n":

            self.carrinho = []


        escolha2 = input("Você deseja escolher outra funcionaldiade? (s ou n)")

        if escolha2.lower() == "n": #escolha de continuação do código
            sys.exit()
        elif escolha2.lower() == "s":
            self.escolha_funcao()

    def controle(self):
            agora = date.today()
            for produto in self.produtos:
                if produto.validade is not None:
                    print(
                        f"{produto.id:2} | {produto.quantidade:2} | {produto.nome:30} | R${produto.preco:.2f} | {produto.validade.strftime('%d/%m/%Y')}")

            delete = input("Você deseja deletar o registro dos produtos inválidos? (s ou n)")

            if delete == 's':
                for produto in self.produtos:
                    if produto.validade is not None and produto.validade < agora:
                        del self.produtos[self.produtos.index(produto)]

            elif delete == 'n':
                print("Não deletou nenhum produto inválido")

            escolha = input('Você deseja deletar algum outro produto mesmo assim? (s ou n)')
            if escolha.lower() == 's':
                self.deletar()

            # elif escolha.lower() == 'n':
            #     escolha2 = input("Você deseja escolher outra funcionaldiade? (s ou n)")
            #
            #     if escolha2.lower() == "n":  # escolha de continuação do código
            #         sys.exit()
            #     elif escolha2.lower() == "s":
            #         self.escolha_funcao()

    def deletar(self):
        while True:
            print("Catálogo de produtos:")
            print("ID  | Quantidade | Nome do Produto             | Preço      | Validade ")
            for produto in self.produtos:
                print(
                    f"{produto.id:2} | {produto.quantidade:2} | {produto.nome:30} | R${produto.preco:.2f} | {produto.validade.strftime('%d/%m/%Y')}")
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
