#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Game import Game


class OnePlayerGame(Game):
    def __init__(self, num_rows, num_columns):
        super().__init__(num_rows, num_columns)
