#!/usr/bin/python3

gameBoard = {
    "1": "",
    "2": "",
    "3": "",
    "4": "",
    "5": "",
    "6": "",
    "7": "",
    "8": "",
    "9": ""
}

def display_gameBoard(gameBoard):
    print(" " + gameBoard["1"] + " | " + gameBoard["2"] + " | " + gameBoard["3"])
    print("---+---+---")
    print(" " + gameBoard["4"] + " | " + gameBoard["5"] + " | " + gameBoard["6"])
    print("---+---+---")
    print(" " + gameBoard["7"] + " | " + gameBoard["8"] + " | " + gameBoard["9"])

display_gameBoard(gameBoard)
