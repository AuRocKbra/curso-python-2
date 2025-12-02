class ItemCardapio:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    def __str__(self):
        print(f'{'Nome'.ljust(10)} | {'Preço'}')
        return f'{self._nome.ljust(10)} | R$ {self._preco:.2f}'