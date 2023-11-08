#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.controller.BoardController import BoardController


def display_board_raw(board):
    msg = ""
    for row in range(len(board.board)):
        for column in range(len(board.board[row])):
            msg += str(board.board[column][row].value)
        msg += "\n"
    print(msg)


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
            if board.board[column][r].isTurnedUp:
                msg += str(board.board[column][r].value)
            else:
                msg += "#"
        msg += "\n"
    print(msg)


def main_view():
    board_controller = BoardController()
    board = board_controller.initialize_board(4, 4)
    display_board(board)
