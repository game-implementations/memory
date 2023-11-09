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


def main_view():
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
        game_controller.play_turn(game, pos1.x, pos1.y, pos2.x, pos2.y)

    score = int((game.player.guessedPairs / game.player.tries) * 100)
    print("~ SCORE of " + player.name + ": ~\t", score)


