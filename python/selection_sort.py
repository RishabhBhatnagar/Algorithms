#selection sort
a = list(map(int, input("Enter list to be sorted : ").split()))
def sorted(a):
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[min_idx], a[i] = a[i], a[min_idx]
    return a
print("sorted list : ", sorted(a))
