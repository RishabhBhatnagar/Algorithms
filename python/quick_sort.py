#QuickSort algorithm.

a = list(map(int, input("Enter list to be sorted : ").split()))

"""
In partition algorithm, last element is choosed as pivot element.
"""
def partition(a, p, r):
    pivot = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i + 1

def sorted(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        sorted(a, low, pivot-1)
        sorted(a, pivot+1, high)
        return a

print(sorted(a, 0, len(a)-1))
