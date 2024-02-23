# Topological Sort Project

This project implements a topological sort algorithm for directed acyclic graphs (DAGs), with a specific requirement to prioritize certain vertices in the ordering process.

## Overview

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge `u v`, vertex `u` comes before `v` in the ordering. This project includes a custom implementation of the topological sort that follows a specific sequence provided in the assignment.
![image](https://github.com/karamkhan1/Topological-Sort/assets/79159011/0b336e4f-468d-4c90-a7f5-96f1f64db84a)
![image](https://github.com/karamkhan1/Topological-Sort/assets/79159011/47d277d4-e9f2-4b9a-a7ff-ffe127105ab1)
## Implementation Details

The implementation consists of two main functions:

- `in_degree(dag, v)`: Calculates the in-degree of a vertex `v` in the graph `dag`.
- `topo(dag)`: Computes the topological ordering of the graph `dag`, ensuring that vertex `2` is processed right after vertex `0`.

## Usage

To use these functions, simply define the adjacency list representation of your DAG and call the `topo` function.

Example:

```python
test_dag = [[1, 2], [3, 4], [4], [], [3]]
topological_order = topo(test_dag)
print(topological_order)  # Expected output: [0, 2, 1, 4, 3]
