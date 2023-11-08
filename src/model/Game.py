#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Board import Board


class Game:
    def __init__(self, num_rows, num_columns):
        self.duration = 0
        self.board = Board(num_rows, num_columns)

