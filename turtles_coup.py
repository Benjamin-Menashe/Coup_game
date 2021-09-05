# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 21:11:49 2021

@author: Benjamin
"""
import random

class coup_zoo:
    def __init__(self,size):
        self.size = size
        self.cur_gen = 0
        self.turtle = [0]*size
        
        for i in range(size):
            self.turtle[i] = self.make_turtle(i)
    
    def make_turtle(self,cage):
        adam = coup_turtle(self.cur_gen)
        for i in range(1440):
            adam.moves_DNA[i] = random.randint(1,9)
        for j in range(2800):
            adam.phase1_DNA[j] = random.randint(0,1)
            adam.phase2_DNA[j] = random.randint(0,1)
            adam.phase3_DNA[j] = random.randint(0,1)
            adam.ID = (self.cur_gen,cage)
        return adam
            
    def birth_turtle(self, dad, mom, mutations=1, amount=50):
        babies = [0]*amount
        for i in range(amount):
            baby = coup_turtle(self.cur_gen+1)
            baby.moves_DNA = self.mix(dad.moves_DNA,mom.moves_DNA,mutations,1440)
            baby.phase1_DNA = self.mix(dad.phase1_DNA,mom.phase1_DNA,mutations,2880)
            baby.phase2_DNA = self.mix(dad.phase2_DNA,mom.phase2_DNA,mutations,2880)
            baby.phase3_DNA = self.mix(dad.phase3_DNA,mom.phase3_DNA,mutations,2880)
            babies[i] = baby
        return babies
            
    def mix(self,mom,dad,mutations,DNA_length):
        new_DNA = [0]*DNA_length
        cuts = [0]+[random.randint(1,DNA_length-1) for i in range(mutations)]
        cuts.sort()
        for i in range(1,len(cuts)):
            if i % 2 == 1:
                new_DNA[cuts[i-1]:cuts[i]] = dad[cuts[i-1]:cuts[i]]
            else:
                new_DNA[cuts[i-1]:cuts[i]] = mom[cuts[i-1]:cuts[i]]
        return new_DNA
        
class coup_turtle:
    def __init__(self,gen=0):
        self.gen = gen
        self.ID = 0
        self.games = 0
        self.wins = 0
        self.moves_DNA = [0]*1440
        self.phase1_DNA = [0]*2880
        self.phase2_DNA = [0]*2880
        self.phase3_DNA = [0]*2880
        
    def calc_move(self,state):
        move = 0
        return move
    
    
zoo = coup_zoo(1000)

