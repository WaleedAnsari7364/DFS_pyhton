ACTIONS = [(0, 1, 2), (1, 0, 2), (1, 1, 3)]  # Actions: right, up, diagonal up-right

def read_maze(filename):
    with open(filename, 'r') as file:
        rows, cols = map(int, file.readline().split())
        start = tuple(map(int, file.readline().split()))
        goal = tuple(map(int, file.readline().split()))
        maze = [list(map(int, line.strip())) for line in file]
    return rows, cols, start, goal, maze

def is_valid_move(rows, cols, maze, visited, row, col):
    return 0 <= row < rows and 0 <= col < cols and maze[rows - row - 1][col] == 0 and (row, col) not in visited

def dfs(start, goal, maze):
    rows=len(maze)
    cols=len(maze[0])
    stack = [(start, [start], 0)] 
    visited = set()
    
    while stack:
        current_pos, path, cost = stack.pop()
        visited.add(current_pos)
        
        if current_pos == goal:
            return path, cost
        
        for dr, dc, move_cost in ACTIONS:
            new_row, new_col = current_pos[0] + dr, current_pos[1] + dc
            new_pos = (new_row, new_col)
            new_cost = cost + move_cost
            if is_valid_move(rows, cols, maze, visited, new_row, new_col):
                new_path = path + [new_pos]
                stack.append((new_pos, new_path, new_cost))
    
    return None, None

def display_path(rows, cols, maze, path):
    for r in range(rows):
        for c in range(cols):
            if (rows - r - 1, c) in path:
                print('*', end=' ')
            else:
                print(maze[r][c], end=' ')
        print()
# MAIN
filename = input("Enter Filename: ")
rows, cols, start, goal, maze = read_maze(filename)
print("Rows:", rows)
print("Cols:", cols)
print("Start coordinates:", start)
print("Goal coordinates:", goal)
print("Maze:")
for i in maze:
    print(i)

found_path, min_cost = dfs(start, goal, maze)
if found_path:
    print("Minimum cost:", min_cost)
    print("Path found:")
    print("Path: ", found_path)
    display_path(rows, cols, maze, found_path)
    
else:
    print("No path found.")
