class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashMap = {}

        for a, b in prerequisites:
            if a not in hashMap:
                hashMap[a] = {b}
            else:
                hashMap[a].add(b)

        def dfs(i, path):
            if i in path:
                return False

            if i not in hashMap:
                return True

            path.add(i)

            for n in hashMap[i]:
                if not dfs(n, path):
                    path.remove(i)
                    return False

            path.remove(i)
            return True

        for i in range(numCourses):
            if not dfs(i, set()):
                return False

        return True