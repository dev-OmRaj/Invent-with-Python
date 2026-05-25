# Blackjack, also known as 21, is a card game where players try to get as close to 21 points as possible without going over. This program uses images drawn with text characters, called ASCII art.

from ast import While
import random
# Set up the constants:
HEARTS   = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES   = chr(9824) # Character 9824 is '♠'.
CLUBS    = chr(9827) # Character 9827 is '♣'.

def rules():
    for _ in range(50):
        print("-", end="")
    print("""\n\nRules:
      Try to get as close to 21 without going over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 through 10 are worth their face value.
      (H)it to take another card.
      (S)tand to stop taking cards.
      On your first play, you can (D)ouble down to increase your bet
      but must hit exactly one more time before standing.
      In case of a tie, the bet is returned to the player.
      The dealer stops hitting at 17.""")
    for _ in range(50):
        print("-", end="")
    print()

def valid_money(num, maximum_limit=50_000):

    if not num.isdecimal():
        print("Invalid Input!! Enter Again\n")
        return False
    num = int(num)
    if num < 0:
        print("Invalid Money!! This much money is not possible!\n")
        return False
    elif num > maximum_limit:
        print("We would very much like see you not go broke tonight. So limit you amount within ₹50k.\n")
        return False
    else:
        print(f"Cashing ₹{num}. Enjoy the Evening...\n")
        return True

def validate_bet(bet, total_money):
    if not bet.isdecimal():
        print("Invalid Bet..\n Enter Again.\n")
        return False
    bet = int(bet)
    if bet < 1 or bet > total_money:
        print("You Don't have Enough money.\nEnter Again\n")
        return False
    else:
        return True

def create_deck():
    # Make a complete deck of 52 cards
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for num_card in range(2, 11):
            deck.append((str(num_card), suit))
        for face_card in ('A', 'J', 'Q', 'K'):
            deck.append((face_card, suit))
    random.shuffle(deck)

    return deck

def show_card(player_hand, dealer_hand, show_dealer_hand):
    """Show the card of player and dealer, HIDE the first card of dealer, if `show_dealer_hand` is False"""
    print()

    # Show Dealer's Cards
    if show_dealer_hand:
        print("Dealer: ", get_card_value(dealer_hand))
        display_card(dealer_hand, True)
    else:
        print("Dealer: ???")
        display_card(dealer_hand, False)

    # Show Player's Card
    print("Player: ", get_card_value(player_hand))
    display_card(player_hand, True)

def get_card_value(hand):
    """Return the total count of the card"""
    sum = 0
    count_ace = 0

    for card in hand:
        if card[0] == 'A':
            count_ace += 1
        elif card[0] in ('J', 'Q' , 'K'):
            sum += 10
        else:
            sum += int(card[0])

    if sum + 11*count_ace <= 21:
        sum += 11*count_ace
    else:
        sum += count_ace
    
    return sum

def display_card(hand, show_first_card):
    '''Print the card on the Screen, if show_first_card == False, hide first card for dealer'''
    rows = ["", "", "", "", ""]
    for i , cards in enumerate(hand):
        rows[0] += " ___  "
        if show_first_card == False and i == 0:
            rows[1] += "|## | "
            rows[2] += "|###| "
            rows[3] += "|_##| "
            show_first_card = True
        else:
            r, s = cards
            rows[1] += "|{} | ".format(r.ljust(2))
            rows[2] += "| {} | ".format(s)
            rows[3] += "|_{}| ".format(r.rjust(2), "_")
    
    for row in rows:
        print(row)
        
def get_player_move(hand, money_left, bet):

    while True:
        possible_moves = ['h', 's']

        if len(hand) == 2 and money_left >= bet:
            possible_moves.append('d')
        
        if(len(possible_moves) == 3):
            print("Hit: H\nStand: S\nDouble Down(D)\nQuit: Q\n")
        else:
            print("Hit: H\nStand: S\nQuit: Q\n")
        
        move = input(">>> ").lower()

        if move == 'q':
            exit()
        if move in ('h', 's'):
            return move
        if move == 'd' and 'd' in possible_moves:
            return move
           
def game(total_money):
    # Checking Total Money

    # Taking Bets
    while True:
        if total_money <= 0:
            print("You don't have enough money to play.\nCome back when you have some money to play with.\n")
            exit()

        while True:
            print(f"Place your bet. (₹1 - ₹{total_money})")
            bet = input(">>> ₹ ").strip()
            if validate_bet(bet, total_money):
                bet = int(bet)
                break

        print(f"Your Bet ₹{bet}")

        card_deck = create_deck()

        # Initial Card distribution
        dealer_hand = [card_deck.pop(), card_deck.pop()]
        player_hand = [card_deck.pop(), card_deck.pop()]

        print("Bet: ", bet)
        # Start the Game
        while True:
            show_card(player_hand, dealer_hand, False)
            print()

            # Check if player hand is bust:
            if(get_card_value(player_hand)) > 21:
                break

            player_move = get_player_move(player_hand, total_money - bet, bet)

            if player_move == 'd':
                while True:
                    print(f"Enter additional bet Between 1 and {total_money-bet}.\n")
                    additional_bet = input(">>> ").strip()
                    if (validate_bet(additional_bet, total_money - bet)):
                        additional_bet = int(additional_bet)
                        break
                bet += additional_bet
                print(f"Bet increased to {bet}")
                print("Bet: ", bet)
                
            if player_move in ('h', 'd'):
                new_card = card_deck.pop()
                rank, suit = new_card
                print("You drew a {} of {}.".format(rank, suit))
                player_hand.append(new_card)

                if get_card_value(player_hand) > 21:
                    continue
            if player_move in ('s', 'd'):
                break
        

        if get_card_value(player_hand) <= 21:
            while get_card_value(dealer_hand) < 17:
                print("Dealer Hits...")
                dealer_hand.append(card_deck.pop())
                show_card(player_hand, dealer_hand, False)

                if get_card_value(dealer_hand) > 21:
                    break

                input("Press ENTER to continue...")
                print("\n\n")

        show_card(player_hand, dealer_hand, True)

        player_cards_value = get_card_value(player_hand)
        dealer_cards_value = get_card_value(dealer_hand)

        if dealer_cards_value > 21:
            print("Dealer Busts...\nYou Win ₹{}".format(bet))
            total_money += bet
        elif player_cards_value > 21 or player_cards_value < dealer_cards_value:
            print("You Lost! ₹{}".format(bet))
            total_money -= bet
        elif player_cards_value > dealer_cards_value:
            print(f"You Win! ₹{bet}")
            total_money += bet
        elif player_cards_value == dealer_cards_value:
            print("Its a tie, The bet ₹{} is returned to you.".format(bet))

        input("Press ENTER to continue.")
        print("\n\n")
    

def main():
    print("Welcome to June's Casino!\n")
    while True:
        total_money = input("How much money would you like to Cash in: ₹ ")
        if valid_money(total_money):
            total_money = int(total_money)
            break

    rules()
    game(total_money)

if __name__ == "__main__":
    main()