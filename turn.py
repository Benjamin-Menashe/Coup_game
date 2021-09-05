# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 22:57:14 2021

@author: Benjamin
"""

class Turn_Kernel:
    def __init__(self):
        self.moves = [0]*3
        self.phases1 = [False]*3
        self.phases2 = [False]*3
        self.phases3 = [False]*3
        self.kernels_dict = {
            000000:0,
            100000:1,
            200000:2,
            300000:3,
            400000:4,
            500000:5,
            600000:6,
            700000:7,
            800000:8,
            900000:9,
            200100:10,
            200010:11,
            200101:12,
            200011:13,
            510000:14,
            501000:15,
            610000:16,
            601000:17,
            600100:18,
            600101:19,
            710000:20,
            701000:21,
            700010:22,
            700011:23,
            810000:24,
            801000:25,
            800100:26,
            800101:27,
            910000:28,
            901000:29,
            900010:30,
            900011:31}
        
    def restart(self): # just in case there is corruption
        self.moves = [0]*3
        self.phases1 = [False]*3
        self.phases2 = [False]*3
        self.phases3 = [False]*3
        
    def make_list(self,p): # turn the kernel into int
        t1 = (p + 1) % 3 # for player to the left
        t2 = (p + 2) % 3 # for player to the right
        x = str(self.moves[p])+ \
        str(int(self.phases1[t1]))+str(int(self.phases1[t2]))+ \
        str(int(self.phases2[t1]))+str(int(self.phases2[t2]))+ \
        str(int(self.phases3[p]))
        self.list = int(x)
        return self.list
        
    def kernel_ID(self,p): # turn the int into shorter int
        i = self.make_list(p)
        self.ID = self.kernels_dict[i]
        return self.ID
        
# a = Turn_Kernel()
# a.moves[0] = 7
# print(a.make_list())
# print(a.kernel_ID())       
    