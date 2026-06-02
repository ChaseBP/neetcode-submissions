class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        visited = set()
        connected = 0 
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for neighbour in adj[node]:
                dfs(neighbour)
        
        for node in range(n):
            if node not in visited:
                connected += 1
                dfs(node)
        
        return connected