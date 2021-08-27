from stuff import *


def take_bet(chips):

    while True:

        try:
            chips.bet = int(input('Quantas fichas você gostaria de apostar? '))
        except:
            print('Por favor, forneça um valor inteiro')
        else:
            print(f'Desculpe, você não tem fichas o suficiente.\n'
                  f'Fichas atuais: {chips.total}')