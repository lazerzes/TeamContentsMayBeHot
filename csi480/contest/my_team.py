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
        self.target_tile = None
        self.start = game_state.get_agent_position(self.index)
        self.food_count = len(self.get_food(game_state).as_list())
        CaptureAgent.register_initial_state(self, game_state)

    def choose_action(self, game_state):
        """
            Choose what action to take
        """
        legal_actions = game_state.get_legal_actions(self.index)
        values = [self.evaluate(game_state, action) for action in legal_actions]
        best_actions = [
            action for action, value in zip(legal_actions, values)
            if value == max(values)
            ]

        remaining_food = len(self.get_food(game_state).as_list())
        '''
        # Special case for food<=2, from baseline team
        if remaining_food <= 2:
            best_distance = float("inf")
            for action in legal_actions:
                successor = self.get_successor(game_state, action)
                new_position = successor.get_agent_position(self.index)
                distance = self.get_maze_distance(self.start, new_position)
                if distance < best_distance:
                    best_action = action
                    best_distance = distance
            return best_action
        '''
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


class ExpectimaxAgent(CaptureAgent):
    def __circular_increment(self, x, b):
        x += 1
        if x > b:
            x = 0
        return x

    def __is_agent_visible(self, index):
        if index in self.team_indices:
            return True
        visible_enemies = {
            i:x
            for i,x in zip(self.enemy_indices, self.enemy_states)
            if x.get_position() is not None
            }
        if visible_enemies.get(index):
            return True
        return False

    def __get_next_index(self, index):
        index = self.__circular_increment(index, 3)
        if not self.__is_agent_visible(index):
            index = self.__circular_increment(index, 3)
        return index

    def __get_optimization_function(self, index):
        if index in self.team_indices:
            return self.get_max
        return self.get_expected

    def register_initial_state(self, game_state):
        CaptureAgent.register_initial_state(self, game_state)
        self.start = game_state.get_agent_position(self.index)
        self.depth = 2
        self.team_indices = self.get_team(game_state)
        self.enemy_indices = self.get_opponents(game_state)
        self.roster = []
        self.target_tile = None

    def evaluate(self, game_state):
        values = []
        for action in game_state.get_legal_actions(self.index):
            features = self.get_features(game_state, action)
            weights = self.get_weights(game_state, action)
            values.append(features * weights)
        return max(values)

    def get_max(self, game_state, agent_index, depth):
        if game_state.is_over() or depth is 0:
            return self.evaluate(game_state)

        legal_actions = game_state.get_legal_actions(agent_index)
        score = -float('inf')-1

        for action in legal_actions:
            next_state = game_state.generate_successor(agent_index, action)
            next_index = self.__get_next_index(agent_index)
            next_function = self.__get_optimization_function(next_index)
            score = max(score, next_function(next_state, next_index, depth-1))
        return score

    def get_expected(self, game_state, agent_index, depth):
        if game_state.is_over() or depth is 0:
            return self.evaluate(game_state)

        legal_actions = game_state.get_legal_actions(agent_index)
        total_value = 0

        for action in legal_actions:
            next_state = game_state.generate_successor(agent_index, action)
            next_index = self.__get_next_index(agent_index)
            next_function = self.__get_optimization_function(next_index)
            total_value += next_function(next_state, next_index, depth-1)
        return total_value / len(legal_actions)

    def get_action(self, game_state):
        self.enemy_states = [
            game_state.get_agent_state(i)
            for i in self.enemy_indices
            ]

        if game_state.is_over():
            return self.evaluate(game_state)

        legal_actions = game_state.get_legal_actions(self.index)
        preferred_action = Directions.STOP
        score = -float('inf')-1

        for action in legal_actions:
            next_state = game_state.generate_successor(self.index, action)
            previous_score = score
            next_index = self.__get_next_index(self.index)
            next_function = self.__get_optimization_function(next_index)
            score = max(score,
                        next_function(next_state, next_index, self.depth))
            if score > previous_score:
                preferred_action = action
        return preferred_action

    def get_successor(self, game_state, action):
        """
        Finds the next successor which is a grid position (location tuple).
        """
        successor = game_state.generate_successor(self.index, action)
        pos = successor.get_agent_state(self.index).get_position()
        if pos != util.nearest_point(pos):
            # Only half a grid position was covered
            return successor.generate_successor(self.index, action)
        else:
            return successor

class OffenseAgent(BaseAgent):
    """
        REDO Weights for Offense
    """
    def get_features(self, game_state, action):
        features = util.Counter()
        next_state = self.get_successor(game_state, action)
        my_state = next_state.get_agent_state(self.index)
        my_position = my_state.get_position()
        food_list = self.get_food(next_state).as_list()

        features['score'] = -len(food_list)

        # Which action will get us closer to a dot?
        if len(food_list) > 0:
            food_distances = ([
                self.get_maze_distance(my_position, food)
                for food in food_list
                ])
            features['food_distance'] = min(food_distances)

        capsule_list = self.get_capsules(next_state)
        if len(capsule_list) > 0:
            capsule_distances = ([
                self.get_maze_distance(my_position, capsule)
                for capsule in capsule_list
                ])
            features['capsule_distance'] = min(capsule_distances)

        # Get enemies and seperate them into both ghosts and pacmans
        all_enemies = [
            next_state.get_agent_state(i)
            for i in self.get_opponents(next_state)
            ]
        enemy_ghosts = [
            agent for agent in all_enemies
            if not agent.is_pacman
            and agent.scared_timer == 0
            if agent.get_position() is not None
            ]
        enemy_ghosts_scared = [
            agent for agent in all_enemies if not agent.is_pacman
            if agent.get_position() is not None
            and agent.scared_timer > 0
            ]
        enemy_pacmans = [
            agent for agent in all_enemies if agent.is_pacman
            if agent.get_position() is not None
            ]

        # Avoid enemy ghosts
        if len(enemy_ghosts) > 0:
            ghost_distance = min([
                self.get_maze_distance(my_position,
                                       ghost.get_position())
                for ghost in enemy_ghosts
                ])
            features['ghost_distance'] = ghost_distance

        if len(enemy_ghosts_scared) > 0:
            ghost_distance = min([
                self.get_maze_distance(my_position,
                                       ghost.get_position())
                for ghost in enemy_ghosts_scared
                ])
            features['scared_ghost_distance'] = ghost_distance

        # If a Pacman is happened upon, go after it
        if len(enemy_pacmans) > 0:
            pacman_distance = min([
                self.get_maze_distance(my_position,
                                       pacman.get_position())
                for pacman in enemy_pacmans
                ])
            features['pacman_distance'] = pacman_distance

        # Movement features
        if action == Directions.STOP:
            features['stop'] = 1
        rev = Directions.REVERSE[
            game_state.get_agent_state(self.index).configuration.direction
            ]
        if action == rev:
            features['reverse'] = 1

        return features

    def get_weights(self, game_state, action):
        return {
            'score' : 1000,
            'food_distance': -1,
            'capsule_distance': -3,
            'ghost_distance': 20,
            'scared_ghost_distance': -10,
            'pacman_distance': -5,
            'stop': -100,
            'reverse': -2
        }

class DefenseAgent(BaseAgent):
    """
        REDO Weights for Defense
    """
    def get_features(self, game_state, action):
        features = util.Counter()
        next_state = self.get_successor(game_state, action)
        my_state = next_state.get_agent_state(self.index)
        my_position = my_state.get_position()
        food_list = self.get_food_you_are_defending(next_state).as_list()

        if not self.target_tile or my_position is self.target_tile:
            if len(food_list) > 0:
                food_distances = ([
                    self.get_maze_distance(my_position, food)
                    for food in food_list
                    ])
                self.target_tile = max(zip(food_list, food_distances),
                                       key=lambda x:x[1])[0]
        distance = self.get_maze_distance(my_position, self.target_tile)
        features['food_distance'] = distance

        features['on_defense'] = 1
        if my_state.is_pacman:
            features['on_defense'] = 0

        # Get enemies and seperate them
        all_enemies = [
            next_state.get_agent_state(i)
            for i in self.get_opponents(next_state)
            ]
        enemy_pacmans = [
            agent for agent in all_enemies if agent.is_pacman
            if agent.get_position() is not None
            ]
        noisy_pacman_distances = [
            pacman.get_agent_distances() for pacman in enemy_pacmans
            if pacman.get_position() is None
        ]

        # If a Pacman is happened upon, go after it
        if len(enemy_pacmans) > 0:
            pacman_distance = min([
                self.get_maze_distance(my_position,
                                       pacman.get_position())
                for pacman in enemy_pacmans
                ])
            features['pacman_distance'] = pacman_distance
        features['number_of_invaders'] = len(enemy_pacmans)

        if len(noisy_pacman_distances) > 0:
            features['noisy_pacman_distance'] = min(noisy_pacman_distances)

        # Movement features
        if action == Directions.STOP:
            features['stop'] = 1
        rev = Directions.REVERSE[
            game_state.get_agent_state(self.index).configuration.direction
            ]
        if action == rev:
            features['reverse'] = 1

        return features

    def get_weights(self, game_state, action):
        weights = {
            'food_distance': -1,
            'on_defense' : 100,
            'pacman_distance': -500,
            'noisy_pacman_distance': -250,
            'number_of_invaders': -1000,
            'stop': -100,
            'reverse': -2
        }

        next_state = self.get_successor(game_state, action)
        my_state = next_state.get_agent_state(self.index)
        if my_state.scared_timer > 0:
            weights['pacman_distance'] = 100

        return weights
