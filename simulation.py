import random
import csv
from goalStates import winner

BOARD_SIZE = 5

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

class MinimaxAgent:
    def __init__(self, marker, depth):
        self.marker = marker
        self.opponent = 'O' if marker == 'X' else 'X'
        self.depth = depth
        self.cache = {}

    def minimax(self, board, depth, alpha, beta, is_maximizing):
        state = tuple(tuple(r) for r in board)
        if state in self.cache:
            return self.cache[state]
        if winner(board, self.marker):
            return 1
        if winner(board, self.opponent):
            return -1
        if is_full(board) or depth == 0:
            return 0
        if is_maximizing:
            best = -float('inf')
            for i in range(BOARD_SIZE):
                for j in range(BOARD_SIZE):
                    if board[i][j] == ' ':
                        board[i][j] = self.marker
                        val = self.minimax(board, depth-1, alpha, beta, False)
                        board[i][j] = ' '
                        best = max(best, val)
                        alpha = max(alpha, val)
                        if beta <= alpha:
                            break
            self.cache[state] = best
            return best
        else:
            best = float('inf')
            for i in range(BOARD_SIZE):
                for j in range(BOARD_SIZE):
                    if board[i][j] == ' ':
                        board[i][j] = self.opponent
                        val = self.minimax(board, depth-1, alpha, beta, True)
                        board[i][j] = ' '
                        best = min(best, val)
                        beta = min(beta, val)
                        if beta <= alpha:
                            break
            self.cache[state] = best
            return best

    def get_move(self, board):
        best_score = -float('inf')
        best_move = None
        self.cache.clear()
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == ' ':
                    board[i][j] = self.marker
                    score = self.minimax(board, self.depth, -float('inf'), float('inf'), False)
                    board[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move

class RandomCPU:
    def __init__(self, marker):
        self.marker = marker

    def get_move(self, board):
        empties = [(i, j) for i in range(BOARD_SIZE) for j in range(BOARD_SIZE) if board[i][j] == ' ']
        return random.choice(empties) if empties else None

def simulate_game(bot1, bot2):
    board = [[' ']*BOARD_SIZE for _ in range(BOARD_SIZE)]
    turn = 0
    while True:
        current = bot1 if turn % 2 == 0 else bot2
        move = current.get_move(board)
        if not move:
            return 'Draw'
        board[move[0]][move[1]] = current.marker
        if winner(board, current.marker):
            return current.marker
        if is_full(board):
            return 'Draw'
        turn += 1

def main():
    depths = [1, 2, 3, 4, 5]
    num_games = 1000
    results = []
    for depth in depths:
        print(f"Running depth {depth} Minimax vs Random")
        m = MinimaxAgent('X', depth)
        r = RandomCPU('O')
        xwins = owins = draws = 0
        for i in range(num_games):
            res = simulate_game(m, r)
            if res == 'X':
                xwins += 1
            elif res == 'O':
                owins += 1
            else:
                draws += 1
            if (i+1) % 100 == 0:
                print(f"  Random match: {i+1}/{num_games}")
        print(f"Depth {depth} Minimax vs Random results: X_wins={xwins}, O_wins={owins}, Draws={draws}")
        results.append({'depth': depth, 'opponent': 'random', 'X_wins': xwins, 'O_wins': owins, 'Draws': draws})

        print(f"Running depth {depth} Minimax vs Minimax")
        m1 = MinimaxAgent('X', depth)
        m2 = MinimaxAgent('O', depth)
        xwins = owins = draws = 0
        for i in range(num_games):
            res = simulate_game(m1, m2)
            if res == 'X':
                xwins += 1
            elif res == 'O':
                owins += 1
            else:
                draws += 1
            if (i+1) % 100 == 0:
                print(f"  Minimax match: {i+1}/{num_games}")
        print(f"Depth {depth} Minimax vs Minimax results: X_wins={xwins}, O_wins={owins}, Draws={draws}")
        results.append({'depth': depth, 'opponent': 'minimax', 'X_wins': xwins, 'O_wins': owins, 'Draws': draws})

    with open('/Users/chriszinati/Desktop/CPSC-481/CPSC-481-5x5-tic-tac-toe-/simulation_results.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['depth', 'opponent', 'X_wins', 'O_wins', 'Draws'])
        writer.writeheader()
        writer.writerows(results)
    print("Results written to simulation_results.csv")

if __name__ == '__main__':
    main()
