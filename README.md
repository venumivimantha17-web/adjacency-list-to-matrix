# Adjacency List to Matrix Converter

A simple Python implementation that converts an adjacency list representation of an unweighted graph into an adjacency matrix.

## Description

An adjacency list represents a graph using a dictionary where each key represents a node and its value contains a list of neighboring nodes.

This project converts that representation into an adjacency matrix, where:

- `1` represents an edge between two nodes.
- `0` represents no edge.

The function also prints each row of the generated matrix and returns the complete matrix.

## Example

### Input

```python
{
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [2]
}
