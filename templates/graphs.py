from __future__ import annotations

from collections import deque


def bfs_path_exists(n: int, edges: list[tuple[int, int]], src: int, dst: int) -> bool:
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    q: deque[int] = deque([src])
    seen = [False] * n
    seen[src] = True

    while q:
        node = q.popleft()
        if node == dst:
            return True
        for nei in adj[node]:
            if not seen[nei]:
                seen[nei] = True
                q.append(nei)

    return False


def count_components(n: int, edges: list[tuple[int, int]]) -> int:
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    seen = [False] * n

    def dfs(node: int) -> None:
        seen[node] = True
        for nei in adj[node]:
            if not seen[nei]:
                dfs(nei)

    components = 0
    for i in range(n):
        if seen[i]:
            continue
        components += 1
        dfs(i)

    return components
