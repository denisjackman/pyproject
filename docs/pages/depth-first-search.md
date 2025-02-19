# Depth First Search (DFS)

## Recursive DFS

```
# Recursive DFS
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()

    # Mark the current node as visited
    visited.add(node)
    print(node)

    # Recur for all the adjacent nodes
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Example graph represented as an adjacency list (dictionary)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Starting DFS from node 'A'
dfs_recursive(graph, 'A')
```

## Iterative DFS

```
# Iterative DFS using a stack
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)
            
            # Add unvisited neighbors to the stack
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Starting DFS from node 'A'
dfs_iterative(graph, 'A')
```

## Explanation

### Alternate Recursive DFS

This function explores each node recursively.
It uses a set visited to track which nodes have been visited.
Each node and its neighbors are explored recursively.

### Alternate Iterative DFS

This uses a stack (a Last In First Out structure) to simulate the recursion.
It starts from the initial node and explores as deep as possible by popping from the stack.
You can choose between the two depending on your preference and use case. Both methods will perform DFS traversal of the graph.


Depth First Search (DFS) is a graph traversal algorithm used to explore nodes and edges of a graph. It works by starting at a given node and explores as far as possible along each branch before backtracking. DFS can be used to solve a variety of problems, such as pathfinding, cycle detection, or finding connected components.

#### Steps for Using Depth First Search (DFS)

* **Choose a Starting Node**: Begin at any arbitrary node in the graph from which you want to explore.
* **Visit the Node**: Mark the starting node as visited (typically by adding it to a visited set) to ensure that you do not visit the same node again.
* **Explore Neighbors**: For each unvisited neighbor of the current node, move to that neighbor and repeat the DFS process.
* **Backtrack**: If a node has no unvisited neighbors, backtrack to the previous node and explore its remaining neighbors (if any).
* **Repeat Until All Nodes are Visited**: Continue exploring and backtracking until you have visited all nodes in the connected component of the graph (or the entire graph, if it's connected).

## When to Use DFS

* **Pathfinding**: DFS can be used to find a path between two nodes.
* **Cycle Detection**: DFS can help identify cycles in a graph.
* **Topological Sorting**: In Directed Acyclic Graphs (DAGs), DFS can be used to sort nodes in a topological order.
* **Connected Components**: DFS is used to find all connected components in a graph.
* **Maze Solving**: DFS can help explore all possible paths in a maze, although it does not guarantee the shortest path.

## DFS Example Walkthrough

Given a graph represented as an adjacency list like this:

```
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
```

DFS Traversal (Recursive Example)
If we start at node 'A' and use DFS:

Visit node 'A'.

Mark 'A' as visited.
The neighbors of 'A' are 'B' and 'C'.
Move to node 'B' (first unvisited neighbor of 'A').

Visit 'B'.
The neighbors of 'B' are 'D' and 'E'.
Move to node 'D' (first unvisited neighbor of 'B').

Visit 'D'.
'D' has no neighbors, so backtrack to 'B'.
Now move to node 'E' (the next unvisited neighbor of 'B').

Visit 'E'.
The neighbor of 'E' is 'F'.
Move to node 'F' (unvisited neighbor of 'E').

Visit 'F'.
'F' has no neighbors, so backtrack to 'E', then to 'B', then to 'A'.
Back at 'A', now move to node 'C' (the next unvisited neighbor of 'A').

Visit 'C'.
The neighbor of 'C' is 'F', but 'F' has already been visited, so backtrack.
The DFS traversal order is: A -> B -> D -> E -> F -> C.

## Practical Applications of DFS

* **Pathfinding**: In games or AI problems, DFS can be used to explore all potential paths from one point to another.
* **Solving Puzzles**: DFS is commonly used in puzzle-solving, like exploring all possible moves in a maze.
* **Cycle Detection**: DFS can be used to detect cycles in directed and undirected graphs, which is useful in tasks like deadlock detection in operating systems.
* **Topological Sorting**: In scheduling problems or course prerequisites, DFS helps in performing topological sorting of DAGs.
* **Connected Components**: DFS can find all the nodes in a connected component of a graph, useful for network analysis.

### DFS Complexity

* **Time Complexity**: O(V + E) where V is the number of vertices (nodes) and E is the number of edges. This is because each node is visited once, and each edge is explored once.
* **Space Complexity**: O(V) due to the recursion stack in the recursive implementation (or the explicit stack in the iterative version).

### Key Points

DFS explores as deep as possible before backtracking, which contrasts with Breadth First Search (BFS), which explores neighbors level by level.
DFS can be implemented either recursively or iteratively using a stack.
DFS is useful for exploring large, deep graphs but may not find the shortest path in unweighted graphs. For shortest paths, BFS or Dijkstra’s algorithm are typically used.
