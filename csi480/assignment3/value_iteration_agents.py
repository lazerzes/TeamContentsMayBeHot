"""value_iteration_agents.py

Author: Rei Armenia, Matthew James Harrison
Class: CSI-480 AI
Assignment: MDPs and Reinforcement Learning Programming Assignment
Due Date: November 1, 2017

Description:
Pacman seeks reward.
Should he eat or should he run?
When in doubt, Q-learn.

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

import mdp
import util

from learning_agents import ValueEstimationAgent


class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learning_agents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """

    def __init__(self, mdp, discount=0.9, iterations=100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.get_states()
              mdp.get_possible_actions(state)
              mdp.get_transition_states_and_probs(state, action)
              mdp.get_reward(state, action, next_state)
              mdp.is_terminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter()  # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        for i in range(0, iterations):
            values = self.values.copy()
            for state in mdp.get_states():
                actions = mdp.get_possible_actions(state)
                if not actions:
                    continue
                q_values = [self.compute_q_value_from_values(state, action) for action in actions]
                values[state] = max(q_values)
            self.values = values.copy()
        self.policy = {}

    def get_value(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def compute_q_value_from_values(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        new_values = []
        for new_state, probability in self.mdp.get_transition_states_and_probs(state, action):
            reward = self.mdp.get_reward(state, action, new_state)
            value = probability * (reward + (self.discount * self.get_value(new_state)))
            new_values.append(value)
        return sum(new_values)

    def compute_action_from_values(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        if state in self.policy.keys():
            return self.policy[state]

        best_action = None

        actions = self.mdp.get_possible_actions(state)
        if actions:
            q_values = [(action, self.compute_q_value_from_values(state, action)) for action in actions]
            best_action, state = max(q_values, key=lambda x:x[1])
        self.policy[state] = best_action
        return best_action

    def get_policy(self, state):
        return self.compute_action_from_values(state)

    def get_action(self, state):
        "Returns the policy at the state (no exploration)."
        return self.compute_action_from_values(state)

    def get_q_value(self, state, action):
        return self.compute_q_value_from_values(state, action)
