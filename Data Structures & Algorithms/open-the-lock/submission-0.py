from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)

        if "0000" in deadends:
            return -1

        queue = deque(["0000"])
        visited = {"0000"}
        dist = 0

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()

                if curr == target:
                    return dist

                for i in range(4):
                    digit = int(curr[i])

                    up = (digit + 1) % 10
                    down = (digit - 1) % 10

                    up_state = curr[:i] + str(up) + curr[i+1:]
                    down_state = curr[:i] + str(down) + curr[i+1:]

                    if up_state not in visited and up_state not in deadends:
                        visited.add(up_state)
                        queue.append(up_state)

                    if down_state not in visited and down_state not in deadends:
                        visited.add(down_state)
                        queue.append(down_state)

            dist += 1

        return -1