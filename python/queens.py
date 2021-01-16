class QueenSolver: 
    def __init__(self, n):
        self.n = n
    
    def is_complete(self, s):
        return len(s) == self.n
    
    def is_promissing(self, s, row):
        return all( row != s[i] and len(s)-i != abs(row - s[i]) for i in range(len(s)))
    
    def backtracking(self, s):
        if self.is_complete(s):
            return s
        for row in range(self.n):
            if self.is_promissing(s, row):
                found = self.backtracking(s + [row])
                if found != None:
                    return found
        return None
    
    def solve(self):
        return self.backtracking([])
    
    
if __name__ == '__main__':
    solver = QueenSolver(5)
    print(f'The solution is: {solver.solve()}')