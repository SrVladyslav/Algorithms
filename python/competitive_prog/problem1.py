import re 

"""
Task
You are given a string .
Your task is to find the indices of the start and end of string  in .

Input Format

The first line contains the string .
The second line contains the string .

Constraints



Output Format

Print the tuple in this format: (start _index, end _index).
If no match is found, print (-1, -1).

Sample Input

aaadaa
aa
Sample Output

(0, 1)  
(1, 2)
(4, 5)
"""
def getSol(a, b):
    res = set()

    for i in range(len(b)):
        m = re.search(a, b[i:])
        if m:
            res.add((m.start()+i, m.end()+i-1))
    
    if len(res) > 0:
        print(f'Res: {res}')
    else:
        print(f'Res: {(-1, -1)}')

getSol('aa','aaadaa')
getSol('ac','aaadaa')