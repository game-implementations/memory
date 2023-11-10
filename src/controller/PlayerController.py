#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.model.Player import Player
from src.model.Position import Position


class PlayerController:
    def __init__(self):
        pass

    def initialize_players(self, num_players):
        players = []
        for _ in range(num_players):
            player = Player()
            player.name = input(f"Enter the name for Player {_ + 1}: ")
            players.append(player)
        return players

    def display_player_turn(self, player):
        print(f"~ {player.name}'s turn ~")

    def display_winner(self, winner):
        print(f"{winner.name} has won!")

    def display_draw(self):
        print("This game ended in a draw.")

    def display_score(self, player):
        score = int((player.guessedPairs / player.tries) * 100)
        print(f"~ SCORE of {player.name}: ~\t", score)

    def ask_position(self, num_columns, num_rows):
        pos = Position()
        col_letter = input("Please write column letter:\t")
        col_letter = col_letter.upper()
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
