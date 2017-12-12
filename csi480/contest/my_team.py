"""my_team.py

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

from capture_agents import CaptureAgent
import random
import time
import util
from game import Directions
import game

#################
# Team creation #
#################

def create_team(first_index, second_index, is_red,
               first='OffenseAgent', second='DefenseAgent'):
    """
    This function should return a list of two agents that will form the
    team, initialized using first_index and second_index as their agent
    index numbers.  is_red is True if the red team is being created, and
    will be False if the blue team is being created.

    As a potentially helpful development aid, this function can take
    additional string-valued keyword arguments ("first" and "second" are
    such arguments in the case of this function), which will come from
    the --red_opts and --blue_opts command-line arguments to capture.py.
    For the nightly contest, however, your team will be created without
    any extra arguments, so you should make sure that the default
    behavior is what you want for the nightly contest.
    """

    # The following line is an example only; feel free to change it.
    return [eval(first)(first_index), eval(second)(second_index)]

##########
# Agents #
##########
class BaseAgent(CaptureAgent):
    """
        Shared Code from between both Offense and Defense
    """
    def register_initial_state(self, game_state):
        CaptureAgent.register_initial_state(self, game_state)

        self.pos_start = game_state.get_agent_position(self.index)
        self.num_foods = len(self.get_food(game_state).as_list())
        self.ini_foods = len(self.get_food(game_state).as_list())

    def choose_action(self, game_state):
        """
            Choose what action to take
        """
        actions = game_state.get_legal_actions(self.index)
        evaluation = [self.evaluate(game_state, action) for action in actions]

        best_actions = [action for action, value in zip(actions, values) if value == max(values)]
        food_left = len(self.get_food(game_state).as_list())

        " Get The Team's State "
        team = [game_state.get_agent_state(agent) for agent in self.get_team(game_state)]



        util.raise_not_defined()

    def get_successor(self, game_state, action):
        """
            Get the next successor (location tuple)
        """

        util.raise_not_defined()

    def evaluate(self, game_state, action):
        """
            Evaluation Function --- No Need to Override
        """

        features = self.get_features(game_state, action)
        weights = self.get_weights(game_state, action)

        return (features * weights)

    def get_features(self, game_state, action):

        features = util.Counter()
        successor = get_successor(game_state)

        features['successor'] = self.get_score(successor)
        return features

    def get_weights(self):
        return {'successor':1.0}

    def euclidean_heuristic(position, problem, info={}):
        "The Euclidean distance heuristic for a PositionSearchProblem -- Copied from Assignment 1"
        xy1 = position
        xy2 = problem.goal
        return ((xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2) ** 0.5


class OffenseAgent(BaseAgent):
    """
        REDO Weights for Offense
    """
    def get_features(self, game_state, action):

        util.raise_not_defined()

    def get_weights(self, game_state, action):

        util.raise_not_defined()

class DefenseAgent(BaseAgent):
    """
        REDO Weights for Defense
    """
    def get_features(self, game_state, action):

        score = get_score(game_state)

    def get_weights(self, game_state, action):

        util.raise_not_defined()

class DummyAgent(CaptureAgent):
    """
    A Dummy agent to serve as an example of the necessary agent structure.
    You should look at baseline_team.py for more details about how to
    create an agent as this is the bare minimum.
    """

    def register_initial_state(self, game_state):
        """
        This method handles the initial setup of the
        agent to populate useful fields (such as what team
        we're on).

        A distance_calculator instance caches the maze distances
        between each pair of positions, so your agents can use:
        self.distancer.get_distance(p1, p2)

        IMPORTANT: This method may run for at most 15 seconds.
        """

        '''
        Make sure you do not delete the following line. If you would like to
        use Manhattan distances instead of maze distances in order to save
        on initialization time, please take a look at
        CaptureAgent.register_initial_state in capture_agents.py.
        '''
        CaptureAgent.register_initial_state(self, game_state)

        '''
        Your initialization code goes here, if you need any.
        '''

    def choose_action(self, game_state):
        """
        Picks among actions randomly.
        """
        actions = game_state.get_legal_actions(self.index)

        '''
        You should change this in your own agent.
        '''

        return random.choice(actions)
