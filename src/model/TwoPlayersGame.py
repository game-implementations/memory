#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Game import Game
from Player import Player


class TwoPlayersGame(Game):
    def __init__(self, num_rows, num_columns):
        super().__init__(num_rows, num_columns)
        self.isPlayerOneTurn = True
        self.playerOne = Player()
        self.playerTwo = Player()
