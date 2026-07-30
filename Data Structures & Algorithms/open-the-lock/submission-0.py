class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends: return -1

        def get_children(lock) -> List[str]:
            res = []
            for i in range(4):
                digit = int(lock[i])
                temp_lock = lock[:i] + str((digit + 1) % 10) + lock[i+1:]
                res.append(temp_lock)

                digit = int(lock[i])
                temp_lock = lock[:i] + str((digit - 1) % 10) + lock[i+1:]
                res.append(temp_lock)

            return res

        queue = deque()
        queue.append(['0000', 0])
        visited = set(deadends)

        while queue:
            lock, step = queue.popleft()

            if lock == target:
                return step

            children = get_children(lock)
            for c in children:
                if c not in visited:
                    visited.add(c)
                    queue.append([c, step + 1])

        return -1
        
