import random

def create_deck():

    deck = []

    cards = ["0", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"] 

    for suit in ["Clubs ♣", "Spades ♠", "Diamonds ♦", "Hearts ♥"]:
        for num in range(1, 14):
            if(num in (11,12,13)):
                deck.append([10, suit, cards[num]])
            else:
                deck.append([num, suit, cards[num]])
            

    return deck



def game(players):

    deck = create_deck()

    print("""\nWelcome to BlackJack. 
All players will get a random card to begin with.
Good luck and have fun!
""")

    players, deck = start_cards(players, deck)

    game_over = False
    rounds = 1

    while(game_over == False):

        print(f"\n\nRound {rounds}, start.\n")
        player, deck, game_over = round(players, deck)
        rounds += 1

    
    declare_winner(players)


def round(players, deck):

    '''Retorna players, deck e gameOver'''


    for player in players:

        player_name = players[player]['player_name']

        if players[player]["playing"]:

            continue_stop = int(input(f"""\n{player_name} you have {players[player]['cards_sum']} points.\nDo you wanna withdraw another card or stop? (1 to continue, 0 to stop): """))

            if continue_stop == 1:

                points, deck = raffle(player_name, deck)

                players[player]["cards_sum"] += points

                status_player = check_points(players[player]["cards_sum"])

                if status_player == 2:

                    print(f"{player_name} are above 21 points, they now have {players[player]['cards_sum']} points. {player_name} is out. ")
                    players[player]["playing"] = False

                elif status_player == 1:
                    return players, deck, True

                else:
                    print(f"{player_name} now has {players[player]['cards_sum']} points.")

            elif continue_stop == 0:

                print(f"{player_name} stopped and has {players[player]['cards_sum']} points.")
                players[player]["playing"] = False


    if (check_continue_game(players, deck) == False):
        return players, deck, True
            
    return players, deck, False

        


def start_cards(players, deck):

    for player in players:
        
        player_name = players[player]["player_name"]

        points, deck = raffle(player_name, deck)

        print(f"{player_name} started with {points} points.")

        players[player]["cards_sum"] = points
        players[player]["playing"] = True

    return players, deck


def declare_winner(players):

    print("Checking winner.... \n\n")

    biggest_points = {"points" : [-1], "players" : [-1]}

    for player in players:

        if players[player]["cards_sum"] == 21:
            print(f"Congrats {players[player]['player_name']} you've reachead exactly 21 points!!! You've won!")
            return

        if players[player]["cards_sum"] > biggest_points["points"][0] and players[player]["cards_sum"] < 21:
            biggest_points["points"] = [players[player]["cards_sum"]]
            biggest_points["players"] = [players[player]["player_name"]]

        elif players[player]["cards_sum"] == biggest_points["points"][0]:
            biggest_points["points"].append(players[player]["cards_sum"]) 
            biggest_points["players"].append(players[player]["player_name"]) 
            
    
    if len(biggest_points["points"]) == 1 and biggest_points["points"][0] != -1:
        print(f"Congrats! {biggest_points['players'][0]} have won with {biggest_points['points'][0]} points.")
    
    elif biggest_points["points"][0] == -1:
        print("All the players are over 21. Game Over!")

    elif len(biggest_points["points"]) > 1:
        print(f"Withdraw! List of winners:\n{biggest_points['players']}.\nYou all got {biggest_points['points'][0]} points.")
    
        


def raffle(player_name, deck):
    
    card_withdrown = random.choice(deck)
    deck.remove(card_withdrown)

    points = card_withdrown[0] 

    print(f"Player {player_name} got a {card_withdrown[2]} of {card_withdrown[1]}.")

    return points, deck


def check_continue_game(players, deck):

    if len(deck) == 0:
        return False

    for player in players:

        if players[player]["playing"]:
            return True
    
    return False




def check_points(points):
    
    if points < 21:
        return 0
    elif points == 21:
        return 1
    else:
        return 2


def create_players(num_players):
    
    players = {}

    for num in range(0, num_players):

        player_name = input(f"Enter the name of the player number {num + 1}: ")

        players[num] = {"player_name" : player_name, "cards_sum" : 0, "playing" : True}

    print(f"\nThere are {len(players)} players. The game will begin.")

    return players


def main():

    players = create_players(int(input("\nEnter the num of players (just integer numbers): ")))
    new_game = -1

    while new_game != 0:

        game(players)

        new_game = int(input("Do you wanna play again? Same players. 1 to yes or 0 to no: "))

        while new_game not in (0,1): 
            new_game = int(input("Do you wanna play again? Same players. 1 to yes or 0 to no: "))
        
        if new_game == 0:
            print("\n---------------------------\nShutting game down...\n---------------------------")

main()