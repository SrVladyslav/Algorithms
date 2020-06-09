# ======================================================================
# Simple program to solve proove the solution for my Shchool exercices
# ======================================================================
# 
# Input ==========================================
# agent: ['opt1 > opt2 > ... > optN', nº of agents]
proove = {
	1: ['a>b>c',5],
	2: ['b>c>a',4],
	3: ['c>a>b',3],#c>a>b

	
	# Paradoja Condorcet: si aparece cada letra una vez en cada columna, es condorcet, 
	# con que aparezca dos veces en la misma columna, ya no es condorcet 
}

# 0: winner, 1: looser
OPCION = 1

# ================================================
# 
# 
# 
# 
# 
# 
# 
# Returns the array of the best weights
# t = 0: winner, 1: looser
# sep is always '>'
def condorcet(agents = proove):
	solution = {}

	for agent in agents.keys():
		options = agents[agent][0].strip().split('>')
		
		lo = len(options)
		for opt in range(lo):
			solution[options[opt]] = agents[agent][1] * (lo - opt - 1) if solution.get(options[opt]) == None else \
			  solution[options[opt]] + agents[agent][1] * (lo - opt- 1)
	max_w = dict(zip(solution.values(), solution.keys()))

	k = max_w.keys()
	print("OPTIONS: ", [(max_w[j], j) for j in k])
	# Maximum
	m = max(k)
	if len([i for i in k if k == m]) > 1:
		print('> There are more maximums')
	else:
		print("> The winner option is:",max_w[m])
	
	# Minimum
	m = min(k)
	if len([i for i in k if k == m]) > 1:
		print('There are more minimums')
	else:
		print("> The looser option is:",max_w[m])


print("="*20,"Condorcet","="*20)
condorcet()
print("="*51)