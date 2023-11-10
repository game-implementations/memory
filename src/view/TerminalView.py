#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.controller.GameController import GameController
from src.controller.PlayerController import PlayerController


def display_board_raw(board):
    msg = ""
    for row in range(len(board.board)):
        for column in range(len(board.board[row])):
            msg += str(board.board[column][row].value)
        msg += "\n"
    print(msg)


def display_board(board):
    msg = ""

    row_letters = ""

    for row_number in range(len(board.board)):
        row_letters += chr(ord('A') + row_number)

    msg += "  " + row_letters + "\n"

    row_number = 1
    for r in range(len(board.board)):
        msg += str(row_number) + " "
        row_number += 1
        for column in range(len(board.board[r])):
            if board.board[column][r].isPaired:
                msg += " "
            elif board.board[column][r].isTurnedUp:
                msg += str(board.board[column][r].value)
            else:
                msg += "#"
        msg += "\n"
    print(msg)


def main_view_two_players():
    NUM_ROWS = 2
    NUM_COLUMNS = 2
    game_controller = GameController()
    player_controller = PlayerController()

    players = player_controller.initialize_players(2)

    game = game_controller.initialize_game_two_players(players[0], players[1], NUM_COLUMNS, NUM_ROWS)

    display_board(game.board)
    while not game.is_game_finished:
        current_player = game.player_one if game.is_player_one_turn else game.player_two
        player_controller.display_player_turn(current_player)

        pos1 = player_controller.ask_position(NUM_COLUMNS, NUM_ROWS)
        pos2 = player_controller.ask_position(NUM_COLUMNS, NUM_ROWS)
        game_controller.turn_cards(game.board, pos1.x, pos1.y, pos2.x, pos2.y)
        display_board(game.board)
        game_controller.turn_cards(game.board, pos1.x, pos1.y, pos2.x, pos2.y)
        is_success = False
        if game.is_player_one_turn:
            is_success = game_controller.play_turn(game, players[0], pos1.x, pos1.y, pos2.x, pos2.y)
            if is_success:
                print("The player one " + players[0].name + " has guessed a pair. It is his turn again.")
        else:
            is_success = game_controller.play_turn(game, players[1], pos1.x, pos1.y, pos2.x, pos2.y)
            if is_success:
                print("The player two " + players[1].name + " has guessed a pair. It is his turn again.")

        if not is_success:
            game.is_player_one_turn = not game.is_player_one_turn

    if players[0].guessedPairs > players[1].guessedPairs:
        player_controller.display_winner(players[0])
        player_controller.display_score(players[0])
    elif players[1].guessedPairs > players[0].guessedPairs:
        player_controller.display_winner(players[1])
        player_controller.display_score(players[1])
    else:
        if players[0].tries > players[1].tries:
            player_controller.display_winner(players[1])
            player_controller.display_score(players[1])
        elif players[1].tries > players[0].tries:
            player_controller.display_winner(players[0])
            player_controller.display_score(players[0])
        else:
            player_controller.display_draw()
            player_controller.display_score(players[1])
            player_controller.display_score(players[0])


def main_view_one_player():
    NUM_ROWS = 2
    NUM_COLUMNS = 2
    game_controller = GameController()
    player_controller = PlayerController()

    player = player_controller.initialize_players(1)[0]

    game = game_controller.initialize_game_one_player(player, NUM_COLUMNS, NUM_ROWS)

    display_board(game.board)
    while not game.is_game_finished:
        pos1 = player_controller.ask_position(NUM_COLUMNS, NUM_ROWS)
        pos2 = player_controller.ask_position(NUM_COLUMNS, NUM_ROWS)
        print("POSITION:\t", pos1)
        print("POSITION2:\t", pos2)
        game_controller.turn_cards(game.board, pos1.x, pos1.y, pos2.x, pos2.y)
        display_board(game.board)
        game_controller.turn_cards(game.board, pos1.x, pos1.y, pos2.x, pos2.y)
        game_controller.play_turn(game, player, pos1.x, pos1.y, pos2.x, pos2.y)

    player_controller.display_score(player)


