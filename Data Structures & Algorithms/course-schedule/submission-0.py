class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashMap = {}

        for a, b in prerequisites:
            if a not in hashMap:
                hashMap[a] = {b}
            else:
                hashMap[a].add(b)

        def dfs(i, path):
            # Cycle found
            if i in path:
                return False

            # No prerequisites
            if i not in hashMap:
                return True

            path.add(i)

            for nei in hashMap[i]:
                if not dfs(nei, path):
                    return False

            path.remove(i)
            return True

        for i in range(numCourses):
            path = set()
            if not dfs(i, path):
                return False

        return True