# Grid representation
grid = [[0, 0, 0, 0],
        [0, "M", "S", 0],
        [0, "G", 0, 0],
        [0, 0, 0, 0]]

# Starting position
start_pos = (0, 0)

# Function to check if a given position is valid
def is_valid(pos, grid, visited):
    row, col = pos
    if row < 0 or col < 0:
        return False
    if row >= len(grid) or col >= len(grid[0]):
        return False
    if grid[row][col] == "M" or visited[row][col]:
        return False
    return True

# Function to detect smell
def detect_smell(pos, grid):
    row, col = pos
    if grid[row][col] == "S":
        return True
    return False

# Function to check if gold is found
def check_gold(pos, grid):
    row, col = pos
    if grid[row][col] == "G":
        return True
    return False

# Function to traverse the grid using DFS
def traverse_grid(pos, grid, visited, smell_detected):
    if check_gold(pos, grid):
        return True
    if not is_valid(pos, grid, visited):
        return False
    if not smell_detected:
        smell_detected = detect_smell(pos, grid)
    visited[pos[0]][pos[1]] = True
    # Move in all four directions
    if traverse_grid((pos[0]+1, pos[1]), grid, visited, smell_detected):
        return True
    if traverse_grid((pos[0]-1, pos[1]), grid, visited, smell_detected):
        return True
    if traverse_grid((pos[0], pos[1]+1), grid, visited, smell_detected):
        return True
    if traverse_grid((pos[0], pos[1]-1), grid, visited, smell_detected):
        return True
    return False

# Initialize visited array
visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

# Output result to file
smell_detected = False
with open("output.txt", "w") as f:
    if traverse_grid(start_pos, grid, visited, smell_detected):
        f.write("Gold found and avoided the monster")
    else:
        f.write("Gold not found or monster encountered")