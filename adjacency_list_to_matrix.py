def adjacency_list_to_matrix(adjacency_list):
    # Determine the number of nodes
    num_nodes = len(adjacency_list)

    # Create an empty adjacency matrix filled with 0s
    matrix = [[0] * num_nodes for _ in range(num_nodes)]

    # Add edges to the matrix
    for node, neighbors in adjacency_list.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1

    # Print each row
    for row in matrix:
        print(row)

    # Return the matrix
    return matrix
