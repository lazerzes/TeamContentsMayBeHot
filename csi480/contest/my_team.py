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

    def choose_action(self, game_state):
        """
            Choose what action to take
        """
        actions = game_state.get_legal_actions(self.index)
        evaluation = [self.evaluate(game_state, action) for action in actions]

        best_actions = [
            action for action, value in zip(actions, evaluation)
            if value == max(evaluation)
            ]
        food_left = len(self.get_food(game_state).as_list())

        " Get The Team's State "
        team = [
            game_state.get_agent_state(agent)
            for agent in self.get_team(game_state)
            ]
        offense = team[0]
        defense = team[1]

        """
            Chech to see if either agent is currently pacman, self.index 0 will
            stop the defense player from caring about this check

            Here we are going to check if the difference between eaten and
            too eat(current score heald by pac man) is greater than 5
            if it is we want it to return to its base.
        """
        # If neither is pacman then just update our current food count
        if (not offense.is_pacman and not defense.is_pacman
                and self.index == 0):
            self.num_foods = food_left
        # If Offense is pacman then get the current amount of food eaten
        elif (offense.is_pacman and not defense.is_pacman
                and self.index == 0):
            dif_foods = self.num_foods - food_left
            if (dif_foods >= 5):
                distance = float("inf")
                for action in actions:
                    successor = self.get_successor(game_state, action)
                    pos_successor = successor.get_agent_position(self.index)
                    temp = self.get_maze_distance(self.pos_start, pos_successor)
                    if(temp < distance):
                        best_action = actions
                        distance = temp
                    return best_action
            elif (food_left == 0 and dif_foods > 0):
                distance = float("inf")
                for action in actions:
                    next_state = self.get_successor(self.index, action)
                    pos_successor = successor.get_agent_position(self.index)
                    temp = self.get_maze_distance(self.start, pos_successor)
                    if(temp < distance):
                        best_action = actions
                        distance = temp
                    return best_action
        return random.choice(best_actions)

    def get_successor(self, game_state, action):
        """
            Get the next successor
        """
        successor = game_state.generate_successor(self.index, action)
        successor_pos = successor.get_agent_state(self.index).get_position()

        #Align to Grid
        if (successor_pos != util.nearest_point(successor_pos)):
            return successor.generate_successor(self.index, action)

        return successor

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

        features['successor_score'] = self.get_score(successor)
        return features

    def get_weights(self):
        return {'successor_score':1.0}

    """def euclidean_heuristic(position, problem, info={}):
        "The Euclidean distance heuristic for a PositionSearchProblem -- Copied from Assignment 1"
        xy1 = position
        xy2 = problem.goal
        return ((xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2) ** 0.5
    """


class OffenseAgent(BaseAgent):
    """
        REDO Weights for Offense
    """
    def get_features(self, game_state, action):

        features = util.Counter()

        # Will an action decrease the food_left? (eating betters the score)
        # baseline_team does the same thing, its a good metric!
        successor = self.get_successor(game_state, action)
        successor_pos = successor.get_agent_state(self.index).get_position()
        foods = self.get_food(successor).as_list()
        features['successor_score'] = -(len(foods))

        # Which action will get us closer to a dot?
        if(len(foods) > 0):
            distance_to_food = min([self.get_maze_distance(successor_pos, dot) for dot in foods])
            features['distance_to_food'] = distance_to_food

        # Get enemies and seperate them into both ghosts and pacmans
        enemies = [
            successor.get_agent_state(num)
            for num in self.get_opponents(successor)
            ]
        enemy_ghosts = [
            agent for agent in enemies if not agent.is_pacman
            and agent.get_position() is not None
            ]
        enemy_pacmans = [
            agent for agent in enemies if agent.is_pacman
            and agent.get_position() is not None
            ]

        # Avoid enemy ghosts
        if(len(enemy_ghosts) > 0):
            ghost_min = min(
                [self.get_maze_distance(successor_pos, ghost_pos.get_position())
                for ghost_pos in enemy_ghosts
                ])
            features['ghost_distance'] = ghost_min


        # If a Pacman is happened upon, go after it
        if(len(enemy_pacmans) > 0):
            pacman_min = min([
                self.get_maze_distance(successor_pos, pac_pos.get_position())
                for pac_pos in enemy_pacmans
                ])
            if(pacman_min <= 3):
                features['pacman_distance'] = pacman_min
            else:
                features['pacman_distance'] = 0


        return features

    def get_weights(self, game_state, action):

        return {
            'successor_score' : 10,
            'distance_to_food': -1,
            'ghost_distance': 200,
            'pacman_distance': 50

        }

class DefenseAgent(BaseAgent):
    """
        REDO Weights for Defense
    """
    def get_features(self, game_state, action):
        features = util.Counter()

        successor = self.get_successor(game_state, action)
        my_state = successor.get_agent_state(self.index)
        my_position = my_state.get_position()

        # TODO: Select a target position

        # Score feature
        features['successor_score'] = self.get_score(successor)

        '''
        # Movement features
        if action == Directions.STOP:
            features['stop'] = 1
        rev = Directions.REVERSE[
            game_state.get_agent_state(self.index).configuration.direction
            ]
        if action == rev:
            features['reverse'] = 1
        '''

        # Enemy features
        enemies = [
            successor.get_agent_state(x) for x in self.get_opponents(successor)
            ]
        invaders = [
            x for x in enemies if x.is_pacman and x.get_position() != None
            ]
        features['num_invaders'] = len(invaders)
        if len(invaders):
            min_distance = min([
                self.get_maze_distance(my_position, x.get_position())
                for x in invaders
                ])
            features['invader_distance'] = min_distance

        # TODO Create a positive feature based on maze distance

        return features

    def get_weights(self, game_state, action):
        return {
            'successor_score': 1,
            'num_invaders': -1000,
            'invader_distance': -10,
            'stop': -100,
            'reverse': -100
            }

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
