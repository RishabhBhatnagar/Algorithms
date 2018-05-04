"""
Single source shortest path using Dijkstras algorithm.
"""

from math import inf

def mat_to_neigh(mat):
    """converts adjaceny matrix to dictionay of neighbours
       two nodes are connected if they have weight 0.
       Example:
       Consider following adjacency matrix : 
       0 0 1
       1 0 0 
       1 1 0
       Output will be : 
       {'A':['C'], 'B':['A'], 'C':['A', 'B']
    """ 
    neighbours = {}
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] != 0:
                try : neighbours[chr(i+65)].append(chr(j+65))
                except : neighbours[chr(i+65)] = [chr(j+65)]
    return neighbours

def initialize(n, source, neighbours):
    '''
    initializING d and pi dictionaries to inf and None respectively.
    '''
    d = {}
    pi = {}
    for i in range(n):
        d[chr(65+i)] = inf
        pi[chr(65+i)] = None
    d[source] = 0
    return d, pi
    
def extract_min(Q, d):
    '''Returns the node with minimum d value in the Queue'''
    return min(Q, key = lambda x : d[x])
    
def relax(u, v, d, pi, mat):
    if d[v]>d[u]+mat[ord(u)-65][ord(v)-65]:
        d[v] = d[u]+mat[ord(u)-65][ord(v)-65]
        pi[v] = u

mat = []
n = int(input("number of vertices : "))
source = "A"
print("Enter the adj matrix : ")
for i in range(n):
    mat.append(list(map(float, input().split())))
    
neighbours = mat_to_neigh(mat)

d, pi = initialize(n, source, neighbours)
S = {}
Q = set([chr(65+i) for i in range(n)])

while Q:
    u = extract_min(Q, d)
    Q = list(Q)
    Q.remove(u)
    Q = set(Q)
    S = set(list(S)+[u])
    for v in neighbours[u]:
        relax(u, v, d, pi, mat)
print("Final distances : ")
for i in d : 
    print(source, 'to', i, ':', d[i])
"""
Example : 
Input : 
9
0 4 0 0 0 0 0 8 0
4 0 8 0 0 0 0 11 0
0 8 0 7 0 4 0 0 2
0 0 7 0 9 14 0 0 0
0 0 0 9 0 10 0 0 0
0 0 4 14 10 0 2 0 0
0 0 0 0 0 2 0 1 6
8 11 0 0 0 0 1 0 7
0 0 2 0 0 0 6 7 0
Output:
Enter the adj matrix : 
Final distances : 
A to A : 0
A to B : 4.0
A to C : 12.0
A to D : 19.0
A to E : 21.0
A to F : 11.0
A to G : 9.0
A to H : 8.0
A to I : 14.0
"""
