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


print ("PROYECTO PACMAN")
print ("Nivel 1: Un fantasma no sabe la ubicacion del Pacman")
print ("Nivel 2: Un fantasma conoce la ubicacion del Pacman")
print ("Nivel 3: Varios fantasmas no colaborativamente no conocen la ubicacion del Pacman")
print ("Nivel 4: Varios fantasmas no colaborativamente conocen la ubicacion del Pacman")
print ("Nivel 5: Varios fantasmas colaborativamente conocen la ubicacion del Pacman y de los otros fantasmas")
print ("Ingrese '0' si desea salir")

print (" ")

while (True):
	num = input ("Ingrese el numero del nivel a jugar: ")

	depth = input ("Ingrese el depth por el pacman: ")
	depth = 'depth='+ str(depth)

	agentInput= input("Cual agante quieres? escribir 1 por MinimaxAgent y 2 por AlphaBetaAgent: ")
	if (agentInput == 1):
		agent = 'MinimaxAgent'
	elif (agentInput == 2):
		agent = 'AlphaBetaAgent'

	print('The game is played with ', agent,' with a depth of ', depth, ' and level ', num, ' on the ghosts')


	if (num == 1):
		args = readCommand( ['-g','RandomGhost','-p', agent, '-l', 'smallClassic', '-a', depth,'-k','1'])
		runGames( **args )
	elif (num == 2):
		args = readCommand( ['-g','DirectionalGhost','-p', agent, '-l', 'mediumClassic', '-a', depth,'-k','1'])
		runGames( **args )
	elif (num == 3):
		args = readCommand( ['-g','RandomGhost','-p', agent, '-l', 'smallClassic', '-a', depth,'-k','3'])
		runGames( **args )
	elif (num == 4):
		args = readCommand( ['-g','DirectionalGhost','-p', agent, '-l', 'mediumClassic', '-a', depth,'-k','3'])
		runGames( **args )
	elif (num == 5):
		args = readCommand( ['-g','TacticalGhost','-p', agent, '-l', 'smallClassic', '-a', depth,'-k','3'])
		runGames( **args )
	elif (num == 0):
		break
	else :
		print ("Ingreso invalido")
