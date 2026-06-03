class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [ i for i in range(n+1)]

        def find(node):
            if parent[node] == node:
                return node
            
            parent[node] = find(parent[node])
            return parent[node]
        def union(node1,node2):
            root1 = find(node1)
            root2 = find(node2)

            if root1 == root2:
                # Both have the same parent so there's a cycle
                return False
            
            parent[root1] = root2
            return True
        
        for u,v in edges:
            if not union(u,v):
                return [u,v]
            
