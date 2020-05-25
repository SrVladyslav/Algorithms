# Kosaraju's algorithm
# ========================
# Given one direct graph, the algorithm finds his SCC( strongly connected components )
V = ['A','B','C','D','E','F','G','H','I']

T = {
	'A':['B'],
	'B':['C','D','F'],
	'C':['A'],
	'D':['E'],
	'E':['F', 'G'],
	'F':['D', 'H'],
	'G':['F'],
	'H':['I'],
	'I':['H'],
}

'''
================== KOSARAJU's ALGORYTHM ================== 
1) Create an empty stack 'S', do DFS on a graph, on the road, insert the vertices on top of this stack.

2) Obtain the Transpose Graph, just reverse the graph

3) One by one pop each vertex from S while S is not empty. 

4) Let popped vertex be 'v', so it will be the source, do DFS on it. The DFS starting from 'v' 
will denote the strongly connected components (SCC) of 'v', one by one popped from stack.
'''

class Graph:
	def __init__(self, vertices = {}, graph= {}):
		self.vertices = vertices
		self.graph = graph
		self.S = [] 
		self.SCC = []

		visited = {}
		for v in vertices:
			visited[v] = False 
		self.visited = visited

	def doDFS(self, graph = None):
		if not graph:
			graph = self.graph

		for u in self.vertices:
			if self.visited[u] == False:
				self.visited[u] = True # Mark u as visited
				for v in graph[u]:
					self.doDFS()
				self.S.insert(0, u)

	def getSCC(self, vertix, graph = {}):
		if self.visited[vertix] == True:
			self.visited[vertix] = False
			ve = [vertix]
			if graph[vertix] is not None:
				for v in graph[vertix]:
					a = self.getSCC(v, graph)
					if a is not None:
						ve += a
			return ve
	# Transpose the given Graph
	def reverseGraph(self, graph = {}):
		rGraph = {}
		for v in graph.keys():
			for dest in graph[v]:
				rGraph[dest] = [v] if rGraph.get(dest) == None else rGraph[dest] + [v]
		return rGraph

	# Constructs new graph from SCC
	def newGraph(self):
		newGraph = {}
			
		for ind in range(len(self.SCC) - 1):
			newGraph[self.SCC[ind][0]] = [self.SCC[ind + 1][0]]
		newGraph[self.SCC[len(self.SCC) - 1][0]] = []
		print(">> Simplified Graph by SCC: ", newGraph)


	# Returns the Strongly Connected Components from a Graph
	def doKosaraju(self):
		# 1) Inserting in S the components
		self.doDFS()
		# 2) Obtaining the reverse graph
		rGraph = self.reverseGraph(self.graph)

		# 3) Popping and searching for SCC
		print("-"*30, "STRONGLY CONNECTED COMPONENTS", "-"*30)
		while len(self.S) > 0:
			v = self.S.pop(0)
			scc = self.getSCC(v, rGraph)
			if scc is not None:
				self.SCC.append(scc)
				print("		> Component",scc[0], " 	>> 	",scc)
		print("-"*91, "\n")

		newGraph = self.newGraph()
		return self.SCC
		


if __name__ == '__main__':
	g = Graph(V,T)
	print('='*150)
	print(">> Directed graph:",g.graph, "\n")
	g.doKosaraju()
	print('='*150)