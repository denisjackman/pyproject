# A* Algorithm in Python

Here’s an implementation of the A* (A-star) search algorithm in Python. This algorithm finds the shortest path between a start and a goal node in a graph or grid, using heuristics to improve search efficiency.

```
import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Distance from start node
        self.h = 0  # Heuristic (estimated distance to goal)
        self.f = 0  # Total cost (g + h)
    
    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

def a_star_search(start, goal, grid):
    """
    A* search algorithm to find the shortest path in a 2D grid.
    
    :param start: Tuple representing the start position (row, col)
    :param goal: Tuple representing the goal position (row, col)
    :param grid: 2D list representing the grid (0 for free space, 1 for obstacles)
    :return: List of tuples representing the path from start to goal
    """
    
    def heuristic(a, b):
        """Heuristic function (Manhattan distance in this case)"""
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    open_list = []
    closed_list = set()
    
    start_node = Node(start)
    goal_node = Node(goal)
    
    heapq.heappush(open_list, start_node)
    
    while open_list:
        # Get the node with the lowest f score
        current_node = heapq.heappop(open_list)
        
        # If the goal is reached, reconstruct the path
        if current_node == goal_node:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path
        
        closed_list.add(current_node.position)
        
        # Generate neighbors (4 possible directions: up, down, left, right)
        neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for n in neighbors:
            neighbor_pos = (current_node.position[0] + n[0], current_node.position[1] + n[1])
            
            # Check if the neighbor is within the grid bounds
            if neighbor_pos[0] < 0 or neighbor_pos[0] >= len(grid) or neighbor_pos[1] < 0 or neighbor_pos[1] >= len(grid[0]):
                continue
            
            # Check if the neighbor is an obstacle
            if grid[neighbor_pos[0]][neighbor_pos[1]] == 1:
                continue
            
            # Check if the neighbor is in the closed list
            if neighbor_pos in closed_list:
                continue
            
            # Create the neighbor node
            neighbor_node = Node(neighbor_pos, current_node)
            
            # Calculate g, h, and f
            neighbor_node.g = current_node.g + 1
            neighbor_node.h = heuristic(neighbor_pos, goal_node.position)
            neighbor_node.f = neighbor_node.g + neighbor_node.h
            
            # Check if the neighbor is already in the open list with a lower f
            if any(neighbor_node == open_node and neighbor_node.f >= open_node.f for open_node in open_list):
                continue
            
            # Add the neighbor to the open list
            heapq.heappush(open_list, neighbor_node)
    
    return None  # No path found

# Example usage
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)
path = a_star_search(start, goal, grid)
print(f"Path: {path}")
```

## Explanation

* **Grid**: A 2D array where 0 represents a free space, and 1 represents an obstacle.
* **Node**: A class to represent each point in the grid with properties for the path cost g, heuristic h, and total cost f.
* **Open list**: A priority queue (min-heap) that stores nodes to be explored. Nodes with the lowest f value are prioritized.
* **Closed list**: A set of visited nodes that have already been explored.
* **Heuristic**: The Manhattan distance is used in this example to estimate the cost from a node to the goal.
* **Output**: This will output the shortest path from the start to the goal, avoiding obstacles.

You can adjust the grid and the start/goal positions as needed.