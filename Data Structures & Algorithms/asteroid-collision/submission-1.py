class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids) == 1:
            return [asteroids[0]]

        stack = []

        for a in asteroids:
            if not stack:
                stack.append(a)

            elif a > 0:
                stack.append(a)

            else:
                append_ast = True
                while stack and stack[-1] > 0:
                    max_a = stack[-1]

                    # asteroid at the top of the stack is destroyed
                    if max_a < abs(a):
                        stack.pop()

                    # both asteroids are destroyed
                    elif max_a == abs(a):
                        stack.pop()
                        append_ast = False
                        break
                    
                    else:
                        append_ast = False
                        break

                if append_ast:
                    stack.append(a)

        res = []
        while stack:
            res.append(stack.pop())
        res.reverse()

        return res

                
