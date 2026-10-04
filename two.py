def is_safe(board, row, col, n):
    for c in range(col):
        if board[row][c] == 1:
            return False
            
    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1
        
    r, c = row, col
    while r < n and c >= 0:
        if board[r][c] == 1:
            return False
        r += 1
        c -= 1
        
    return True

def solve_n_queens_util(board, col, n, solutions):
    if col >= n:
        solution_copy = [row[:] for row in board]
        solutions.append(solution_copy)
        return
        
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_util(board, col + 1, n, solutions)
            board[row][col] = 0

def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print()

def main():
    n = 4
    print(f"N-Queens Problem Solver using Backtracking (N = {n})")
    
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    
    print(f"Total Unique Solutions Found: {len(solutions)}\n")
    for idx, sol in enumerate(solutions, 1):
        print(f"--- Solution {idx} ---")
        print_board(sol)

if __name__ == '__main__':
    main()
