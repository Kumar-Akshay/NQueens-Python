import heapq

class Node:
    def __init__(self, state, parent=None):
        self.state = state  # Current state (positions of queens)
        self.parent = parent  # Parent node
        self.g = len(state)  # Cost function: Number of queens on the board
        self.h = N - len(state)  # Heuristic: Number of queens left to place
        self.f = self.g + self.h  # Total cost

    def __lt__(self, other):
        return self.f < other.f

def is_valid_state(state):
    current_row = len(state) - 1
    for row, col in enumerate(state[:-1]):
        diff = abs(col - state[-1])
        if diff == 0 or diff == current_row - row:
            return False
    return True

def get_children(node):
    children = []
    for col in range(N):
        new_state = node.state + [col]
        if is_valid_state(new_state):
            children.append(Node(new_state, node))
    return children

def print_solution_matrix(solution):
    """ Print the solution in a matrix format. """
    n = len(solution)
    matrix = [[". " for _ in range(n)] for _ in range(n)]
    for col, row in enumerate(solution):
        matrix[row][col] = "Q "
    for row in matrix:
        print("".join(row))



def a_star(N):
    start_node = Node([])

    open_set = []
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)
        if current_node.g == N:
            return current_node

        for child in get_children(current_node):
            heapq.heappush(open_set, child)

    return None

def print_board(state):
    N = len(state)
    for row in range(N):
        line = ""
        for col in range(N):
            if col == state[row]:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]  # Return reversed path

# Solve the N-Queens problem
N = 8  # Change this value for different sizes of the chessboard
solution_node_with_print = a_star(N)

if solution_node_with_print:
    print("Solution for the N-Queens problem:")
    print_solution_matrix(solution_node_with_print.state)
else:
    print("No solution found for N =", N)
