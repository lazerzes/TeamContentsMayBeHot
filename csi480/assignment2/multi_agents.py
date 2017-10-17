"""multi_agents.py

Author: Rei Armenia, Matthew James Harrison
Class: CSI-480 AI
Assignment: Multi-Agent Pacman Programming Assignment
Due Date: October 16, 2017

Description:
Pacman, now with ghosts.
Minimax, Expectimax,
Evaluation.

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
 - Reproduce this assignment and provide a copy to another member of academic
   staff; and/or
 - Communicate a copy of this assignment to a plagiarism checking service
   (which may then retain a copy of this assignment on its database for the
   purpose of future plagiarism checking)

----------------------
Champlain College CSI-480, Fall 2017
The following code was adapted by Joshua Auerbach (jauerbach@champlain.edu)
from the UC Berkeley Pacman Projects (see license and attribution below).

----------------------
Licensing Information:  You are free to use or extend these projects for
educational purposes provided that (1) you do not distribute or publish
solutions, (2) you retain this notice, and (3) you provide clear
attribution to UC Berkeley, including a link to http://ai.berkeley.edu.

Attribution Information: The Pacman AI projects were developed at UC Berkeley.
The core projects and autograders were primarily created by John DeNero
(denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
Student side autograding was added by Brad Miller, Nick Hay, and
Pieter Abbeel (pabbeel@cs.berkeley.edu).
"""


from util import manhattan_distance
from game import Directions
import random, util
import sys

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def get_action(self, game_state):
        """
        You do not need to change this method, but you're welcome to.

        get_action chooses among the best options according to the evaluation function.

        Just like in the previous project, get_action takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legal_moves = game_state.get_legal_actions()

        # Choose one of the best actions
        scores = [self.evaluation_function(game_state, action) for action in legal_moves]
        best_score = max(scores)
        best_indices = [index for index in range(len(scores)) if scores[index] == best_score]
        chosen_index = random.choice(best_indices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legal_moves[chosen_index]

    def evaluation_function(self, current_game_state, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (new_food) and Pacman position after moving (new_pos).
        new_scared_times holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successor_game_state = current_game_state.generate_pacman_successor(action)
        new_pos = successor_game_state.get_pacman_position()
        new_food = successor_game_state.get_food()
        new_ghost_states = successor_game_state.get_ghost_states()
        new_scared_times = [ghost_state.scared_timer for ghost_state in new_ghost_states]

        "*** YOUR CODE HERE ***"
        score = successor_game_state.get_score()

        # Filter/Map: Compute Manhattan distances from Pacman to ghosts
        new_ghost_positions = [ ghost.get_position() for ghost in new_ghost_states if ghost.scared_timer > 0 ]
        new_ghost_distances = [ manhattan_distance(ghost_pos, new_pos) for ghost_pos in new_ghost_positions ]

        # Map: Compute Manhattan distances from Pacman to foods
        new_food_positions = successor_game_state.get_food().as_list()
        new_food_distances = [ manhattan_distance(food_pos, new_pos) for food_pos in new_food_positions ]

        evaluation = score
        if new_food_distances:
            # Reduce: Find closest food and compute bonus with inverse relation to distance
            evaluation += 10/(min(new_food_distances)+1)
        if new_ghost_distances:
            # Reduce: Find closest ghost and compute penalty with inverse relation to distance
            evaluation -= 15/(min(new_ghost_distances)+1)
        return evaluation

def score_evaluation_function(current_game_state):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return current_game_state.get_score()

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

    def __init__(self, eval_fn = 'score_evaluation_function', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluation_function = util.lookup(eval_fn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def minimax(self, state, depth, agent):
        # Check if depth reached
        if depth == self.depth:
            return ('Stop', self.evaluation_function(state))

        # Get all actions
        actions = state.get_legal_actions(agent)

        # Check if terminal state
        if not actions:
            return ('Stop', self.evaluation_function(state))

        # Get all successors
        successors = [ state.generate_successor(agent, action) for action in actions ]

        # Increment agent (with wrapping) and increment depth when all agents have acted
        next_agent = agent+1
        next_depth = depth
        if next_agent >= state.get_num_agents():
            next_agent = 0
            next_depth += 1

        # Recurse for each successor to compute their values, incrementing agent index and depth
        values = [ self.minimax(successor, next_depth, next_agent)[1] for successor in successors ]

        # Create tuples of related actions and values: (action, value)
        successors = zip(actions, values)

        # Maximize if player or else minimize, returning tuple: (action, value)
        if agent == 0:
            return max(successors, key=lambda x: x[1])
        return min(successors, key=lambda x: x[1])

    def get_action(self, game_state):
        """
          Returns the minimax action from the current game_state using self.depth
          and self.evaluation_function.

          Here are some method calls that might be useful when implementing minimax.

          game_state.get_legal_actions(agent_index):
            Returns a list of legal actions for an agent
            agent_index=0 means Pacman, ghosts are >= 1

          game_state.generate_successor(agent_index, action):
            Returns the successor game state after an agent takes an action

          game_state.get_num_agents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"

        return self.minimax(game_state, 0, 0)[0]

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def ab_minimax(self, state, depth, agent, alpha, beta):
        # Check if depth reached
        if depth == self.depth:
            return ('Stop', self.evaluation_function(state))

        # Get all actions
        actions = state.get_legal_actions(agent)

        # Check if terminal state
        if not actions:
            return ('Stop', self.evaluation_function(state))

        # Increment agent (with wrapping) and increment depth when all agents have acted
        next_agent = agent+1
        next_depth = depth
        if next_agent >= state.get_num_agents():
            next_agent = 0
            next_depth += 1

        # Maximize if player, returning tuple: (action, value)
        if agent == 0:
            value = ('Stop', -sys.maxsize - 1)
            for action in actions:
                successor = state.generate_successor(agent, action)
                tmp = ( action, self.ab_minimax(successor, next_depth, next_agent, alpha, beta)[1] )
                value = max(value, tmp, key=lambda x: x[1])
                if value[1] > beta:
                    return value
                alpha = max(alpha, value[1])
            return value
        # Or else minimize, returning tuple: (action, value)
        value = ('Stop', sys.maxsize)
        for action in actions:
            successor = state.generate_successor(agent, action)
            tmp = ( action, self.ab_minimax(successor, next_depth, next_agent, alpha, beta)[1] )
            value = min(value, tmp, key=lambda x: x[1])
            if value[1] < alpha:
                return value
            beta = min(beta, value[1])
        return value

    def get_action(self, game_state):
        """
          Returns the minimax action using self.depth and self.evaluation_function
        """
        "*** YOUR CODE HERE ***"

        return self.ab_minimax(game_state, 0, 0, -sys.maxsize - 1, sys.maxsize)[0]

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def get_max(self, game_state, depth):
        if game_state.is_win() or game_state.is_lose() or depth is 0:
            return self.evaluation_function(game_state)

        legal_actions = game_state.get_legal_actions(0)
        prefer_action = Directions.STOP
        score = -(float("inf"))

        for action in legal_actions:
            prev_score = score
            next_state = game_state.generate_successor(0, action)
            score = max(score, self.get_expected(next_state, 1, depth))
        return score

    def get_expected(self, game_state, index, depth):
        if game_state.is_win() or game_state.is_lose() or depth is 0:
            return self.evaluation_function(game_state)

        number_ghosts = game_state.get_num_agents() - 1
        legal_actions = game_state.get_legal_actions(index)
        numbe_actions = len(legal_actions)
        total_val = 0

        for action in legal_actions:
            next_state = game_state.generate_successor(index, action)
            if index is number_ghosts:
                total_val += self.get_max(next_state, depth - 1)
            else:
                total_val += self.get_expected(next_state, index + 1, depth)

        return total_val / numbe_actions

    def get_action(self, game_state):
        """
          Returns the expectimax action using self.depth and self.evaluation_function

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        if(game_state.is_win() or game_state.is_lose()):
            return self.evaluation_function(game_state)

        legal_actions = game_state.get_legal_actions(0)
        prefer_action = Directions.STOP
        score = -(float("inf"))

        for action in legal_actions:
            next_state = game_state.generate_successor(0, action)
            prev_score = score
            score = max(score, self.get_expected(next_state, 1, self.depth))
            if score > prev_score:
                prefer_action = action
        return prefer_action


def better_evaluation_function(current_game_state):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: Prioritizes states in which food is close and ghosts are far.
      Food becomes more valuable as its scarcity increases.

    """
    "*** YOUR CODE HERE ***"
    score = current_game_state.get_score()
    new_ghost_states = current_game_state.get_ghost_states()
    new_pos = current_game_state.get_pacman_position()
    new_food = current_game_state.get_food()

    # Compute distances to foods
    new_food_positions = current_game_state.get_food().as_list()
    new_food_distances = [ manhattan_distance(food_pos, new_pos) for food_pos in new_food_positions ]

    # Compute distances to ghosts
    new_ghost_positions = [ ghost.get_position() for ghost in new_ghost_states if ghost.scared_timer > 0 ]
    new_ghost_distances = [ manhattan_distance(ghost_pos, new_pos) for ghost_pos in new_ghost_positions ]

    evaluation = score
    if new_food_distances:
        # Bonus for minimizing distance to closest food, improves with food scarcity
        evaluation += 10/(min(new_food_distances)+1) * 5/(len(new_food_distances)+1)
    if new_ghost_distances:
        # Penalty for minimizing distance to closest ghost
        evaluation -= 15/(min(new_ghost_distances)+1)
    return evaluation

# Abbreviation
better = better_evaluation_function
