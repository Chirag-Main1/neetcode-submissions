class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # if not prerequisites:
#             return [False] * len(queries)
        
#         hashMap = {}
        
#         for a, b in prerequisites:
#             if a not in hashMap:
#                 hashMap[a] = {b}
#             else:
#                 hashMap[a].add(b)


#         def dfs(a,b,path):
#             if a not in hashMap:
#                 return False

#             if b in hashMap[a]:
#                 return True

#             if a in path:
#                 return False
            
#             if not hashMap[a]:
#                 return False
            
#             path.add(a)
#             for i in hashMap[a]:
#                 if dfs(i,b,path):
#                     hashMap[i].add(b)
#                     return True

#             path.remove(a)
#             return False

#         result = []
#         for a, b in queries:
#             if dfs(a,b,set()):
#                 hashMap[a].add(b)
#                 result.append(True)
#             else: result.append(False)

#         return result


            hashMap = {}

            for a, b in prerequisites:
                if a not in hashMap:
                    hashMap[a] = {b}
                else:
                    hashMap[a].add(b)

            memo = {}

            def dfs(a):
                if a in memo:
                    return memo[a]

                reachable = set()

                if a in hashMap:
                    for child in hashMap[a]:
                        reachable.add(child)
                        reachable |= dfs(child)

                memo[a] = reachable
                return reachable

            for i in range(numCourses):
                dfs(i)

            result = []
            for a, b in queries:
                result.append(b in memo[a])

            return result