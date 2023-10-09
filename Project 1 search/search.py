# search.py
# ---------
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

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
import math
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def backtrack(reachedGoal,start,prev):
    result = []
    current = reachedGoal
    while (prev[current] is not None):
        result.append(prev[current][1])
        current = prev[current][0]
    result.reverse()
    print(result)
    return result

def depthFirstSearch(problem: SearchProblem):
    dfsq = util.Stack()
    visited = set()
    start = problem.getStartState()
    dfsq.push(start)
    prev = {} # maps state to (prevstate, action)
    prev[start] = None
    while (not dfsq.isEmpty()):
        current = dfsq.pop()
        visited.add(current)
        if problem.isGoalState(current):
            return backtrack(current,start,prev)
        for nextState,action,cost in  problem.getSuccessors(current):
            if (nextState in visited):continue
            prev[nextState]=(current,action)
            dfsq.push(nextState)

def breadthFirstSearch(problem: SearchProblem):   
    dfsq = util.Queue()
    visited = set()
    prev = {} # maps state to (prevstate, action)
    start = problem.getStartState()
    dfsq.push(start)
    prev[start] = None
    while (not dfsq.isEmpty()):
        current = dfsq.pop()
        if problem.isGoalState(current):
            return backtrack(current,start,prev)
        visited.add(current)
        for nextState,action,cost in  problem.getSuccessors(current):
            if (nextState in visited):continue
            dfsq.push(nextState)
            visited.add(nextState)
            prev[nextState]=(current,action)
            

def uniformCostSearch(problem: SearchProblem):
    dfsq = util.PriorityQueue()
    visited = set()
    costs = {}
    start = problem.getStartState()
    dfsq.push(start,0) 
    costs[start]=0
    prev = {} # maps state to (prevstate, action)
    prev[(start)] = None
    while (not dfsq.isEmpty()):
        current = dfsq.pop()
        visited.add(current)
        if problem.isGoalState(current):
            return backtrack(current,start,prev)
        for nextState,action,cost in  problem.getSuccessors(current):
            if (nextState in visited):continue
            if (costs.get(nextState,math.inf) > costs[current] + cost): 
                prev[nextState]=(current,action)
                costs[nextState]= costs[current] + cost
            dfsq.update(nextState, costs[current] + cost)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    dfsq = util.PriorityQueue()
    visited = set()
    costs = {}
    start = problem.getStartState()
    dfsq.push(start,0 + heuristic(start,problem)) 
    costs[start]=0
    prev = {} # maps state to (prevstate, action)
    prev[(start)] = None
    while (not dfsq.isEmpty()):
        current = dfsq.pop()
        visited.add(current)
        if problem.isGoalState(current):
            return backtrack(current,start,prev)
        for nextState,action,cost in  problem.getSuccessors(current):
            if (nextState in visited):continue
            if (costs.get(nextState,math.inf) > costs[current] + cost): 
                prev[nextState]=(current,action)
                costs[nextState]= costs[current] + cost
            dfsq.update(nextState, costs[current] + cost + heuristic(nextState,problem))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
