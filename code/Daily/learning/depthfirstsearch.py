''' depth first search '''


def dfs_iterative(graph, start):
    ''' depth first search iterative'''
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


def dfs_recursive(graph, node, visited=None):
    ''' depth forst search recursive '''
    if visited is None:
        visited = set()

    # Mark the current node as visited
    visited.add(node)
    print(node)

    # Recur for all the adjacent nodes
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


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
    dfs_recursive(graph, 'A')
    dfs_iterative(graph, 'A')


if __name__ == "__main__":
    main()
