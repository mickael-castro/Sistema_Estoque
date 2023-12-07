class Estoque:
    def __init__(self):
        self.catalogo = {"arroz": 10.8, "Feijao": 8.5, "macarrão": 5.8, "carne": 25.0}
        self.carrinho = {}
        self.total = 0.0

    def comprar (self):
        while true:
            print("catálogo de produtos:")
            for produto, preco in self.catalogo.items():
                print()
        pass