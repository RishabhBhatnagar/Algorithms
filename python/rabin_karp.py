"""
Rabin Karp is a string matching algorithm used to find pattern in a text.
Input : A string and a pattern to find in input string.
Output : shifts at which pattern is found.

Example :
First String : mathematics is abbreivated as maths.
Second String : at
[1, 6, 22, 31] 
"""
def rabin_karp(T, P, d, q):
    n = len(T)
    m = len(P)
    h = pow(d, m-1)%q
    p, t = 0, 0
    result = []
    for i in range(m):
        t = (d*t+ord(T[i]))%q
        p = (d*p+ord(P[i]))%q
    for s in range(n-m+1):
        if t == p:
            match = True
            for i in range(m):
                if T[s+i] != P[i]:
                    match = False
                    break
            if match : result = result+[s]
        if s<n-m : 
            t = (t - h*ord(T[s]))%q
            t = (t*d+ord(T[s+m]))%q
            t = (t+q)%q
    return result
print(rabin_karp(input("First String : "), input("Second String : "), 257, 11))
