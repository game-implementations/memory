#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.model.Card import Card


class Board:
    def __init__(self, num_rows, num_columns):
        self.board = []

        for _ in range(num_columns):
            column_content = []
            for _ in range(num_rows):
                column_content.append(Card(""))
            self.board.append(column_content)
