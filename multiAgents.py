# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        hola alberto

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        def minScore(state, depth, agentIndex):  #agentIndes: 0 = the pacman  1>= ghosts
        #Recurive method going through att agents in the game.

            legal_actions = state.getLegalActions(agentIndex)
            Nbr_ghosts = gameState.getNumAgents() - 1;
            score = float("inf")                            #score to +infinity , because min() is used

            if state.isWin() or state.isLose() or depth == 0:
                return self.evaluationFunction(state)

            is_last_ghost = (agentIndex == Nbr_ghosts)
            if is_last_ghost:
                for action in legal_actions:
                    successor= state.generateSuccessor(agentIndex, action)
                    score = min(score, maxScore(successor, depth - 1))
            else:
                for action in legal_actions:
                    successor = state.generateSuccessor(agentIndex,action)
                    #recurvie here. checks against the next agent. and saves the lowest score.
                    score = min(score, minScore(successor, depth, agentIndex + 1))

            return score

        def maxScore(state, depth):

            Nbr_ghosts = gameState.getNumAgents() - 1;
            score = -(float("inf"))                            #score set to negativ infinity since max() is used

            if state.isWin() or state.isLose() or depth == 0:
                return self.evaluationFunction(state)

            for action in state.getLegalActions(0):
                successor = state.generateSuccessor(0, action)   #successors for pacman
                score = max(score, minScore(successor, depth - 1, 1))

            return score

        #THE CODE:
        # Main:
        # return action with the maxvalue from minScore()
        # minScore:
        # (If in terminal-state - return utiliy)
        # return the min value from all actions maxScore()
        # maxScore:
        # (If in terminal-state - return utiliy)
        # return the max value from all actions minScore()

        score = -(float("inf"))
        action = Directions.STOP #If no actions exsist in getLegalActions. it is put to STOP.

        #The action with the highest score is used.
        for next_action in gameState.getLegalActions():
            if next_action != Directions.STOP:
                score_old = score
                next_state = gameState.generateSuccessor(0, next_action)  # gets successors for Pacman (0=pacman)
                #Takes the largest number out of score and minScore() for the ghosts
                score_new = max(score, minScore(next_state, self.depth, 1))  # depth default = 2.
                if score_new > score_old:
                    action = next_action
                score=score_new     #to make the highest score being the one compare in next loop.

        return action

class AlphaBetaAgent(MultiAgentSearchAgent):
	"""
		Your minimax agent with alpha-beta pruning (question 3)
	"""

	def getAction(self, gameState):
		"""
			Returns the minimax action using self.depth and self.evaluationFunction
		"""
		"*** YOUR CODE HERE ***"
		def maxScore(state, alpha, beta, depth):

			if state.isWin() or state.isLose() or depth == 0:
				return self.evaluationFunction(state)

			score = -(float("inf"))
			legal_actions = state.getLegalActions(0)

			for action in legal_actions:
				nextState = state.generateSuccessor(0, action)
				score = max(score, minScore(nextState, alpha, beta, state.getNumAgents() - 1, depth))

				if score >= beta:
					return score

				alpha = max(alpha, score)

			return score


		def minScore(gameState, alpha, beta, agent_i, depth):

			numghosts = gameState.getNumAgents() - 1

			if gameState.isWin() or gameState.isLose() or depth == 0:
				return self.evaluationFunction(gameState)

			score = float("inf")
			legal_actions = gameState.getLegalActions(agent_i)

			for action in legal_actions:
				nextState = gameState.generateSuccessor(agent_i, action)

				if agent_i == numghosts:

					score = min(score, maxScore(nextState, alpha, beta, depth - 1))
					if score <= alpha:
						return score
					beta = min(beta, score)

				else:

					score = min(score, minScore(nextState, alpha, beta, agent_i + 1, depth))
					if score <= alpha:
						return score
					beta = min(beta, score)

			return score


		action = Directions.STOP

		score 	= -(float("inf"))
		alpha 	= -(float("inf"))
		beta 	= float("inf")

		for avail_action in gameState.getLegalActions(0):

			prevscore = score
			nextState = gameState.generateSuccessor(0, avail_action)
			score = max(score, minScore(nextState, alpha, beta, 1, self.depth))

			if score > prevscore:
				action = avail_action

			if score >= beta:
				return action

			alpha = max(alpha, score)

		return action


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
