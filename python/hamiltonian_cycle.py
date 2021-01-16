from graph import Graph
from random import sample 

class HamiltonianCycle:
    def __init__(self, E):
        self.E = E
        self.G = Graph(E= self.E)
        
    def get_cycle(self):
        def backtracking(path):
            if len(path) == len(self.G.V):
                if (path[-1], path[0]) in G.E:           # The end is the starting point of a Graph
                    return path + [path[0]]
            else:
                for v in G.succs(path[-1]):              # Next vertices
                    if v not in path:                    # Unexplored vertex 
                        found = backtracking(path + [v]) # Let's explore it
                        if found:
                            return found
            return None
        
        [random, vertex] = sample(G.V, 1) # Pick a random vertex to start with
        return backtracking([random, vertex])
    
if __name__ == '__main__':    
    hc = HamiltonianCycle(
        E = [(0,1), (0,2), (0,3), (1,3), (1,4), (2,3), (2,5), (3,4), (3,5), (3,6), (4,7), (5,6), (5,8), (6,7), (6,8), (6,9) (7,9), (8,9)]
    )