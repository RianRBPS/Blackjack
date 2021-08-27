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


def hit(deck, hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing # Controla um while Loop futuro

    while True:
        x = input('Comprar ou Parar? ').strip().lower()

        if x[0] == 'c':
            hit(deck, hand)

        elif x[0] == 'p':
            print('Jogador parou, turno do Dealer')
            playing == False

        else:
            print('Desculpe, eu não entedi, por favor informe se deseja continuar ou parar.')
            continue
        break
