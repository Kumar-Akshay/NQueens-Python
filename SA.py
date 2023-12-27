import random
import math

def compute_heuristic(state):
    """ Compute the number of pairs of queens attacking each other. """
    h = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            # Check if queens are in the same row or in the same diagonal
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                h += 1
    return h

def print_solution_matrix(solution):
    """ Print the solution in a matrix format. """
    n = len(solution)
    matrix = [[". " for _ in range(n)] for _ in range(n)]
    for col, row in enumerate(solution):
        matrix[row][col] = "Q "
    for row in matrix:
        print("".join(row))

def get_neighbor(state):
    """ Randomly move one queen to a different row in its column. """
    neighbor = state.copy()
    col = random.randint(0, len(state) - 1)
    row = random.randint(0, len(state) - 1)
    neighbor[col] = row
    return neighbor

def simulated_annealing(n):
    """ Perform simulated annealing to solve the N-Queens problem. """
    current_state = [random.randint(0, n - 1) for _ in range(n)]
    print("Initial State.....")
    print_solution_matrix(current_state)
    print("..........................................")
    current_heuristic = compute_heuristic(current_state)
    temperature = 1.0
    cooling_rate = 0.99
    step = 0

    while temperature > 0.0001:
        neighbor = get_neighbor(current_state)
        neighbor_heuristic = compute_heuristic(neighbor)

        if neighbor_heuristic < current_heuristic:
            current_state, current_heuristic = neighbor, neighbor_heuristic
            print_solution_matrix(current_state)
            print("..........................................")
            if current_heuristic == 0:
                # Solution found
                return current_state
        else:
            # Accept worse state with a certain probability
            if random.uniform(0, 1) < math.exp(-(neighbor_heuristic - current_heuristic) / temperature):
                current_state, current_heuristic = neighbor, neighbor_heuristic
                print_solution_matrix(current_state)
                print("..........................................")
        temperature *= cooling_rate
        step += 1

    return None  # No solution found

# Solving for a 4x4 board
n = 4
solution = simulated_annealing(n)
if solution:
    print("Simulated Annealing - Solution found:")
    print_solution_matrix(solution)
else:
    print("Simulated Annealing - No solution found.")
