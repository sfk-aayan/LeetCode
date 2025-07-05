class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()

        for item in s:
            if item == ']':
                currStr = ''
                while stack[-1] != '[':
                    currStr = stack.pop() + currStr
                stack.pop()
                currDigit = ''
                while stack and stack[-1] not in ('[', ']') and stack[-1].isdigit():
                    currDigit = stack.pop() + currDigit
                currStr = int(currDigit) * currStr
                stack.append(currStr)
            else:
                stack.append(item)

        return "".join(stack)