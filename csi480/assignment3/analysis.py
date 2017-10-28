"""analysis.py

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

######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

# Change only ONE of the discount and noise parameters so that the optimal
# policy causes the agent to attempt to cross the bridge.
def question2():
    answer_discount = 0.9
    answer_noise = 0.0
    return answer_discount, answer_noise


# Prefer the close exit (+1), risking the cliff (-10)
def question3a():
    answer_discount = 0.1
    answer_noise = 0.0
    answer_living_reward = 0.0
    return answer_discount, answer_noise, answer_living_reward

    # If not possible, return 'NOT POSSIBLE'

# Prefer the close exit (+1), but avoiding the cliff (-10)
def question3b():
    answer_discount = 0.1
    answer_noise = 0.1
    answer_living_reward = 0
    return answer_discount, answer_noise, answer_living_reward

    # If not possible, return 'NOT POSSIBLE'

# Prefer the distant exit (+10), risking the cliff (-10)
def question3c():
    answer_discount = None
    answer_noise = None
    answer_living_reward = None
    return answer_discount, answer_noise, answer_living_reward

    # If not possible, return 'NOT POSSIBLE'

# Prefer the distant exit (+10), avoiding the cliff (-10)
def question3d():
    answer_discount = None
    answer_noise = None
    answer_living_reward = None
    return answer_discount, answer_noise, answer_living_reward

    # If not possible, return 'NOT POSSIBLE'

# Avoid both exits and the cliff (so an episode should never terminate)
def question3e():
    answer_discount = None
    answer_noise = None
    answer_living_reward = None
    return answer_discount, answer_noise, answer_living_reward

    # If not possible, return 'NOT POSSIBLE'

def question6():
    answer_epsilon = None
    answer_learning_rate = None
    return answer_epsilon, answer_learning_rate
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
