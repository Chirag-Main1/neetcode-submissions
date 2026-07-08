class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for s,d,w in edges:
            adj[s].append((d,w))
            adj[d].append((s,w))

        visit = set()
        visit.add(0)
        mst = 0
        mst1 = []
        minHeap = []
        for n1, w in adj[0]:
            heapq.heappush(minHeap,[w,0,n1])

        # print(adj)
        # print(minHeap)

        while minHeap:
            w,s,d = heapq.heappop(minHeap)

            if d in visit:
                continue

            mst += w
            visit.add(d)
            mst1.append((s,d))

            for no, w in adj[d]:
                if no not in visit:
                    heapq.heappush(minHeap,[w,s,no])
        
        print(len(mst1) , n-1)
        if len(mst1) == n-1:
            return mst
        else: 
            return -1