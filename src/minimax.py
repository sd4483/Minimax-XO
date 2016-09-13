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

import random
from game_settings import game_settings


class minimax(object):

    board = game_settings()
    
    """
    Alpha-Beta Purring Algorithm is an optimized version of minimax that discards worst conditions to save computational power.

    runs recursively through all available blocks and chooses the best one then return it to the program..

    for each move, after the recursion it proceeds to the comparison to define the best move

    """
    def alphabeta(self, node, player, alpha, beta):
        
	#If the board is complete, determine the winner of the recursion
        if node.complete_board():

            if node.X_won():
                return -1
            elif node.tied():
                return 0
            elif node.O_won():
                return 1

        else :

            for move in node.available_moves():

	        #the computer plays against himself virtually to determine best move
                node.make_move(move, player)
                val = self.alphabeta(node, self.board.set_enemy(player), alpha, beta)
                node.make_move(move, None)
                	
		#Calculating best location for this move
                if player == 'O':
                    if val > alpha:
                        alpha = val
                    if alpha >= beta:
                        return beta
                else:
                    if val < beta:
                        beta = val
                    if beta <= alpha:
                        return alpha

            #Return the result
            if player == 'O':
	        return alpha
            else:
                return beta
                
    """
    This determines the next move using some hard-coded rules and minimax algorithm
    """
    def determine(self, board, player):

        a = -2
        choices = []
        
	#Plays at corner if no move was made yet
        if len(board.available_moves()) == 9:
            return 4

        #loops through available places 
        for move in board.available_moves():
            
	    #the computer plays against himself virtually to determine best move
            board.make_move(move, player)
            val = self.alphabeta(board, board.set_enemy(player), -2, 2)
            board.make_move(move, None)

	    #Determine the next move
            if val > a:
                a = val
                choices = [move]
            elif val == a:
                choices.append(move)

        #if more than one possible optimum move, choose one randomly      
        return random.choice(choices) 


