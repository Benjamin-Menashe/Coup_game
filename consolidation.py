# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 10:10:39 2021

@author: Benjamin
"""

# conclusions and scenerios

def consolidate(self):
    
    p = self.cur_player
    t1 = (p + 1) % 3 # for player to the left
    t2 = (p + 2) % 3 # for player to the right
    
    cur_move = self.kernel.moves[p]
    if cur_move in [3,6,8]:
        target = t1
    elif cur_move in [4,7,9]:
        target = t2
        
    if cur_move == 0:
        self.no_move()
        
    elif self.cur_kernel.phases1 == [False]*3: # if no bluff is called
        if cur_move in [2,6,7,8,9]: # blockable moves
            if self.cur_kernel.phases2 != [False]*3: # there is a block
                if self.cur_kernel.phases3 != [False]*3: # the block is bluffed
                    claim2 = self.block_dict[cur_move]  
                    self.bluff_protocol(self.player_state[p],self.player_state[target],claim2)
                    self.next_turn()
                else: # no bluff on the block - successful block
                    self.no_move()
            else: # there is no block and no bluff - successful attack
                if cur_move == 2: # Foreign Aid
                    self.player_state[p].add_coins(2)
                    self.next_turn()
                elif cur_move in [6,7]: # Assassinate
                    self.player_state[p].add_coins(-3)
                    self.player_state[target].rm_card()
                    self.next_turn()
                elif cur_move in [8,9]: # Steal
                    self.player_state[p].add_coins(2)
                    self.player_state[target].add_coins(-2)
                    self.next_turn()
        elif cur_move == 1: #Income
            self.player_state[p].add_coins(1)
            self.next_turn()
        elif cur_move == 5: # tax
            self.player_state[p].add_coins(3)
            self.next_turn()
        elif cur_move in [3,4]: # coup
            self.player_state[p].add_coins(-7)
            self.player_state[target].rm_card()
            self.next_turn()
    else: # someone called bluff
        claim1 = self.card_dict[cur_move]
        offense = self.cur_kernel.phases1.index(True) # who called bluff first
        self.bluff_protocol(self.player_state[offense],self.player_state[p],claim1)
        self.next_turn()
        
def bluff_protocol(self,offense,defense,card):
    if defense.have_card(card):
        print('no bluff! '+defense.name+' has '+card+'!')
        self.switch_card(defense,card)
        offense.rm_card()
        self.cur_kernel.phases1 = [False]*3
        self.cur_kernel.phases3 = [False]*3
        self.consolidate()
    else:
        print(defense.name + ' was bluffing!')
        defense.rm_card()
        