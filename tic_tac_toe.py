
import itertools ##player_choice = itertools.cycle([1,2])
#Tic Tac Toe Game by sentdex on YT

## Winning Parameters
def win(current_game):
    
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

#horizontal winning
    for row in game:
        if all_same(row):
            print(f"Player {row[0]} is the winner horiz (-).")
            return True

#diagonal winning 
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[col][row])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diags (/).")
        return True

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diags (\\).")
        return True

#vertical winning
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])

        if all_same(check):
            print(f"Player {check[0]} is the winner vert (|) .")
            return True
    return False

#define function and parameters - GAME BOARD
def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0: #so players do no overwrite each other 
            print("This position is taken! get outta here.")
            return game_map, False
        #print("   0  1  2") #display game map
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:    ## if player != 0: #does not equal 0
            game_map[row][column] = player 
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True

    except IndexError as e: #index error handeling
        print("error, error, errorrrrrr wrong input!!!", e)
        return game_map, False
    
    except Exception as e: 
        print("done goofed", e)
        return game_map, False

#reseting the game
play = True
players = [1, 2]
while play:

    game_size = int(input("What size for your game board (number of rows and columns)?"))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    #runs inital game map
    game,_= game_board(game,just_display=True) 
    player_choice = itertools.cycle([1,2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False

        while not played:
            column_choice = int(input("What column do you want to play?"))
            row_choice = int(input("What row do you want to play?"))
            #runs game map after player decision
            game,played = game_board(game, current_player, row_choice, column_choice) 
        
        if win(game):
            game_won = True
            again = input("play again? (Y/N)") ## makes lowercase
            if again.lower() == "y":
                print("restarting...")
            elif again.lower() == "n": #else if 
                print("buh bye")
                play = False
            else:
                print("Not a valid input, please try again.")
                play = False

