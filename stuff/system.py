from stuff import *


def take_bet(chips):

    while True:

        try:
            chips.bet = int(input('Quantas fichas você gostaria de apostar? '))
            break
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
     # Controla um while Loop futuro

    while True:
        global playing
        x = input('Comprar ou Parar? ').strip().lower()

        if x[0] == 'c':
            hit(deck, hand)

        elif x[0] == 'p':
            print('Jogador parou, turno do Dealer')
            playing == False
            break
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



while True:
    print('Bem vindo ao BlackJack')

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing == True: # Era playing

        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

            break

    if player_hand.value <= 21:

        # Soft 17 rule
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value: # SOFT 17 RULE
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    print(f'\n Fichas do jogador atualmente: {player_chips.total}')

    new_game = input('Gostaria de jogar novamente? ').strip().lower()

    if new_game[0] == 's':
        playing = True
        continue
    else:
        print('Thank you for playing')
        break

