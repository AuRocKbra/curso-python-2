from modelos.cardapio.bebida import Bebida
from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.cardapio.prato import Prato
from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('suco', 2.50, 'medio')
prato_salada = Prato('salada', 3.50, 'Salada com carne')
item_generico = ItemCardapio('item generico', 1.50)

def main():
    restaurante_praca.adicinar_item_cardapio(bebida_suco)
    restaurante_praca.adicinar_item_cardapio(prato_salada)
    restaurante_praca.adicinar_item_cardapio(item_generico)
    restaurante_praca.listar_cardapio()


if __name__ == '__main__':
    main()