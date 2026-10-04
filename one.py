from collections import deque

def get_valid_moves(state):
    pegs = [list(p) for p in state]
    moves = []
    
    for src in range(3):
        if not pegs[src]:
            continue
        disk = pegs[src][-1]
        for dest in range(3):
            if src == dest:
                continue
            if not pegs[dest] or pegs[dest][-1] > disk:
                new_pegs = [list(p) for p in state]
                moved_disk = new_pegs[src].pop()
                new_pegs[dest].append(moved_disk)
                next_state = tuple(tuple(p) for p in new_pegs)
                move_desc = f"Move disk {disk} from Peg {chr(65 + src)} to Peg {chr(65 + dest)}"
                moves.append((next_state, move_desc))
                
    return moves

def solve_tower_of_hanoi_state_space(n_disks):
    start_state = (tuple(range(n_disks, 0, -1)), (), ())
    goal_state = ((), (), tuple(range(n_disks, 0, -1)))
    
    queue = deque([(start_state, [])])
    visited = {start_state}
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state == goal_state:
            return path + [(None, current_state)]
            
        for next_state, action in get_valid_moves(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [(action, current_state)]))
                
    return None

def format_state(state):
    return f"A:{list(state[0])} | B:{list(state[1])} | C:{list(state[2])}"

def main():
    n_disks = 3
    print("Tower of Hanoi Problem via State-Space Search")
    print(f"Number of Disks: {n_disks}")
    
    solution = solve_tower_of_hanoi_state_space(n_disks)
    if solution:
        print(f"Initial State: {format_state(solution[0][1])}")
        print("Sequence of State Transitions:")
        for step_num, (action, st) in enumerate(solution[:-1], 1):
            next_st = solution[step_num][1] if step_num < len(solution) - 1 else solution[-1][1]
            print(f"Step {step_num:02d}: {action} => {format_state(next_st)}")
        print("Goal State Successfully Achieved!")
    else:
        print("No solution found.")

if __name__ == '__main__':
    main()
