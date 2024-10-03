class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr = summ = 0
        sign = 1
        
        for item in s:
            if item == ' ':
                continue

            if item.isdigit():
                curr = curr * 10 + int(item)
            elif item in ('+', '-'):
                summ += (sign * curr)

                sign = 1 if item == '+' else -1

                curr = 0

            elif item == '(':
                stack.append(summ)
                stack.append(sign)

                sign = 1

                summ = 0

            else:
                summ += sign * curr
                summ *= stack.pop()
                summ += stack.pop()

                curr = 0

        return summ + (sign * curr)
        