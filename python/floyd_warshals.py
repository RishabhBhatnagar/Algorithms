"""
All pair shortest path using floyd warshalls algorithm.
"""
def apsp(w):
    n = len(w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                w[i][j] = min(w[i][k], w[k][j])
    return w


n = int(input("Enter number of vertices : "))
w = []
print("Enter the weight matrix : ")
for i in range(n):
    w.append(list(map(float, input().split())))
print("Final output : ")
for i in w:
    for j in i:
        print(j, end = " ")
    print()

"""
0 1 2
2 0 inf
4 inf 0              
Final output : 
0.0 1.0 2.0 
2.0 0.0 inf 
4.0 inf 0.0
"""
