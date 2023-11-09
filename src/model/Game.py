#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.model.Board import Board


class Game:
    def __init__(self, num_columns, num_rows):
        self.duration = 0
        self.board = Board(num_columns, num_rows)
        self.is_game_finished = False


