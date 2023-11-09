#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.controller.GameController import GameController
from src.model.Player import Player
from src.model.Position import Position


def display_board_raw(board):
    msg = ""
    for row in range(len(board.board)):
        for column in range(len(board.board[row])):
            msg += str(board.board[column][row].value)
        msg += "\n"
    print(msg)


def ask_position(num_columns, num_rows):
    pos = Position()
    # TODO: Protect with do while
    col_letter = input("Please write column letter:\t")
    col_letter.upper()
    col_letter = col_letter[0]
    if ord(col_letter) - ord('A') < 0 or ord(col_letter) - ord('A') >= num_columns:
        raise ValueError("Out of range letter.")
    pos.x = ord(col_letter) - ord('A')

    row_number = input("Please write row number:\t")
    row_number = row_number[0]
    row_number = int(row_number) - 1
    if row_number < 0 or row_number >= num_rows:
        raise ValueError("Out of range number.")

    pos.y = row_number

    return pos


def display_board(board):
    msg = ""

    row_letters = ""

    for row_number in range(len(board.board)):
        row_letters += chr(ord('A') + row_number)

    msg += "  " + row_letters + "\n"

    row_number = 1
    for r in range(len(board.board)):
        msg += str(row_number) + " "
        row_number += 1
        for column in range(len(board.board[r])):
            if board.board[column][r].isPaired:
                msg += " "
            elif board.board[column][r].isTurnedUp:
                msg += str(board.board[column][r].value)
            else:
                msg += "#"
        msg += "\n"
    print(msg)


def main_view_two_players():
    NUM_ROWS = 4
    NUM_COLUMNS = 4
    game_controller = GameController()

    player1 = Player()
    player2 = Player()
    player1.name = input("What is your name?\t")
    player2.name = input("What is your name?\t")

    game = game_controller.initialize_game_two_players(player1, player2, NUM_COLUMNS, NUM_ROWS)

    display_board(game.board)
    while not game.is_game_finished:
        if game.isPlayerOneTurn:
            print("~ Player 1:\t" + player1.name + "'s turn ~")
        else:
            print("~ Player 2:\t" + player2.name + "'s turn ~")

        pos1 = ask_position(NUM_COLUMNS, NUM_ROWS)
        pos2 = ask_position(NUM_COLUMNS, NUM_ROWS)
        game_controller.turn_cards(game.board, pos1.x, pos1.y, pos2.x, pos2.y)
        display_board(game.board)
        game_controller.turn_cards(game.board, pos1.x, pos1.y, pos2.x, pos2.y)
        is_success = False
        if game.isPlayerOneTurn:
            is_success = game_controller.play_turn(game, player1, pos1.x, pos1.y, pos2.x, pos2.y)
            if is_success:
                print("The player one " + player1.name + "has guessed a pair. It is his turn again.")
        else:
            is_success = game_controller.play_turn(game, player2, pos1.x, pos1.y, pos2.x, pos2.y)
            if is_success:
                print("The player two " + player2.name + "has guessed a pair. It is his turn again.")

        if not is_success:
            game.isPlayerOneTurn = not game.isPlayerOneTurn



    if player1.guessedPairs > player2.guessedPairs:
        print(player1.name + " has won!")
        score = int((player1.guessedPairs / player1.tries) * 100)
        print("~ SCORE of " + player1.name + ": ~\t", score)
    elif player2.guessedPairs > player1.guessedPairs:
        print(player2.name + " has won!")
        score = int((player2.guessedPairs / player2.tries) * 100)
        print("~ SCORE of " + player2.name + ": ~\t", score)
    else:
        if player1.tries > player2.tries:
            print(player2.name + " has won!")
            score = int((player2.guessedPairs / player2.tries) * 100)
            print("~ SCORE of " + player2.name + ": ~\t", score)
        elif player2.tries > player1.tries:
            print(player1.name + " has won!")
            score = int((player1.guessedPairs / player1.tries) * 100)
            print("~ SCORE of " + player1.name + ": ~\t", score)
        else:
            print("This game ended in a draw.")
            score = int((player1.guessedPairs / player1.tries) * 100)
            print("~ SCORE of " + player1.name + ": ~\t", score)
            score = int((player2.guessedPairs / player2.tries) * 100)
            print("\n~ SCORE of " + player2.name + ": ~\t", score)



def main_view_one_player():
    NUM_ROWS = 2
    NUM_COLUMNS = 2
    game_controller = GameController()

    player = Player()
    player.name = input("What is your name?\t")

    game = game_controller.initialize_game_one_player(player, NUM_COLUMNS, NUM_ROWS)

    display_board(game.board)
    while not game.is_game_finished:
        pos1 = ask_position(NUM_COLUMNS, NUM_ROWS)
        pos2 = ask_position(NUM_COLUMNS, NUM_ROWS)
        print("POSITION:\t", pos1)
        print("POSITION2:\t", pos2)
        game_controller.turn_cards(game.board, pos1.x, pos1.y, pos2.x, pos2.y)
        display_board(game.board)
        game_controller.turn_cards(game.board, pos1.x, pos1.y, pos2.x, pos2.y)
        game_controller.play_turn(game, player, pos1.x, pos1.y, pos2.x, pos2.y)

    score = int((game.player.guessedPairs / game.player.tries) * 100)
    print("~ SCORE of " + player.name + ": ~\t", score)


