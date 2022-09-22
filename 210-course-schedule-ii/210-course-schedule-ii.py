class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        visited = [0 for _ in range(numCourses)]
        result = []
        for x,y in prerequisites:
            graph[x].append(y)
        
        def dfs(node):
            if visited[node] == -1:
                return False
            if visited[node] == 1:
                return True
            
            visited[node] = -1
            for i in graph[node]:
                if not dfs(i):
                    return False
                
            result.append(node)
            visited[node] = 1
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return result
            