# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 20:51:36 2021

@author: Benjamin
"""

# DNA code interpertation:
    # _2_ my lives {1,2}
    # _8_ player1 + player2 lives {01,02,10,11,12,20,21,22}
    # _3_ my coins {0-2,3-6,7+}
    # _3_ player1 coins {0-2,3-6,7+}
    # _3_ player2 coins {0-2,3-6,7+}
    # _10_ my cards {ASSASSIN+NULL, ASSASSIN+DUKE, ASSASSIN+CAPTAIN, ASSASSIN+CONTESSA
    #                DUKE+NULL, DUKE+CAPTAIN, DUKE+CONTESSA,
    #                CAPTAIN+NULL, CAPTAIN+CONTESSA
    #                CONTESSA+NULL} where NULL = same or none
    
    # for bluffing, blocking, bluffing the block
    # _2_ who moved, attacked, blocked me {player1,player2}