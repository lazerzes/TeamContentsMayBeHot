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

        self.start = game_state.get_agent_position(self.index)
        self.food_count = len(self.get_food(game_state).as_list())

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

        # Get the team state
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
            self.food_count = remaining_food
        # If Offense is pacman then get the current amount of food eaten
        elif (offense.is_pacman and not defense.is_pacman
                and self.index == 0):
            dif_foods = self.food_count - remaining_food
            if (dif_foods >= 5):
                distance = float("inf")
                for action in legal_actions:
                    successor = self.get_successor(game_state, action)
                    new_position = successor.get_agent_position(self.index)
                    temp = self.get_maze_distance(self.start, new_position)
                    if(temp < distance):
                        best_action = legal_actions
                        distance = temp
                    return best_action
            elif (remaining_food == 0 and dif_foods > 0):
                distance = float("inf")
                for action in legal_actions:
                    next_state = self.get_successor(self.index, action)
                    new_position = successor.get_agent_position(self.index)
                    temp = self.get_maze_distance(self.start, new_position)
                    if(temp < distance):
                        best_action = legal_actions
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

        # Movement features
        if action == Directions.STOP:
            features['stop'] = 1
        rev = Directions.REVERSE[
            game_state.get_agent_state(self.index).configuration.direction
            ]
        if action == rev:
            features['reverse'] = 1

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
            'stop': -1000,
            'reverse': -5
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

class ExpectimaxAgent(CaptureAgent):
    def __get_next_index(self, index):
        index += 1
        if index > 3:
            index = 0
        return index

    def register_initial_state:
        self.start = game_state.get_agent_position(self.index)
        self.depth = 2
        self.team = get_team()
        if self.index == team[0]:
            self.get_features = get_offensive_features
            self.get_weights = get_offensive_weights
        else:
            self.get_features = get_defensive_features
            self.get_weights = get_defensive_weights
        CaptureAgent.register_initial_state(self, game_state)

    def evaluate(self, game_state, action):
        features = self.get_features(game_state, action)
        weights = self.get_weights(game_state, action)
        return features * weights

    def get_max(self, game_state, agent_index, depth):
        if game_state.is_win() or game_state.is_lose():
            return self.evaluate(game_state)

        legal_actions = game_state.get_legal_actions(agent_index)
        score = -float('inf')-1

        for action in legal_actions:
            next_state = game_state.generate_successor(agent_index, action)
            next_index = self.__get_next_index(agent_index)
            score = max(score, self.get_expected(next_state, next_index, depth))
        return score

    def get_expected(self, game_state, agent_index, depth):
        if game_state.is_win() or game_state.is_lose():
            return self.evaluate(game_state)

        legal_actions = game_state.get_legal_actions(agent_index)
        total_value = 0

        for action in legal_actions:
            next_state = game_state.generate_successor(agent_index, action)
            next_index = __get_next_index(agent_index)
            total_value += self.get_max(next_state, next_index, depth-1)
        return total_value / len(legal_actions)

    def get_action(self, game_state):
        if game_state.is_win() or game_state.is_lose():
            return self.evaluate(game_state)

        legal_actions = game_state.get_legal_actions(self.index)
        preferred_action = Directions.STOP
        score = -float('inf')-1

        for action in legal_actions:
            next_state = game_state.generate_successor(self.index, action)
            previous_score = score
            next_index = __get_next_index(self.index)
            score = max(score, self.get_expected(next_state,
                                                 next_index,
                                                 self.depth))
            if score > previous_score:
                preferred_action = action
        return preferred_action
