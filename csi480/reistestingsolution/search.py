"""search.py

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

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in search_agents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def get_start_state(self):
        """
        Returns the start state for the search problem.
        """
        util.raise_not_defined()

    def is_goal_state(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raise_not_defined()

    def get_successors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, step_cost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'step_cost' is
        the incremental cost of expanding to that successor.
        """
        util.raise_not_defined()

    def get_cost_of_actions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raise_not_defined()


def tiny_maze_search(problem):
    """
    Returns a sequence of moves that solves tiny_maze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tiny_maze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depth_first_search(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.get_start_state()
    print "Is the start a goal?", problem.is_goal_state(problem.get_start_state())
    print "Start's successors:", problem.get_successors(problem.get_start_state())
    """
    "*** YOUR CODE HERE ***"
    print problem

    visited = {}
    current_state = problem.get_start_state();
    frontier = util.Stack()

    record = {}
    record["parent"] = None
    record["act"] = None
    record["state"] = current_state
    frontier.push(record)

    while not frontier.is_empty():
        record = frontier.pop()
        current_state = record["state"]
        if visited.has_key(hash(current_state)):
            continue
        visited[hash(current_state)] = True

        if problem.is_goal_state(current_state) == True:
            break

        for child in problem.get_successors(current_state):
            if not visited.has_key(hash(child[0])):
                sub_node = {}
                sub_node["parent"] = record
                sub_node["act"] = child[1]
                sub_node["state"] = child[0]
                frontier.push(sub_node)

    actions = []
    while record["act"] != None:
        actions.insert(0, record["act"])
        record = record["parent"]

    return actions



def breadth_first_search(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    visited = {}
    current_state = problem.get_start_state();
    frontier = util.Queue()

    record = {}
    record["parent"] = None
    record["act"] = None
    record["state"] = current_state
    frontier.push(record)

    while not frontier.is_empty():
        record = frontier.pop()
        current_state = record["state"]
        if visited.has_key(hash(current_state)):
            continue
        visited[hash(current_state)] = True

        if problem.is_goal_state(current_state) == True:
            break

        for child in problem.get_successors(current_state):
            if not visited.has_key(hash(child[0])):
                sub_node = {}
                sub_node["parent"] = record
                sub_node["act"] = child[1]
                sub_node["state"] = child[0]
                frontier.push(sub_node)

    actions = []
    while record["act"] != None:
        actions.insert(0, record["act"])
        record = record["parent"]

    return actions


def uniform_cost_search(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    visited = {}
    current_state = problem.get_start_state();
    frontier = util.PriorityQueue()

    record = {}
    record["parent"] = None
    record["act"] = None
    record["state"] = current_state
    record["cost"] = 0
    frontier.push(record, record["cost"])

    while not frontier.is_empty():
        record = frontier.pop()
        current_state = record["state"]
        cost = record["cost"]

        if visited.has_key(hash(current_state)):
            continue
        visited[hash(current_state)] = True

        if problem.is_goal_state(current_state) == True:
            break

        for child in problem.get_successors(current_state):
            if not visited.has_key(hash(child[0])):
                sub_node = {}
                sub_node["parent"] = record
                sub_node["act"] = child[1]
                sub_node["state"] = child[0]
                sub_node["cost"] = child[2] + cost
                frontier.push(sub_node, sub_node["cost"])

    actions = []
    while record["act"] != None:
        actions.insert(0, record["act"])
        record = record["parent"]

    return actions


def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def a_star_search(problem, heuristic=null_heuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    visited = {}
    current_state = problem.get_start_state();
    frontier = util.PriorityQueue()

    record = {}
    record["parent"] = None
    record["act"] = None
    record["state"] = current_state
    record["cost"] = 0
    record["heur"] = heuristic(current_state, problem)
    frontier.push(record, record["cost"] + record["heur"])

    while not frontier.is_empty():
        record = frontier.pop()
        current_state = record["state"]
        cost = record["cost"]
        h = record["heur"]

        if visited.has_key(hash(current_state)):
            continue
        visited[hash(current_state)] = True

        if problem.is_goal_state(current_state) == True:
            break

        for child in problem.get_successors(current_state):
            if not visited.has_key(hash(child[0])):
                sub_node = {}
                sub_node["parent"] = record
                sub_node["act"] = child[1]
                sub_node["state"] = child[0]
                sub_node["cost"] = child[2] + cost
                sub_node["heur"] = heuristic(sub_node["state"], problem)
                frontier.push(sub_node, sub_node["cost"] + sub_node["heur"])

    actions = []
    while record["act"] != None:
        actions.insert(0, record["act"])
        record = record["parent"]

    return actions

# Abbreviations
bfs = breadth_first_search
dfs = depth_first_search
astar = a_star_search
ucs = uniform_cost_search
