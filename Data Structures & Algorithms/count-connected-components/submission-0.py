from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
            hashMap = {}
            visited = set()

            for a, b in edges:
                if a not in hashMap:
                    hashMap[a] = set()
                if b not in hashMap:
                    hashMap[b] = set()

                hashMap[a].add(b)
                hashMap[b].add(a)

            result = 0
            queue = deque()
            def bfs(i):
                nonlocal result
                if i in visited:
                    return
                
                if i not in hashMap:
                    result+=1
                    return 
                
                queue.append(i)
                visited.add(i)
                while queue:
                    a = queue.popleft()
                    for neighbor in hashMap[a]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                    
                result+=1
        
            for i in range(n):
                bfs(i)
            
            return result