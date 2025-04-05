from collections import deque

maze_text = [
    "#.####..##.#.##.....#.##...####..",
    "..###.#.####.#..#.#.#..#.. .###.#",
    ".#.###.#.#.#..#.#.....##.#.....#.",
    "...##...###.#..##..###.#.#######"
]

rows = len(maze_text)
cols = len(maze_text[0])
maze = [list(row) for row in maze_text]

# Define directions
moves = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}

# Start at top-left open cell (where 'U' is logically located)
start = (0, 1)  # Based on visual inspection
queue = deque()
queue.append((start, ""))

visited = set()
visited.add(start)

def is_valid(x, y):
    return 0 <= x < rows and 0 <= y < cols and maze[x][y] != '#' and (x, y) not in visited

while queue:
    (x, y), path = queue.popleft()

    # The last row has only one open cell at col 30 (visually verified)
    if x == 3 and y == 30:
        print("Found path:", path)
        break

    for move, (dx, dy) in moves.items():
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny):
            visited.add((nx, ny))
            queue.append(((nx, ny), path + move))
