a = [1,4,6,9,30,479,2749,283947]

N = 4

def find(a, N):
    ini = 0
    fin = len(a)

    for _ in a:
        if ini >= fin: return

        m = (ini + fin) // 2
        if a[m] == N:
            print("Found: ", m)
            return 
        elif N < a[m]:
            fin = m -1
        else:
            ini = m + 1
    print("Not found")
    return False

find(a,N)