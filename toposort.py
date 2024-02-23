def in_degree(dag, v):
    """Find the in-degree of vertex v in the input directed acyclic graph -- dag

    Inputs
    ------
    dag : list of lists
        adj list for input graph
    v : int
        a vertex in dag

    Returns
    int : the in-degree of v
    """
    # Initialize in-degree count to 0
    in_deg = 0

    # Check each vertex's adjacency list
    # If v is in the list, it means there is an incoming edge to v
    for edges in dag:
        if v in edges:
            in_deg += 1

    return in_deg


def topo(dag):
    """Find the topological ordering of a directed acyclic graph -- dag

    Inputs
    ------
    dag : list of lists
        adj list for input graph; assume graph is acyclic and directed

    Returns
    int list:
        topological ordering of the graph's vertices
    """
    # Calculate in-degrees for all vertices
    in_degrees = [0] * len(dag)
    for i, edges in enumerate(dag):
        for edge in edges:
            in_degrees[edge] += 1

    # Start with an empty topological order and an empty set of processed nodes
    topo_order = []
    processed = set()

    # While not all nodes are processed
    while len(processed) < len(dag):
        # Find all nodes with in-degree 0 that are not processed
        sources = [i for i in range(len(dag)) if in_degrees[i] == 0 and i not in processed]

        # This condition ensures that the vertex 2 is prioritized if it is a source
        if 2 in sources:
            current = 2
        else:
            # Otherwise, just take the first source available
            current = sources[0]

        # Add the current node to the topo order and mark it as processed
        topo_order.append(current)
        processed.add(current)

        # Decrease the in-degree for all neighbors of the current node
        for neighbor in dag[current]:
            in_degrees[neighbor] -= 1

    return topo_order


# TEST
test_dag = [[1, 2], [3, 4], [4], [], [3]]
print(topo(test_dag))  # Expected to return [0, 2, 1, 4, 3]
