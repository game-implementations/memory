#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.model.Board import Board
import random


class BoardController:
    def __init__(self):
        pass

    def initialize_board(self, num_rows, num_columns):
        num_cards = num_rows * num_columns
        if num_cards % 2 != 0:
            raise ValueError("The is number of cards is odd change num_rows and num_columns so its multiplication gives pair number.")

        board = Board(num_rows, num_columns)
        deck = []
        for card_value in range(ord('A'), ord('z')):
            deck.append(card_value)
            deck.append(card_value)

            if len(deck) == num_cards:
                break

        for column in range(num_columns):
            for row in range(num_rows):
                board.board[column][row].value = chr(deck.pop(random.randint(0, len(deck) - 1)))

        return board
