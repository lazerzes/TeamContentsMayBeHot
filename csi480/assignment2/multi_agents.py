"""multi_agents.py

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
        tab = ''
        for i in range(0, depth):
            tab += ' | '
        print(tab + 'Depth:', depth, '/', self.depth)

        # Check if depth reached
        if depth == self.depth:
            return ('Stop', self.evaluation_function(state))

        # Agent index wrapping
        if agent >= state.get_num_agents():
            agent = 0

        # Get all actions
        actions = state.get_legal_actions(agent)
        print(tab + 'Actions:', actions)

        # Check if terminal state
        if not actions:
            return ('Stop', self.evaluation_function(state))

        # Get all successors
        successors = [ state.generate_successor(agent, action) for action in actions ]

        # Recurse for each successor to compute their values, incrementing agent index and depth
        values = [ self.minimax(successor, depth+1, agent+1)[1] for successor in successors ]
        print(tab + 'Values:', values)
        print(tab)

        # Create tuples of related actions and values: (action, value)
        successors = zip(actions, values)

        # Maximize if player or else minimize
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

    def get_action(self, game_state):
        """
          Returns the minimax action using self.depth and self.evaluation_function
        """
        "*** YOUR CODE HERE ***"
        util.raise_not_defined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def get_action(self, game_state):
        """
          Returns the expectimax action using self.depth and self.evaluation_function

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"

        """
            func_name: get_expected -- (en_US: Get Expected Value)

            desc:
        """
        def get_expected(game_state, index, depth):
            if game_state.is_win() or game_state.is_lise() or depth is 0:
                return self.evaluation_function(game_state)

            number_ghosts = game_state.get_num_agents() - 1
            legal_actions = game_state.get_legal_actions(index)
            numbe_actions = len(legal_actions)
            total_val = 0

            for action in legal_actions:
                next_state = game_state.generate_successor(index, action)
                if index is number_ghosts:
                    total_val += get_max_value(next_state, depth - 1)
                else:
                    total_value += get_expected(next_state, index + 1, depth)

            return total_value / numbe_actions

        if(game_state.is_win() or game_state.is_lose()):
            return self.evaluation_function(game_state)

        legal_actions = game_state.get_legal_actions(0)
        prefer_acrion = Directions.STOP
        score = -(float("inf"))

        for action in legal_actions:
            next_state = game_state.generate_successor(0, action)
            prev_score = score

        util.raise_not_defined()

def better_evaluation_function(current_game_state):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raise_not_defined()

# Abbreviation
better = better_evaluation_function
