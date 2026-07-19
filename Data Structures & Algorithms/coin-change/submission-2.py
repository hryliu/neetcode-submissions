class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins: return -1
        if amount == 0: return 0

        queue = deque()
        visited = {0}

        for c in coins:
            queue.append((c, 1)) # total, coins used
            visited.add(c)
        
        def bfs(queue) -> int:
            while queue:
                for _ in range(len(queue)):
                    total, num_coins = queue.popleft()

                    if total == amount: 
                        return num_coins
                    for c in coins:
                        if c + total <= amount and c + total not in visited: 
                            queue.append((c + total, num_coins + 1))
                            visited.add(c + total)

            return -1

        return bfs(queue)
            