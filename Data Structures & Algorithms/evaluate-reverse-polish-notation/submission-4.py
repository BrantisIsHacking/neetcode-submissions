class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for i in tokens:
            if i == "+":
                num1 = s.pop()
                num2 = s.pop()
                sum = int(num1) + int(num2)
                s.append(sum)
            elif i == "-":
                num1 = s.pop()
                num2 = s.pop()
                sum = int(num2) - int(num1)
                s.append(sum)
            elif i == "*":
                num1 = s.pop()
                num2 = s.pop()
                sum = int(num1) * int(num2)
                s.append(sum)
            elif i == "/":
                num1 = s.pop()
                num2 = s.pop()
                sum = int(num2) / int(num1)
                s.append(sum)
            else:
                s.append(i)

        return int(s.pop())
