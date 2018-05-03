def fractional_knapsack(w, p, cap, fp = 0):
    """
        w is list of weights of elements. 
        p is list of profits of elements. 
        cap is max capacity of knapsack.
        fp is final profit.
        
        Initial Call : fk(w, p, cap)
        Output : prints final maximum possible profit.
    """
    if w:  
        if w[0] <= cap :
            fractional_knapsack(w[1:], p[1:], cap-w[0], fp+p[0])
        else :
            fraction = (w[0]-cap)/w[0]
            print(fp+fraction*p[0])
            return None
    else :
        print(fp)
        return None
        
w = list(map(int, input("Enter weight list : ").split()))
p = list(map(int, input("Enter profit list : ").split()))
cap = int(input("Enter the maximum capacity of knapsack : "))

"Sorting profits and weights wrt profit/weight"
p, w = zip(*sorted(zip(p, w), key = lambda x : x[0]/x[1]))

print("final profits : ", end = "")
fractional_knapsack(w, p, cap)

"""
OUTPUT:
Enter weight list : 3 5 2 6 8
Enter profit list : 100 230 420 130 700
Enter the maximum capacity of knapsack : 12
final profits : 322.0
"""
