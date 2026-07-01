class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {}
        rank = {}
        for i in range(1,n+1):
            if i not in parent:
                parent[i] = i

        for i in range(1,n+1):
            if i not in rank:
                rank[i] = 0

        
        def find(x):
            if parent[x] == x:
                return x
            else:
                parent[x] = find(parent[x])
                return parent[x]

        def union(a,b):
            if find(a) == find(b):
                return False     

            a = find(a)
            b = find(b)
            if rank[a] > rank[b]:
                parent[b] = a
            elif rank[a] < rank[b]:
                parent[a] = b
            else:
                parent[b] = a
                rank[a] += 1
            return True 
        
        for a,b in edges:
            if not union(a,b):
                return [a,b]

    # def __init__(self, n: int):
    #     self.parent = {}
    #     self.rank = {}
    #     self.n = n
    #     for i in range(self.n):
    #         if i not in self.parent:
    #             self.parent[i] = i

    #     for i in range(self.n):
    #         if i not in self.rank:
    #             self.rank[i] = 0


    # def find(self, x: int) -> int:
    #     if self.parent[x] == x:
    #         return x
    #     else:
    #         self.parent[x] = self.find(self.parent[x])
    #         return self.parent[x]
        

    # def isSameComponent(self, x: int, y: int) -> bool:
    #     return self.find(x) == self.find(y)


    # def union(self, x: int, y: int) -> bool:
    #     if self.find(x) == self.find(y):
    #         return False
    #     else:
    #         x = self.find(x)
    #         y = self.find(y)
    #         if self.rank[x] > self.rank[y]:
    #             self.parent[y] = self.parent[x]

    #         elif self.rank[x] < self.rank[y]:
    #             self.parent[x] = self.parent[y]
            
    #         else:
    #             self.parent[y] = self.parent[x]
    #             self.rank[x] += 1
            
    #         return True

    # def getNumComponents(self) -> int:
    #     a = 0
    #     for i in range(self.n):
    #         if self.parent[i] == i:
    #             a += 1   
    #     return a


