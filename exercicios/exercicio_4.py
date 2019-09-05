class Hmmm:
    def __init__(self):
        self.valor_pago = 0
        self.preco = 0
        self.troco = 0

    def aumm(self, valor_pago, preco):
        #self.valor_pago = float(input("Digite o valor total que foi pago:"))
        #self.preco = float(input("\n Digite o preço do produto"))
        self.troco = self.valor_pago - self.preco
        batatafrita = ("O troco a ser dado é R$", self.troco)
        return batatafrita
