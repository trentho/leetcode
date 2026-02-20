from __future__ import annotations

from collections import deque

from .nodes import Node


def build_undirected_graph(adj_list: list[list[int]]) -> list[Node]:
    """Build graph nodes from adjacency list using 0-based indexing."""
    nodes = [Node(i) for i in range(len(adj_list))]
    for i, neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[n] for n in neighbors]
    return nodes


def edge_list_to_adj(n: int, edges: list[tuple[int, int]], directed: bool = False) -> list[list[int]]:
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        if not directed:
            adj[v].append(u)
    return adj


def weighted_edge_list_to_adj(
    n: int, edges: list[tuple[int, int, int]], directed: bool = False
) -> list[list[tuple[int, int]]]:
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        if not directed:
            adj[v].append((u, w))
    return adj


def bfs_order(adj: list[list[int]], start: int = 0) -> list[int]:
    seen = [False] * len(adj)
    q: deque[int] = deque([start])
    seen[start] = True
    order: list[int] = []

    while q:
        node = q.popleft()
        order.append(node)
        for nei in adj[node]:
            if not seen[nei]:
                seen[nei] = True
                q.append(nei)

    return order
