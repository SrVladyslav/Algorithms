"""
Problem: Longest Common Subsequence

Given two sequences of characters, find the length of the longest common subsequence (LCS) between them. 
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. 

For example, for the sequences "ABCBDAB" and "BDCAB", the LCS is "BCAB", and its length is 4.
"""

def longest_subsequence(t1,t2):
    a, b = len(t1), len(t2)

    dp = [[0] * (b+1) for _ in range(a+1)]

    for i in range(1, a+1):
        for j in range(1, b+1):
            if t1[i-1] == t2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[a][b]

print(longest_subsequence('ABCBDAB', 'BDCAB'))





# Python program to find length 
# of the shortest supersequence 

# Function to find length of the 
# shortest supersequence of X and Y. 


def shortestSuperSequence(X, Y): 
	m = len(X) 
	n = len(Y) 
	l = lcs(X, Y, m, n) 

	# Result is sum of input string 
	# lengths - length of lcs 
	return (m + n - l) 

# Returns length of LCS for 
# X[0..m - 1], Y[0..n - 1] 


def lcs(X, Y, m, n): 
	L = [[0] * (n + 2) for i in
		range(m + 2)] 

	# Following steps build L[m + 1][n + 1] 
	# in bottom up fashion. Note that L[i][j] 
	# contains length of LCS of X[0..i - 1] 
	# and Y[0..j - 1] 
	for i in range(m + 1): 

		for j in range(n + 1): 

			if (i == 0 or j == 0): 
				L[i][j] = 0

			elif (X[i - 1] == Y[j - 1]): 
				L[i][j] = L[i - 1][j - 1] + 1

			else: 
				L[i][j] = max(L[i - 1][j], 
							L[i][j - 1]) 

	# L[m][n] contains length of 
	# LCS for X[0..n - 1] and Y[0..m - 1] 
	print(L)
	return L[m][n] 


# Driver code 
X = "AGGTAB"
Y = "GXTXAYB"

print("Length of the shortest supersequence is %d"
	% shortestSuperSequence(X, Y)) 

# This code is contributed by Ansu Kumari 
