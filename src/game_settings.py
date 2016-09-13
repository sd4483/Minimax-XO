"""
 * Copyright (C) 2016 root
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

class game_settings(object):
    
    
    ############################## Variables ###################################

    #the winning combos in all directions
    winning_combos = ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6])

    winners = ('X-win', 'Draw', 'O-win')


    ############################## Constructor #################################

    def __init__(self, squares=[]):
        
        #Creates an empty board
        if len(squares) == 0:
            self.squares = [None for i in range(9)]
        else:
            self.squares = squares
    

    ############################## Functions ###################################


    """
    Shows the board : loop inside the array of squares and print each square
    """
    def show_board(self):
        
        for element in [self.squares[i:i + 3] for i in range(0, len(self.squares), 3)]:
            print element

    """
    Computes the available moves : by knowing if a square is filled or not
    """
    def available_moves(self):
        return [k for k, v in enumerate(self.squares) if v is None]

    """
    Checks is the game over : by knowing if number of unfilled squares == 0
    """
    def complete_board(self):
        if None not in [v for v in self.squares]:
            return True
        if self.winner() != None:
            return True
        return False


    """
    Checks who won : by knowing combos made
    """
    def winner(self):
        for player in ('X', 'O'):
            positions = self.get_all_squares(player)
            for combo in self.winning_combos:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player
        return None

    """
    gets all squares of a player
    """
    def get_all_squares(self, player):
        return [k for k, v in enumerate(self.squares) if v == player]


    """
    makes the next move
    """
    def make_move(self, position, player):
        self.squares[position] = player
    
        
    """
    Three functions to state the game's result
    """
    def X_won(self):
        return self.winner() == 'X'

    def O_won(self):
        return self.winner() == 'O'

    def tied(self):
        return self.complete_board() == True and self.winner() is None

    """
    state the enemy symbol
    """
    def set_enemy(self, player):
        if player == 'X':
            return 'O'
        return 'X'

