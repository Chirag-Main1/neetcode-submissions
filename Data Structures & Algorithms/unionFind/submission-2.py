class UnionFind:
    
    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}
        self.n = n
        for i in range(self.n):
            if i not in self.parent:
                self.parent[i] = i

        for i in range(self.n):
            if i not in self.rank:
                self.rank[i] = 0


    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        

    def isSameComponent(self, x: int, y: int) -> bool:
        self.find(x)
        self.find(y)
        if self.parent[x] == self.parent[y]:
            return True
        else: return False


    def union(self, x: int, y: int) -> bool:
        if self.find(x) == self.find(y):
            return False
        else:
            x = self.find(x)
            y = self.find(y)
            if self.rank[x] > self.rank[y]:
                self.parent[y] = self.parent[x]

            elif self.rank[x] < self.rank[y]:
                self.parent[x] = self.parent[y]
            
            else:
                self.parent[y] = self.parent[x]
                self.rank[x] += 1
            
            return True

    def getNumComponents(self) -> int:
        a = 0
        for i in range(self.n):
            if self.parent[i] == i:
                a += 1   
        return a

