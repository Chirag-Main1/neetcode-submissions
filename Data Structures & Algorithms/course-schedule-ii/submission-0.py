class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashMap = {}
        comp = []

        for a, b in prerequisites:
            if a not in hashMap:
                hashMap[a] = {b}
            else:
                hashMap[a].add(b)

        def dfs(i, path):
            nonlocal comp
            if i in path:
                return False

            if i not in hashMap:
                comp.append(i)
                return True

            path.add(i)

            for n in hashMap[i]:
                if n in comp:
                    continue
                if not dfs(n, path):
                    path.remove(i)
                    return False

            path.remove(i)
            comp.append(i)
            return True

        for i in range(numCourses):
            if i in comp:
                continue
            if not dfs(i, set()):
                return []

        return comp