#!/usr/bin/python3
end_state = 0
gameBoard = {
    "1": " ",
    "2": " ",
    "3": " ",
    "4": " ",
    "5": " ",
    "6": " ",
    "7": " ",
    "8": " ",
    "9": " "
}

def display_gameBoard(gameBoard):
    print(gameBoard["1"] + "|" + gameBoard["2"] + "|" + gameBoard["3"])
    print("-+-+-")
    print(gameBoard["4"] + "|" + gameBoard["5"] + "|" + gameBoard["6"])
    print("-+-+-")
    print(gameBoard["7"] + "|" + gameBoard["8"] + "|" + gameBoard["9"])

def check_verticals(gameBoard, end_state):
    if gameBoard["1"] == gameBoard["4"] == gameBoard["7"] and gameBoard["1"] != " ":
        end_state = 1
        winner = gameBoard["1"]
    elif gameBoard["2"] == gameBoard["5"] == gameBoard["8"] and gameBoard["2"] != " ":
        end_state = 1
        winner = gameBoard["2"]
    elif gameBoard["3"] == gameBoard["6"] == gameBoard["9"] and gameBoard["3"] != " ":
        end_state = 1
        winner = gameBoard["3"]
    else:
        end_state = 0
        winner = ""

    return end_state, winner

def end_game(winner, gameBoard):
    display_gameBoard(gameBoard)
    print("Winner of the game was: " + winner)

end_state, winner = check_verticals(gameBoard, end_state)

if(end_state == 1):
    end_game(winner, gameBoard)
else:
    print("NO WINNER YET")
