# Main idea for part one
# Read input.txt file. 
# It contains multiple lines of text that is composed of only 2 possible characters "." and "@". 
# "." should be parsed as 0 and "@" should be parsed as 1. 
# This way program should load file data into cartesian collection of zeros and ones. 
# That cartesian collection is going to be input for processing logic. 
# Program needs to count nodes that fulfill following rules:
# 1. value is 1
# 2. Sum of neighbour nodes values is less then 4
# Neighbour nodes are 8 possible nodes around current node (top, bottom, left, right and 4 diagonals)
# When accessing neighbour nodes to sum their value skip accessing indexes that would get out of range for input table

# Main idea for part two
# Read input.txt file and parse it the same way as in part one. 
# New function needs to count nodes like count_accessible_nodes function 
# but it needs to create and seed new grid of the same size as input grid but the values set based on following rules:
# 1. value is 1 and fullfill condition of part one then set value to 0
# 2. value is 1 and does not fullfill condition of part one then set value to 1
# 3. value is 0 then set value to 0
# Function should call itself recurently with new grid if nodes count is greater then zero and aggregate result

# Define 8 neighbor directions: up, down, left, right, and 4 diagonals
NEIGHBOR_DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),  # top-left, top, top-right
    (0, -1),           (0, 1),    # left, right
    (1, -1),  (1, 0),  (1, 1)     # bottom-left, bottom, bottom-right
]

def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.read().strip().split('\n')
    
    grid = []
    for line in lines:
        row = []
        for char in line:
            if char == '.':
                row.append(0)
            elif char == '@':
                row.append(1)
        grid.append(row)
    
    return grid


def count_nodes_with_value_one(grid):
    count = 0
    for row in grid:
        for value in row:
            if value == 1:
                count += 1
    return count


def get_neighbor_sum(grid, row, col, rows, cols, directions=None):
    neighbor_sum = 0
    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc
        
        if 0 <= new_row < rows and 0 <= new_col < cols:
            neighbor_sum += grid[new_row][new_col]
    
    return neighbor_sum


def count_accessible_nodes(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    count = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                neighbor_sum = get_neighbor_sum(grid, row, col, rows, cols, NEIGHBOR_DIRECTIONS)
                if neighbor_sum < 4:
                    count += 1
    
    return count


def count_accessible_nodes_recursive(grid, iteration=1):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    current_count = 0
    new_grid = []
    
    for row in range(rows):
        new_row = []
        for col in range(cols):
            if grid[row][col] == 1:
                neighbor_sum = get_neighbor_sum(grid, row, col, rows, cols, NEIGHBOR_DIRECTIONS)
                if neighbor_sum < 4:
                    current_count += 1
                    new_row.append(0)
                else:
                    new_row.append(1)
            else:
                new_row.append(0)
        new_grid.append(new_row)
    
    print(f"Iteration {iteration}: {current_count} accessible nodes")
    
    if current_count == 0:
        return current_count
    
    return current_count + count_accessible_nodes_recursive(new_grid, iteration + 1)


def main():
    grid = read_input('input.txt')
    
    if grid:
        print(f"Grid dimensions: {len(grid)} rows x {len(grid[0])} columns")

    result1 = count_nodes_with_value_one(grid)
    print(f"Number of nodes with value 1: {result1}")
    
    result2 = count_accessible_nodes(grid)
    print(f"Number of nodes with value 1 and neighbor sum < 4: {result2}")
    
    print("\n--- Part Two: Recursive counting ---")
    result3 = count_accessible_nodes_recursive(grid)
    print(f"Total aggregated accessible nodes across all iterations: {result3}")

if __name__ == "__main__":
    main()
