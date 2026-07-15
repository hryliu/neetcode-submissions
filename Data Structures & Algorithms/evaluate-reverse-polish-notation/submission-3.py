class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens: return 0

        stack = deque()
        
        for t in tokens:
            if t not in ['+', '-', '*', '/']:
                stack.append(t)

            else:
                x = int(stack.pop())
                y = int(stack.pop())
                if t == '+':
                    total = y + x
                elif t == '-':
                    total = y - x
                elif t == '*':
                    total = y * x
                else:
                    total = y / x
                
                stack.append(total)

        return int(stack[0])

