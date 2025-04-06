''' Dijkstra's Algorythm '''
import heapq


def dijkstra(graph, start):
    ''' Dijkstra's Algo '''
    # Initialize distances dictionary,
    # setting the distance to the start node as 0 and all others as infinity
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


def main():
    ''' main function '''
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


if __name__ == "__main__":
    main()
