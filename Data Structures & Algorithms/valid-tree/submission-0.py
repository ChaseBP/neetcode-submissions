class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Valid tree conditions
        # Tree should have n-1 edges and Tree should be connected without any cycles
        if len(edges) != n - 1:
            return False
        # Creating adj list
        adj = {i: [] for i in range(n)}
        # Visited list
        visited = set()

        # Adding entries to the list (Undirected graph)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            if node in visited:
                return
            visited.add((node))

            for neighbor in adj[node]:
                dfs(neighbor)

        dfs(0)
        return len(visited) == n
