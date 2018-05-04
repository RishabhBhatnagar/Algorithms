"""
Matrix chain multiplication : 
Prints the optimal parenthesis using which, 
    the best combination is returned, 
    which gives the least number of multiplications.
"""

from math import inf
p = list(map(int, input("Enter the dimension matrix : ").split()))
n = len(p)
m = [[0 for i in range(n)] for j in range(n)]
s = [[0 for i in range(n)] for j in range(n)]
for d in range(1, n-1):
    for i in range(1, n-d):
        j = i + d
        m[i][j] = inf
        min = inf
        for k in range(i, j):
            q = m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
            if q < min:
                min = q
                s[i][j] = k
        m[i][j] = min
def parenthesis(A, s, i, j):
    if i<j:
        print("(", end = "")
        X = parenthesis(A, s, i, s[i][j])
        if X : 
            print('A', X, end = "", sep = "")
            print("*", end = "")
        Y = parenthesis(A, s, s[i][j]+1, j)
        if Y : print('A', Y, end = "", sep = "")
        print(")", end = "")
    else:
        return i
parenthesis(p, s, 0, n-1)
print()

"""
Example Output:
Enter the dimension matrix :  5 4 7 2 3
(((A1*(A2*A3))A4))
"""
