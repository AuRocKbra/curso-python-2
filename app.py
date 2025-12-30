from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa
from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('suco', 7.50, 'medio')
prato_salada = Prato('salada', 23.50, 'Salada com carne')
sobremesa_sorvete = Sobremesa('sorvete avelã',17.30,'sorvete','grande','Sorvete de chocolate de avelã')

def main():
    prato_salada.aplicar_desconto()
    bebida_suco.aplicar_desconto()
    sobremesa_sorvete.aplicar_desconto()
    restaurante_praca.adicinar_item_cardapio(sobremesa_sorvete)
    restaurante_praca.adicinar_item_cardapio(bebida_suco)
    restaurante_praca.adicinar_item_cardapio(prato_salada)
    restaurante_praca.listar_cardapio()


if __name__ == '__main__':
    main()