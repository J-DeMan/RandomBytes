''' 
   Simple AI #2
   Jerrett DeMan
'''
# Imports the base class for AI player
from ZDengine import ZDPlayer


from random import randint

'''
    Access and manipulation of n_win and rank is strictly forbidden. You may create as many methods 
    as needed. However, the only method that will be called by the tournament is Play().
    
    Name both your file with the pattern: zd_yourname_ainame.py (file name), zd_yourname_ainame (Class name)
'''
class zd_Jerrett_DeMan_Dave(ZDPlayer):
    # must begin with zd_
    name = 'zd_Jerrett_DeMan_Dave'
    # Specify a division (Use the most specific)
    # Division 1 : less than 20 unergraduate courses in computer science/informatics
    # DIvision 2 : All undergraduate students
    # Division 3 : General category (Graduates, Graduate students, etc.) 
    division = 1
    
    ## Division to be entered in (select the most specific)
    #  Division 1: less than 20 completed courses in CSCI/INFX
    #  Division 2: All Undergraduate students (Includes Div 1)
    #  Division 3: All human beings (include Div 2, Graduates, graduate students, faculty and staff)
    division = 1
    
    def __init__(self):
        ZDPlayer.__init__(self)
        
    def Play(self, player_id, tallies, hand, cup, n_brain, n_shotgun):
        '''
            The method called by the game to query a decision from the AI.
            INPUT:
               player_id (int) - the index in tallies of the AI player.
               tallies (list of list of int) - List of scores from rounds for all players.
               hand - (List of string) - List of dice in hand, coded by color (R,G,Y)
               cup - (list of string) - Similar to hand, but for what is left in the cup
               n_brain - (int) Current number of brains on the table
               n_shotgun - (int) Current number of shotgun on the table.
            OUTPUT:
               True - (bool) Proceed with another round of dice rolling
               False - (bool) Cash in the brains and end the turn
               
            STRATEGY:
               ...
         '''
        if n_brain == 0:
            return True
        if n_shotgun <= 1:
            return True
        return False
