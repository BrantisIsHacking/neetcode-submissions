class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        minv = self.getMin()
        if minv == None or minv > val:
            minv = val
        self.st.append([val, minv])

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        if self.st:
            return(self.st[-1][0])
        else:
            None

    def getMin(self) -> int:
        if self.st:
            return self.st[-1][1]
        else:
            None
