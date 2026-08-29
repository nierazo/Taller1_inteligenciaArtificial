from algorithms.problems import SearchProblem
import algorithms.utils as utils
from world.game import Directions
from algorithms.heuristics import nullHeuristic
from algorithms.utils import PriorityQueue, Stack, Queue


def tinyDiagnosticSearch(problem: SearchProblem):
    """
    Returns a hard-coded sequence of moves for the tinyDiagnostic layout.
    For any other station layout, the sequence of moves will be incorrect.
    """
    s = Directions.SOUTH
    e = Directions.EAST
    return [s, e, s, e, e, e, e, s, e, e, s, s, e, s, s, e, s, e, e, e, e, e, e, e]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    # TODO: Add your code here
    visitado = set()
    pila = Stack()

    pila.push((problem.getStartState(), []))

    while not pila.isEmpty():
        nodo, movimientos = pila.pop()

        if problem.isGoalState(nodo):
            return movimientos

        if nodo not in visitado:
            visitado.add(nodo)
            for sucesor, accion, costo in problem.getSuccessors(nodo):
                if sucesor not in visitado:
                    nueva_lista = movimientos + [accion]
                    pila.push((sucesor, nueva_lista))

    return None


def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.

    BFS must minimize the number of actions (moves), not the terrain cost.
    The frontier is FIFO, and a state is marked visited when it is enqueued,
    ensuring that the first time a state is discovered corresponds to the
    shortest path to it in an unweighted graph.
    """
    # TODO: Add your code here
    inicio = problem.getStartState()
    visitado = set()
    cola = Queue()
    
    visitado.add(inicio)
    
    cola.push((inicio, []))

    while not cola.isEmpty():
        nodo, movimientos = cola.pop()

        if problem.isGoalState(nodo):
            return movimientos

        for sucesor, accion, costo in problem.getSuccessors(nodo):
            if sucesor not in visitado:
                visitado.add(sucesor)
                cola.push((sucesor, movimientos + [accion]))

    return None


def uniformCostSearch(problem: SearchProblem):
    """
    Search the node of least total cost first.
    """

    # TODO: Add your code here
    visitado = set()
    priority_q = PriorityQueue()
    priority_q.push((problem.getStartState(), []), 0)

    while not priority_q.isEmpty():
        nodo, movimientos = priority_q.pop()
        if problem.isGoalState(nodo):
            return movimientos
        if nodo not in visitado:
            visitado.add(nodo)
            for sucesor, accion, costo in problem.getSuccessors(nodo):
                if sucesor not in visitado:
                    nueva_lista = movimientos + [accion]
                    priority_q.push((sucesor, nueva_lista), problem.getCostOfActions(nueva_lista))
    return None
    utils.raiseNotDefined()


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    visitado = set()
    priority_q = PriorityQueue()
    start = problem.getStartState()
    priority_q.push((start, [], 0), heuristic(start, problem))

    while not priority_q.isEmpty():
        nodo, movimientos, costo_g = priority_q.pop()

        if problem.isGoalState(nodo):
            return movimientos

        if nodo not in visitado:
            visitado.add(nodo)
            for sucesor, accion, stepCost in problem.getSuccessors(nodo):
                if sucesor not in visitado:
                    nuevo_costo_g = costo_g + stepCost
                    nueva_lista = movimientos + [accion]
                    prioridad = nuevo_costo_g + heuristic(sucesor, problem)
                    priority_q.push((sucesor, nueva_lista, nuevo_costo_g), prioridad)

    return None


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
