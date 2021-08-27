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


def show_some(player, dealer):

    # dealer.cards[1]

    # Show only ONE of the Dealer´s card
    print('\n Mão do Dealer: ')
    print('Primeira carta escondida!')
    print(dealer.cards[1])

    # Show all (2 cards) of the player´s hand
    print('\n Mão do jogador: ')
    for card in player.cards:
        print(card)

def show_all(player, dealer):

    # Show all the dealer´s cards
    print('\n Mão do Dealer: ')
    for card in dealer.cards:
        print(card)

    # print(f'Mão do Dealers: ', *dealer.cards,sep='\n')
    # Calculate and display value (J+K == 20)
    print(f'Valor da mão do Dealer é: {dealer.value}')

    # Show all the player´s cards
    print('\n Mão do jogador: ')
    for card in player.cards:
        print(card)
    print(f'Valor da mão do Jogador é: {player.value}')


def player_busts(player, dealer, chips):
    print('Jogador perde!')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('Jogador ganha!')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('Jogador ganha! Dealer perde!')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print('Dealer ganha! Jogador perde!')
    chips.lose_bet()


def push(player, dealer):
    print('Empate')