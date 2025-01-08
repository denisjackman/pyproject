# Dijkstra’s Algorithm

This algorithm finds the shortest path between nodes in a graph, which is often represented using an adjacency list or matrix. Below is a sample implementation using an adjacency list and a priority queue to efficiently select the next node to visit:

## Dijkstra's Algorithm in Python

```
import heapq

def dijkstra(graph, start):
    # Initialize distances dictionary, setting the distance to the start node as 0 and all others as infinity
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Priority queue to explore the node with the smallest distance
    priority_queue = [(0, start)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip processing if we've already found a better path
        if current_distance > distances[current_node]:
            continue

        # Check neighbors and update their distances if a shorter path is found
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Only consider this new path if it's shorter
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)],
}

start_node = 'A'
distances = dijkstra(graph, start_node)
print(f"Shortest distances from {start_node}: {distances}")
```

## Explanation

* **Graph Representation**:The graph is represented as an adjacency list where each key is a node and the value is a list of tuples representing neighboring nodes and the weight (or distance) to them.
* **Priority Queue**: We use heapq to implement a priority queue that always processes the node with the smallest known distance.
* **Distances Dictionary**: This keeps track of the shortest known distance from the starting node to each other node. Initially, all distances are set to infinity except the start node, which is set to 0.
* **Main Loop**: At each step, the algorithm picks the node with the smallest distance, updates its neighbors' distances, and repeats until all nodes have been processed.

This implementation has a time complexity of O((V + E) log V) where V is the number of vertices and E is the number of edges.
