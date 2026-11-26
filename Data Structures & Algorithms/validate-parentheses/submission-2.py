class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for n in s:
            if n in pairs:
                if not stack or stack[-1] != pairs[n]:
                    return False
                stack.pop()
            else:
                stack.append(n)
        return len(stack) == 0
                


        