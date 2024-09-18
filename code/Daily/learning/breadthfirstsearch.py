''' breadth first search '''
from collections import deque


def breadth_first_search(graph, start):
    ''' breadth first search '''
    # Create a queue for BFS and enqueue the starting node
    queue = deque([start])

    # Set to keep track of visited nodes
    visited = set()

    # Mark the start node as visited
    visited.add(start)

    # Continue until the queue is empty
    while queue:
        # Dequeue a node from the queue
        node = queue.popleft()
        print(node)  # Process the node (print it here)

        # Get all adjacent nodes (neighbors)
        for neighbor in graph[node]:
            # If the neighbor hasn't been visited, enqueue it and mark as visited
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)


def main():
    ''' main function '''
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
    breadth_first_search(graph, 'A')


if __name__ == "__main__":
    main()
