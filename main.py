# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:23:32 2021

@author: Benjamin
"""

## Coup Main


from gameplay import Game

def play_coup():
    game = Game()
    print('Welcome to Coup! The availible moves are:')
    print(game.move_dict)
    ticker = 0
    while game.winner == 0 and ticker < 60:
        if ticker % 3 == 0:
            print('The current cards are:')
            game.player_state[0].show_cards()
            game.player_state[1].show_cards()
            game.player_state[2].show_cards()
        print('The game status is:')
        estr0 = game.player_state[0].name+' lives='+str(game.player_state[0].lives)+' coins='+str(game.player_state[0].coins)
        estr1 = game.player_state[1].name+' lives='+str(game.player_state[1].lives)+' coins='+str(game.player_state[1].coins)
        estr2 = game.player_state[2].name+' lives='+str(game.player_state[2].lives)+' coins='+str(game.player_state[2].coins)
        print(estr0 + ' | ' + estr1 + ' | ' + estr2)
        game.get_moves()
        game.consolidate()
        ticker += 1
    print('Good game! Play again?')
    
play_coup()