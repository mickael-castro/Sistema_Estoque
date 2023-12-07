import sys
from enum import IntEnum, unique
from datetime import date

id = 0

@unique
class Funcionalidade(IntEnum):
    COMPRAR = 1
    CADASTRO = 2
    RELATORIO = 3
    CONTROLE = 4

class Produto:
    def __init__(self, nome, preco, validade, quantidade):
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

        arroz = Produto('Saco de Arroz (1 Kg)', 10.8, date(2023, 12, 10), 10)
        self.produtos.append(arroz)

        feijao = Produto('Saco de Feijao (1 Kg)', 8.5, date(2023, 12, 12), 10)
        self.produtos.append(feijao)

        macarrao = Produto('Saco de Macarrão (500 g)', 5.8, date(2023, 12, 7), 10)
        self.produtos.append(macarrao)

        carne = Produto('Peça de maminha (1 Kg)', 25.0, date(2023, 12, 10), 10)
        self.produtos.append(carne)

    def escolha_funcao(self):
        while True:
            print("Escolha entre as opções abaixo de funcionalidades:")
            for funcionalidade in Funcionalidade:
                print(f'{funcionalidade.value} - {funcionalidade.name.capitalize()}')

            escolha = input("Digite o número correspondente à funcionalidade que você deseja usar ou 'sair' para Cancelar: ")

            if escolha.lower() == "sair":
                break

            try:
                escolha = int(escolha)
            except ValueError:
                print("Digite um número válido.")
                continue

            if escolha == Funcionalidade.COMPRAR.value:
                self.comprar()
            elif escolha == Funcionalidade.CADASTRO.value:
                self.cadastro_produto()
            else:
                print("Funcionalidade não encontrada ou não implementada :(")

    def cadastro_produto(self):
        from datetime import datetime

        while True:
            novo_produto = input("Digite o nome do produto a cadastrar (ou 'sair' para cancelar): ")

            if novo_produto.lower() == "sair":
                break

            novo_preco = input("Digite o preço deste produto: ")
            try:
                preco = float(novo_preco)
            except ValueError:
                print("Digite um valor válido para o preço.")
                continue

            data_validade_str = input("Digite a data de validade no formato (DD/MM/AAAA): ")
            try:
                data_validade = datetime.strptime(data_validade_str, "%d/%m/%Y").date()
            except ValueError:
                print("Digite uma data válida no formato correto (DD/MM/AAAA).")
                continue

            nova_quantidade = input("Digite a quantidade deste produto: ")
            try:
                quantidade = int(nova_quantidade)
            except ValueError:
                print("Digite uma quantidade válida.")
                continue

            produto = Produto(novo_produto, preco, data_validade, quantidade)
            self.produtos.append(produto)

            print(f'Produto {produto.nome} cadastrado com sucesso.')

    def comprar(self):
        while True:
            print("Catálogo de produtos:")
            print("ID  | Quantidade | Nome do Produto             | Preço      | Validade ")
            for produto in self.produtos:
                print(
                    f"{produto.id:2} | {produto.quantidade:2} | {produto.nome:30} | R${produto.preco:.2f} | {produto.validade.strftime('%d/%m/%Y')}")
            escolha = input("Digite o id do produto que deseja comprar (ou `sair` para encerrar): ")

            if escolha.lower() == "sair":
                break

            escolha = int(escolha)

            selecao = None  # Inicializa selecao como None

            for produto in self.produtos:
                if produto.id == escolha:
                    selecao = produto
                    break  # Para o loop após encontrar o produto correspondente

            if selecao is not None:
                qtd_desejada = int(input("Digite a quantidade desejada: "))

                if qtd_desejada > selecao.quantidade:
                    qtd_desejada = int(input(f"Há apenas {selecao.quantidade} unidades de {selecao.nome}. Digite novamente a quantidade desejada (ou `sair` para cancelar seleção de produto):"))
                else:
                    # Atualiza a quantidade no catálogo
                    selecao.quantidade -= qtd_desejada
                    self.carrinho.append(selecao)
                    print(f"{qtd_desejada} unidades de {selecao.nome} adicionadas ao carrinho. ")

            else:
                print("Produto não encontrado no catálogo. Tente novamente. ")

        print("\nResumo da compra")
        print("ID  | Quantidade | Nome do Produto             | Preço Unitário | Preço Total ")
        for produto in self.carrinho:
            preco_total = produto.preco * qtd_desejada
            print(
                f"{produto.id:2} | {qtd_desejada:2} | {produto.nome:30} | R${produto.preco:.2f} | R${preco_total:.2f} ")

            self.total += preco_total

        print(f"Total da Compra: R${self.total}")
        escolha2 = input("Você deseja continuar?(sim ou nao)")

        if escolha2.lower() == "nao": #escolha de continuação do código
            sys.exit()
        else:
            self.escolha_funcao()

if __name__ == "__main__":
    estoque = Estoque()
    estoque.escolha_funcao()
