import sys
class Estoque:
    def __init__(self):
        self.catalogo = {"arroz": 10.8, "feijao": 8.5, "macarrão": 5.8, "carne": 25.0}
        self.carrinho = {}
        self.total = 0.0
        self.funcionalidades = ["Comprar", "Cadastro", "Relatorio", "Controle"]


    def esolha_funcao(self):
        while True:
            print("Escolha entre as opções abaixo de funcionalidade: ")
            for funcionalidades in self.funcionalidades:
                print(f'{funcionalidades.capitalize()}')

            escolha = input("Digite qual das funcionalidade você deseja. (ou ´sair´ para Cancelar): ")

            if escolha.lower() == "sair":
                break

            if escolha in self.funcionalidades:
                if escolha.lower() == "comprar":
                    self.comprar()
                elif escolha.lower() == "cadastro":
                    self.cadastro_produto()
            else:
                print("Não encontrei tal funcionalidade, ou não implementamos ainda :(")
                print("Tente Novamente")
                self.esolha_funcao()

    def cadastro_produto(self):
        while True:
            novo_produto = input("Digite o produto a cadastrar. (ou 'sair' para cancelar): ")

            if novo_produto.lower() == "sair":
                break

            novo_preco = input("Digite o preco deste produto. (ou 'sair' para cancelar): ")

            if novo_preco.lower() == "sair":
                break

            # Convertendo o preço para float
            preco = float(novo_preco)

            # Atualizando o catálogo
            self.catalogo.update({novo_produto: preco})
            for produto, preco in self.catalogo.items():
                print(f'{produto.capitalize()} - R${preco}')

    def comprar(self):
        while True:
            print("Catálogo de produtos:")
            for produto, preco in self.catalogo.items():
                print(f'{produto.capitalize()} - R${preco}')

            escolha = input("Digite o nome do produto que deseja comprar (ou `sair` para encerrar): ")

            if escolha.lower() == "sair":
                break

            if escolha in self.catalogo:
                quantidade = int(input("Digite a quantidade desejada: "))
                if escolha in self.carrinho:
                    self.carrinho[escolha] += quantidade
                else:
                    self.carrinho[escolha] = quantidade
                print(f"{quantidade} unidades de {escolha.capitalize()} adicionadas ao carrinho. ")
            else:
                print("Produto não encontrado no catálogo. Tente novamente. ")

        print("\nResumo da compra")
        for produto, quantidade in self.carrinho.items():
            preco_unitario = self.catalogo[produto]
            preco_total = preco_unitario * quantidade
            print(f"{quantidade} unidades de {produto.capitalize()} - R${preco_total:.2f}")
            self.total += preco_total

        print(f"Total da Compra: R${self.total}")
        self.pagar()

    def pagar(self):
        while True:
            pagamento = input("Digite o valor recebido pelo Cliente (ou 'cancelar' para cancelar a compra): ")

            if pagamento.lower() == "cancelar":
                print("Compra cancelada")
                return

            try:
                valor_pago = float(pagamento)
            except ValueError:
                print("Digite um valor válido.")
                continue

            troco = valor_pago - self.total

            if troco >= 0:
                print(f"Troco: R${troco}")
                break  # Sai do loop se o troco for não negativo
            else:
                print(f"Valor insuficiente. Faltam R${-troco}")

        cpf_nota = input("Deseja informar o CPF na nota? (sim/não): ")
        if cpf_nota.lower() == "sim":
            cpf = input("Digite o CPF: ")
            print(f"Nota fiscal: Total da compra - R${self.total} | CPF - {cpf}")

        else:
            print(f"Nota fiscal: Total da compra - R${self.total}")

        escolha2 = input("Você deseja continuar?(sim ou nao)")

        if escolha2.lower() == "nao": #escolha de continuação do código
            sys.exit()
        else:
            self.esolha_funcao()





if __name__ == "__main__":
    estoque = Estoque()
    estoque.esolha_funcao()