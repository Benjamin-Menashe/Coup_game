# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 15:38:26 2021

@author: Benjamin
"""

class Player:
    def __init__(self, number, deck):
        self.name = 'Player' + str(number) #  unique IDs
        
        self.coins = 2 # coins per player
        
        self.lives = 2 # cards per player
        self.card = []
        self.card[1:2] = [deck.pop(), deck.pop()]
        
        self.dead = False
        
        self.move = 0
        self.phase1 = False
        self.phase2 = False
        self.phase3 = False
        
    def calc_move(self, game):
        self.move = int(input(self.name + ' pick a move [0,9]:'))
        if self.coins >= 10 and self.move not in [3,4]:
            print(self.name + ' has 10+ coins, must select coup [3/4]')
            self.move = int(input(self.name + ' pick a coup [3/4]:'))
        if self.move in [3,4] and self.coins < 7: # coin check
            print('Not enough coins for coup. Turn over')
            self.move = 0
        if self.move in [6,7] and self.coins < 3: # coin check
            print('Not enough coins for Assassination. Turn over')
            self.move = 0           
        return self.move

    def calc_phase1(self, game, move):
        marker = input(self.name + ' bluff? [y/n]:')
        if marker == 'y':
            self.phase1 = True
        else:
            self.phase1 = False
        return self.phase1
            
    def calc_phase2(self, game, move):
        marker = input(self.name + ' block? [y/n]:')
        if marker == 'y':
            self.phase2 = True
        else:
            self.phase2 = False
        return self.phase2
        
    def calc_phase3(self, game, move):
        marker = input(self.name + ' bluff the block? [y/n]:')
        if marker == 'y':
            self.phase3 = True
        else:
            self.phase3 = False
        return self.phase3
            
    # modifiers based on conclusions        
    def add_coins(self,number):
        self.coins += number
        
    def rm_card(self):
        if self.lives == 2:
            c = int(input(self.name + ' pick a card to remove [0/1]: '))
            away = self.card[c]
            if c == 0:
                self.card[0] = self.card[1]
            self.card[1] = []
        elif self.lives == 1:
            away = self.card[0]
            self.card[0] = []
            self.dead = True
            print(self.name + ' had no more cards left and IS DEAD!')
        self.lives += -1
        return away
        
        
    def have_card(self,claim):
        if claim in self.card:
            return True
        return False
    
    def show_cards(self):
        print(self.card)

