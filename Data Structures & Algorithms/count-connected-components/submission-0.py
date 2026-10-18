class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()   
        graph = {i:[] for i in range(n)}     
        count = 0
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbour in graph[node]:
                dfs(neighbour)
        for i in range(n):
            if i in visited:
                continue
            count+=1
            dfs(i)
        return count
        