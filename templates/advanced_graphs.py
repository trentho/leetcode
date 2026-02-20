from __future__ import annotations

import heapq


def dijkstra(n: int, edges: list[tuple[int, int, int]], start: int) -> list[int]:
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))

    dist = [10**18] * n
    dist[start] = 0
    pq: list[tuple[int, int]] = [(0, start)]

    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for nei, w in adj[node]:
            nd = d + w
            if nd < dist[nei]:
                dist[nei] = nd
                heapq.heappush(pq, (nd, nei))

    return dist


def topological_sort(n: int, edges: list[tuple[int, int]]) -> list[int]:
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        adj[u].append(v)
        indeg[v] += 1

    queue = [i for i in range(n) if indeg[i] == 0]
    out: list[int] = []

    i = 0
    while i < len(queue):
        node = queue[i]
        i += 1
        out.append(node)
        for nei in adj[node]:
            indeg[nei] -= 1
            if indeg[nei] == 0:
                queue.append(nei)

    return out if len(out) == n else []
