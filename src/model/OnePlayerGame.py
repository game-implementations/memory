#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.model.Game import Game


class OnePlayerGame(Game):
    def __init__(self, player, num_rows, num_columns):
        super().__init__(num_rows, num_columns)
        self.player = player
