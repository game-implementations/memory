#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.controller.BoardController import BoardController
from src.model.OnePlayerGame import OnePlayerGame
from src.model.TwoPlayersGame import TwoPlayersGame


class GameController:
    def __init__(self):
        self.boardController = BoardController()

    def play_turn(self, game, player, x1, y1, x2, y2):
        player.tries += 1
        if game.board.board[x1][y1].isPaired or game.board.board[x2][y2].isPaired:
            return False
        if self.boardController.is_same_card(game.board, x1, y1, x2, y2):
            game.board.board[x1][y1].isPaired = True
            game.board.board[x2][y2].isPaired = True
            player.guessedPairs += 1
            game.is_game_finished = self.boardController.is_board_finished(game.board)
            return True
        else:
            return False

    def initialize_game_one_player(self, player, num_columns, num_rows):
        game = OnePlayerGame(player, num_columns, num_rows)
        game.board = self.boardController.initialize_board(num_columns, num_rows)
        return game
    
    def initialize_game_two_players(self, player1, player2, num_columns, num_rows):
        game = TwoPlayersGame(player1, player2, num_columns, num_rows)
        game.board = self.boardController.initialize_board(num_columns, num_rows)
        return game

    def turn_cards(self, board, x1, y1, x2, y2):
        self.boardController.turn_cards(board, x1, y1, x2, y2)
