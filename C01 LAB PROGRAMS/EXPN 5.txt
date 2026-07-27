#EXP:5 MISSIONARY CANIBALS

from collections import deque

def is_safe(m, c):
    if m > 0 and m < c:
        return False
    if (3 - m) > 0 and (3 - m) < (3 - c):
        return False
    return True

def bfs():
    start = (3, 3, 'L')
    goal = (0, 0, 'R')

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            print("Solution:")
            for s in path:
                print(s)
            return

        if state in visited:
            continue
        visited.add(state)

        m, c, boat = state

        moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

        for dm, dc in moves:
            if boat == 'L':
                nm, nc = m - dm, c - dc
                nb = 'R'
            else:
                nm, nc = m + dm, c + dc
                nb = 'L'

            if 0 <= nm <= 3 and 0 <= nc <= 3 and is_safe(nm, nc):
                new_state = (nm, nc, nb)
                if new_state not in visited:
                    queue.append((new_state, path + [new_state]))

bfs()
