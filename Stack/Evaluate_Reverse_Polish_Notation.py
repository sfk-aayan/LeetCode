class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = set(('+','-','/','*'))

        for item in tokens:
            if item in operators:
                operand1 = int(stack.pop())
                operand2 = int(stack.pop())

                if item == '+':
                    stack.append(operand2 + operand1)

                elif item == '-':
                    stack.append(operand2 - operand1)
        
                elif item == '/':
                    stack.append(operand2 / operand1)
                    
                else:
                    stack.append(operand2 * operand1)

            else:
                stack.append(item)

        return int(stack[0])


        