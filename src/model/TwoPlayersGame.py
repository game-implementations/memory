#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.model.Game import Game


class TwoPlayersGame(Game):
    def __init__(self, player_one, player_two, num_rows, num_columns):
        super().__init__(num_rows, num_columns)
        self.isPlayerOneTurn = True
        self.playerOne = player_one
        self.playerTwo = player_two
