from pacman import runGames
from game import GameStateData
from game import Game
from game import Directions
from game import Actions
from util import nearestPoint
from util import manhattanDistance
import util, layout
import sys, types, time, random, os
from multiAgents import MinimaxAgent
from pacman import readCommand


# ##################
# #LEVEL 1 :
# ##############
# for nbr in range(1,4):
# 	if (nbr == 3):
# 		nbr = 4
# 	nbr = str(nbr)
# 	agent = 'MinimaxAgent'
# 	depth = 'depth='+ nbr
#
# 	for turn in range(1,6):
# 		args = readCommand( ['-g','RandomGhost','-p', agent, '-l', 'mediumClassic', '-a', depth,'-k','1'])
# 		print('Intento: ', turn ,' Algoritmo: ', agent,' Profundidad: ', depth, ' Nivel: 1', )
#
# 		runGames( **args )
#
# for nbr in range(1,4):
# 	if (nbr == 3):
# 		nbr = 4
# 	nbr = str(nbr)
# 	agent = 'AlphaBetaAgent'
# 	depth = 'depth='+ nbr
#
# 	for turn in range(1,6):
# 		args = readCommand( ['-g','RandomGhost','-p', agent, '-l', 'mediumClassic', '-a', depth,'-k','1'])
# 		print('Intento: ', turn ,' Algoritmo: ', agent,' Profundidad: ', depth, ' Nivel: 1', )
#
# 		runGames( **args )

##################
#LEVEL 2 :
##############
# print( "-----------------")
# print( " ---- NIVEL 2 !! ------ ")
# print ("------------------")
# for nbr in range(1,4):
# 	if (nbr == 3):
# 		nbr = 4
# 	nbr = str(nbr)
#
# 	depth = 'depth='+ nbr
#
# 	for difAgent in range(1,3):
# 		if(difAgent == 1):
# 			agent = 'MinimaxAgent'
# 		if(difAgent == 2):
# 			agent = 'AlphaBetaAgent'
# 		print(" ------- New Box: ----------")
# 		for turn in range(1,6):
# 			args = readCommand( ['-g','DirectionalGhost','-p', agent, '-l', 'mediumClassic', '-a', depth,'-k','1'])
# 			print('Intento: ', turn ,' Algoritmo: ', agent,' Profundidad: ', depth, ' Nivel: 2', )
#
# 			runGames( **args )

#################
#Missing from LEVEL 2 :
#############
# print( "-----------------")
# print( " ---- NIVEL 2, depht = 4 !! ------ ")
# print ("------------------")
#
# if(True):
# 	nbr = 4
# 	nbr = str(nbr)
#
# 	depth = 'depth='+ nbr
#
# 	for difAgent in range(1,3):
# 		if(difAgent == 1):
# 			agent = 'MinimaxAgent'
# 		if(difAgent == 2):
# 			agent = 'AlphaBetaAgent'
# 		print(" ------- New Box: ----------")
# 		for turn in range(1,6):
# 			args = readCommand( ['-g','DirectionalGhost','-p', agent, '-l', 'mediumClassic', '-a', depth,'-k','1'])
# 			print('Intento: ', turn ,' Algoritmo: ', agent,' Profundidad: ', depth, ' Nivel: 2', )
#
# 			runGames( **args )
#

##################
#LEVEL 3 :
##############
# print( "-----------------")
# print( " ---- NIVEL 3 !! ------ ")
# print ("------------------")
# for nbr in range(1,4):
# 	if (nbr == 3):
# 		nbr = 4
# 	nbr = str(nbr)
#
# 	depth = 'depth='+ nbr
#
# 	for difAgent in range(1,3):
# 		if(difAgent == 1):
# 			agent = 'MinimaxAgent'
# 		if(difAgent == 2):
# 			agent = 'AlphaBetaAgent'
# 		print(" ------- New Box: ----------")
# 		for turn in range(1,6):
# 			args = readCommand( ['-g','RandomGhost','-p', agent, '-l', 'mediumClassic', '-a', depth,'-k','3'])
# 			print('Intento: ', turn ,' Algoritmo: ', agent,' Profundidad: ', depth, ' Nivel: 3', )
#
# 			runGames( **args )

#('Intento: ', 1, ' Algoritmo: ', 'AlphaBetaAgent', ' Profundidad: ', 'depth=4', ' Nivel: 3')


##################
# Falta de LEVEL 3 :
#depth = 4, AlphaBetaAgent
##############
#
# if (True):
# 	nbr = 4
# 	nbr = str(nbr)
#
# 	depth = 'depth='+ nbr
#
# 	if(True):
# 		agent = 'AlphaBetaAgent'
#
# 		print(" ------- New Box: ----------")
# 		for turn in range(1,6):
# 			args = readCommand( ['-g','RandomGhost','-p', agent, '-l', 'mediumClassic', '-a', depth,'-k','3'])
# 			print('Intento: ', turn ,' Algoritmo: ', agent,' Profundidad: ', depth, ' Nivel: 3', )
#
# 			runGames( **args )

##################
#LEVEL 4 :
##############
# print( "-----------------")
# print( " ---- NIVEL 4 !! ------ ")
# print ("------------------")
# for nbr in range(1,4):
# 	if (nbr == 3):
# 		nbr = 4
# 	nbr = str(nbr)
#
# 	depth = 'depth='+ nbr
#
# 	for difAgent in range(1,3):
# 		if(difAgent == 1):
# 			agent = 'MinimaxAgent'
# 		if(difAgent == 2):
# 			agent = 'AlphaBetaAgent'
# 		print(" ------- New Box: ----------")
# 		for turn in range(1,6):
# 			args = readCommand( ['-g','DirectionalGhost','-p', agent, '-l', 'mediumClassic', '-a', depth,'-k','3'])
# 			print('Intento: ', turn ,' Algoritmo: ', agent,' Profundidad: ', depth, ' Nivel: 4', )
#
# 			runGames( **args )

# ##################
# #LEVEL 5 :
# ##############
print( "----------------------")
print( "---- NIVEL 5 !! ------ ")
print ("----------------------")
for nbr in range(1,4):
	if (nbr == 3):
		nbr = 4
	nbr = str(nbr)

	depth = 'depth='+ nbr

	for difAgent in range(1,3):
		if(difAgent == 1):
			agent = 'MinimaxAgent'
		if(difAgent == 2):
			agent = 'AlphaBetaAgent'
		print(" ------- New Box: ----------")
		for turn in range(1,6):
			args = readCommand( ['-g','TacticalGhost','-p', agent, '-l', 'originalClassic','-z .5', '-a', depth,'-k','3'])
			print('Intento: ', turn ,' Algoritmo: ', agent,' Profundidad: ', depth, ' Nivel: 5', )

			runGames( **args )
