class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = {i: [] for i in range(n)}
        
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
            
        def dfs(i):
            for v in graph.pop(i, []):
                dfs(v)
        
        dfs(0)
        return not graph
        