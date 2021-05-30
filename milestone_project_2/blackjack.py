# CARD
# SUIT,RANK,VALUE
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten', 'Jack'
          , 'Queen','King', 'Ace')
values = {'Two': 2,'Three': 3,'Four': 4,'Five': 5,'Six':6,'Seven':7, 'Eight':8, 'Nine': 9 , 'Ten':10, 'Jack': 11
          , 'Queen': 12,'King': 13 , 'Ace': 14}

playing = True

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " +  self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.deck.append(created_card)

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()

        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop(0)
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class chips:
    def __init__(self,total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet



class blackjack:

    def __init__(self):
        pass

    def take_bet(self,chips):
        while True:
            try:
                chips.bet = int(input("How many chips would you like to bet? "))
            except:
                print("Sorry please provide an Integer")
            else:
                if chips.bet > chips.total:
                    print('Sorry you do not have enough chips! You have : {}'.format(chips.total))
                else:
                    break

    def hit(self,deck,hand):
        single_card = deck.deal()
        hand.add_card(single_card)
        hand.adjust_for_ace()

    def hit_or_stand(self,deck,hand):

        while True:
            x = input('Hit or Stand? Enter h or s')

            if x[0].lower() == 'h':
                self.hit(deck,hand)
            elif x[0].lower() == 's':
                print("Player stands, dealers turn")
                playing = False
            else:
                print("Sorry, please try again.")
                continue
            break

    def show_some(self,player,dealer):
        print("\n Dealer's hand: ")
        print("First card hidden!")
        print(dealer.cards[1])

        print("\n Players hand: ")
        for card in player.cards:
            print(card)


    def show_all(self,player,dealer):
        print("\n Players hand: ")
        for card in player.cards:
            print(card)
        print(f"Value of player's hand is : {player.value}")

        print("\n Dealers Hand: ",*dealer.cards,sep='\n')
        for card in dealer.cards:
            print(card)
        print(f"Value of dealer's hand is : {dealer.value}")


    def player_busts(self,dealer,player,chips):
        print("Player Busts!")
        chips.lose_bet(self)

    def player_wins(self, dealer, player, chips):
        print("Player wins!")
        chips.win_bet()

    def dealer_busts(self,dealer,player,chips):
        print("Dealer Busts!")
        chips.lose_bet()

    def dealer_wins(self, dealer, player, chips):
        print("Dealer wins!")
        chips.win_bet()
    def push(self,player,dealer):
        print('Its a tie between dealer and player')


    def game_logic(self):
        playing = True
        while True:
            print("Welcome to Blackjack!!")

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            player_hand.add_card(deck.deal())
            player_hand.add_card(deck.deal())

            dealer_hand = Hand()
            dealer_hand.add_card(deck.deal())
            dealer_hand.add_card(deck.deal())

            player_chips = chips()
            self.take_bet(player_chips)

            self.show_some(player_hand,dealer_hand)

            while playing:
                self.hit_or_stand(deck,player_hand)
                self.show_some(player_hand,dealer_hand)

                if player_hand.value > 21:
                    self.player_busts(dealer_hand,player_hand,chips)
                    break
                if player_hand.value <=21:

                    while dealer_hand.value < player_hand.value:
                        self.hit(deck,dealer_hand)

                    self.show_all(player_hand,dealer_hand)

                    if dealer_hand.value > 21:
                        self.dealer_busts(dealer_hand,player_hand,chips)
                    elif dealer_hand.value>player_hand.value:
                        self.dealer_wins(dealer_hand,player_hand,chips)
                    elif dealer_hand.value < player_hand.value:
                        self.player_wins(dealer_hand,player_hand,chips)
                    else:
                        self.push(player_hand,dealer_hand)

                print('\n Player total chips: {} '.format(player_chips.total))

                new_game = input('Would you like to play anoher hand? y/n ')

                if new_game[0].lower() == 'y':
                    playing=True
                    continue
                else:
                    print('Thank yoi for playing')
                    break

game = blackjack()
game.game_logic()