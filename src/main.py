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

from game_settings import game_settings
from minimax import minimax
import os
from sys import platform as _platform


x = 0
player_score = 0
computer_score = 0

print "\n============== AI Tic Tac Toe ===============\n"
print "\n"
print "The XO Bot that will kick your ass"
print "\nDesigned by Alpa-Beta purring algorithm"


raw_input("\nPress Enter to continue...")


#Clears Screen to get ready
if _platform == "linux" or _platform == "linux2":
    # linux
    os.system('clear') 
elif _platform == "darwin":
    # MAC OS X
    os.system('clear') 
elif _platform == "win32":
    # Windows
    os.system('cls') 



while True:
    
    board = game_settings()
    
    if not x > 0:
        minimax = minimax()
        print "\n============== Round 1 ===============\n"
    
    else: 
        print "\n============== Round", x + 1, "===============\n"
 

    board.show_board()

    while not board.complete_board():
        player = 'X'
        player_movee = raw_input("\nNext Move: ")

        ####################################

        if player_movee.isdigit():
            player_move = int(player_movee) - 1
        else:
            print "\n -- Error :: Invalid Input , Game Terminated -- "
            break
            
        if not player_move in board.available_moves():
            print "\n-- Error :: Invalid Move, Try Again -- "
            continue
            
        ####################################
            
        
        print "\n======== You Played ========\n"
        
        board.make_move(player_move, player)
        print ""  
        board.show_board()
        
        print "\n======== I played ========\n"

        ####################################
        
        if board.complete_board():
            break

        player = board.set_enemy(player)
        computer_move = minimax.determine(board, player)
        board.make_move(computer_move, player)
        print ""    
        board.show_board()
        
    print ""    
    print "Winner : ", board.winner()
    
    #Workaround to prevent failure, also round counter
    x = x + 1
    
    if board.winner() == 'X':
        print "Score : Player => ", player_score + 1, " ", "AI => ", computer_score
    elif board.winner() == '0': 
        print "Score : Player => ", player_score, " ", "AI => ", computer_score + 1
    else: 
        print "Score : Player => ", player_score, " ", "AI => ", computer_score
    
    ####################################

    print "\n"
    answer = raw_input("\n Do you want to play again? (y/n) ")
    
    if answer == "n":
	print "\nThanks for playing, human.."
        
        print "\n\nFinal Score : \n\n"
        print "Player => ", player_score, "\n", "AI => ", computer_score

    	os._exit(1)
    else: 
	print "\nHere we go, mortal.."


