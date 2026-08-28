from typing import Tuple
from algorithms import utils
from algorithms.problems import SystemRepairProblem


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def manhattanHeuristic(state, problem):
    """
    The Manhattan distance heuristic.

    Baseline rule for this workshop: estimate the direct distance to the next
    mandatory target:
    - K if the robot does not have the kit yet.
    - the nearest pending T if the robot has the kit and systems remain.
    - C if all systems have been repaired.
    """
    position, hasKit, pendingSystems = state
    
    if not hasKit:
        problem.kitPosition
    elif len(pendingSystems) > 0:
        target min( pendingSystems,
            key=lambda t: abs(position[0] - t[0]) + abs(position[1] - t[1]),)
    else:
        target = problem.controlPosition

    return abs(position[0] - target[0]) + abs(position[1] - target[1])


def euclideanHeuristic(state, problem):
    """
    The Euclidean distance heuristic.

    Baseline rule for this workshop: estimate the direct distance to the next
    mandatory target:
    - K if the robot does not have the kit yet.
    - the nearest pending T if the robot has the kit and systems remain.
    - C if all systems have been repaired.
    """
    position, hasKit, pendingSystems = state

    if not hasKit:
        target = problem.kitPosition
    elif len(pendingSystems) > 0:
        target = min(
            pendingSystems,
            key=lambda t: ((position[0] - t[0]) ** 2 + (position[1] - t[1]) ** 2) ** 0.5,
        )
    else:
        target = problem.controlPosition

    return ((position[0] - target[0]) ** 2 + (position[1] - target[1]) ** 2) ** 0.5


def systemRepairHeuristic(
    state: Tuple[Tuple, bool, Tuple], problem: SystemRepairProblem
):
    """
    Your heuristic for the SystemRepairProblem.

    state: (position, hasKit, pendingSystems)
    problem: SystemRepairProblem instance

    This must be admissible and preferably consistent.

    Hints:
    - Use problem.heuristicInfo to cache expensive computations
    - Go with some simple heuristics first, then build up to more complex ones
    - Consider the kit, pending systems, and the final return to control center
    - Balance heuristic strength vs. computation time (do experiments!)
    """
    
    position, hasKit, pendingSystems = state

    required = list(pendingSystems)
    if not hasKit:
        required.append(problem.kitPosition)
    required.append(problem.controlPosition)

    return max(
        abs(position[0] - p[0]) + abs(position[1] - p[1])
        for p in required
    )
