# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 15:20:08 2021

@author: Benjamin
"""

## Pseudocode

# 1. Game state:
    # a. deck info
    # b. turn
    # c. phase
    # d. players

# 2. Player state:
    # a. no_cards
    # b. cards
    # c. coins
    # d. phase1: move & target
    # e. phase2: bluff or not
    # f. phase3: block or not
    # g. phase4: bluff or not
    
# 3. list of moves:
    # a. move:
        # 0. 0
        # 1. income
        # 2. foreignAid
        # 3. coupL
        # 4. coupR
        # 5. tax
        # 6. assassinateL
        # 7. assassinateR
        # 8. stealL
        # 9. stealR
    # b. phase1:
        # 0. bluff
    # c. phase2: block
        # 0. 0
        # 1. block foreign aid (with DUKE)
        # 2. block steal (with CAPTAIN)
        # 3. block assassination (with CONTESSA)
    # d. phase3:
        # 0. bluff on block

# 4. set up game: shuffle cards and divide to players.

# 5. gameplay:
    # a. phase1: cur_player makes move, others return 0.
    # b. phase2: cur_player 0, others {0 or bluff}
    # c. phase3: cur_player 0, target {0 or block}
    # d. phase4: target 0, others {0 or bluff}
    # e. clean up and update game state, player states
    # f. next turn
    
    
    