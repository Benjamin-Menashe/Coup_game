# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 16:04:05 2021

@author: Benjamin
"""
from random import shuffle
from player import Player
from turn import Turn_Kernel

class Game:
    def __init__(self):
        self.players = {0,1,2} # ID of players
        self.deaths = 0 # number of dead players
        self.winner = 0 # name of winner
        self.cur_player = 0 # whose turn it is [0,1,2]
        self.turns = 0
        self.kernels = [0]*60 # 60 empty slots for turns
        
        self.deck = ['CAPTAIN','CONTESSA','DUKE','ASSASSIN']*3 # deck
        self.shuffle()
        
        self.player_state = [Player(p, self.deck) for p in self.players] # start game by adding players and giving cards
        
        self.cur_phase = 0 # turn phases are:
        # 0: cur_player makes move.
        # 1: option to challenge.
        # 2: option to block (if unchallanged and blockable).
        # 3: option to challenge block (if blocked).
        
        # moves, card, and blocks dictionaries
        self.move_dict = {
            0: 'NoMove',
            1: 'Income',
            2: 'ForeignAid',
            3: 'CoupL',
            4: 'CoupR',
            5: 'Tax',
            6: 'AssassinateL',
            7: 'AssassinateR',
            8: 'StealL',
            9: 'StealR'}
        self.card_dict = {
            5: 'DUKE',
            6: 'ASSASSIN',
            7: 'ASSASSIN',
            8: 'CAPTAIN',
            9: 'CAPTAIN'}
        self.block_dict = {
            2: 'DUKE',
            6: 'CONTESSA',
            7: 'CONTESSA',
            8: 'CAPTAIN',
            9: 'CAPTAIN'}
        
    def shuffle(self): # shuffle deck
        shuffle(self.deck)
        
    def next_turn(self): # next turn
        self.death_check()
        self.turns += 1
        self.cur_player = (self.cur_player + 1) % 3
        
    def get_moves(self):
        
        self.cur_kernel = Turn_Kernel() # make new kernel
        self.cur_kernel.restart()
                
        p = self.cur_player
        t1 = (p + 1) % 3 # for player to the left
        t2 = (p + 2) % 3 # for player to the right
        
        if self.player_state[p].lives == 0: # check death
            pass       
        else:
            cur_move = self.player_state[p].calc_move(self) # player selects their move and changes kernel
            if cur_move in [3,6,8] and self.player_state[t1].dead: # check for targeting dead players
                print('Targeted a dead player. Changing to target the other player...')
                cur_move += 1
            if cur_move in [4,7,9] and self.player_state[t2].dead:
                print('Targeted a dead player. Changing to target the other player...')
                cur_move += -1
            self.cur_kernel.moves[p] = cur_move            
            
            trg_str = ''
            if cur_move in [3,6,8]:
                trg_str = ' targeting ' + self.player_state[t1].name
            elif cur_move in [4,7,9]:
                trg_str = ' targeting ' + self.player_state[t2].name
            
            print(self.move_dict[cur_move] + trg_str) # print move to show everybody
                
            if cur_move in [6,7]: # Assassinate lose coins no matter what happens later
                self.player_state[p].add_coins(-3)

            if cur_move in [5,6,7,8,9]: # check if anyone calls bluff (left player then right player)
                if self.player_state[t1].lives != 0:
                    self.cur_kernel.phases1[t1] = self.player_state[t1].calc_phase1(self,cur_move)
                if self.cur_kernel.phases1[t1] == 0 and self.player_state[t2].lives != 0:
                    self.cur_kernel.phases1[t2] = self.player_state[t2].calc_phase1(self,cur_move)        
            
            if self.cur_kernel.phases1 == [False]*3: # check if target blocks
                if cur_move in [2,6,8] and self.player_state[t1].lives > 0:
                    self.cur_kernel.phases2[t1] = self.player_state[t1].calc_phase2(self,cur_move)     
                if cur_move in [2,7,9] and self.player_state[t2].lives > 0 and self.cur_kernel.phases2[t1] == 0:
                    self.cur_kernel.phases2[t2] = self.player_state[t2].calc_phase2(self,cur_move)
                    
                if self.cur_kernel.phases2 != [False]*3: # check if player calls bluff on the block
                    self.cur_kernel.phases3[p] = self.player_state[p].calc_phase3(self,cur_move)       
                    
        self.kernels[self.turns] = self.cur_kernel.kernel_ID(p)
    
    # Conclusions:
    def consolidate(self):
    
        p = self.cur_player
        t1 = (p + 1) % 3 # for player to the left
        t2 = (p + 2) % 3 # for player to the right
        
        cur_move = self.cur_kernel.moves[p]
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
                        if cur_move==2:
                            target = self.cur_kernel.phases2.index(True)
                        claim2 = self.block_dict[cur_move]   
                        self.bluff_protocol(self.player_state[p],self.player_state[target],claim2)
                    else: # no bluff on the block - successful block
                        self.no_move()
                else: # there is no block and no bluff - successful attack
                    if cur_move == 2: # Foreign Aid
                        self.player_state[p].add_coins(2)
                        self.next_turn()
                    elif cur_move in [6,7]: # Assassinate
                        self.deck.append(self.player_state[target].rm_card())
                        self.shuffle()
                        self.next_turn()
                    elif cur_move in [8,9]: # Steal
                        d = 2
                        if self.player_state[target].coins < 2:
                            d = self.player_state[target].coins
                        self.player_state[p].add_coins(d)
                        self.player_state[target].add_coins(-d)
                        self.next_turn()
            elif cur_move == 1: #Income
                self.player_state[p].add_coins(1)
                self.next_turn()
            elif cur_move == 5: # tax
                self.player_state[p].add_coins(3)
                self.next_turn()
            elif cur_move in [3,4]: # coup
                self.player_state[p].add_coins(-7)
                self.deck.append(self.player_state[target].rm_card())
                self.shuffle()
                self.next_turn()
        else: # someone called bluff
            claim1 = self.card_dict[cur_move]
            offense = self.cur_kernel.phases1.index(True) # who called bluff first
            self.bluff_protocol(self.player_state[offense],self.player_state[p],claim1)
            
    def bluff_protocol(self,offense,defense,card):
        if defense.have_card(card):
            print('no bluff! '+defense.name+' has '+card+'!')
            self.switch_card(defense,card)
            self.deck.append(offense.rm_card())
            self.shuffle()
            self.cur_kernel.phases1 = [False]*3
            self.cur_kernel.phases3 = [False]*3
            self.consolidate()
        else:
            print(defense.name + ' was bluffing!')
            self.deck.append(defense.rm_card())
            self.shuffle
            if self.cur_kernel.phases3[self.cur_player]: # if it was bluff the block then restart without block
                self.cur_kernel.phases2 = [False]*3
                self.cur_kernel.phases3 = [False]*3
                self.consolidate()
            else: # if it was bluff on the original move just move to next turn
                self.next_turn()
        
    def no_move(self):
        self.next_turn()
    
    def switch_card(self,player,card):
        c = player.card.index(card)
        self.deck.append(player.card[c])
        self.shuffle()
        player.card[c] = self.deck.pop()
        
    def death_check(self):
        statii = [self.player_state[i].dead for i in range(3)]
        self.deaths = sum(statii)
        if self.deaths == 2:
            self.winner = self.player_state[statii.index(False)].name
            lives = self.player_state[statii.index(False)].lives
            print(self.winner+' has won the game with '+str(lives)+' lives left')
        
