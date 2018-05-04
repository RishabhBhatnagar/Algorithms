#MergeSort

a = list(map(int, input("Enter list to be sorted : ").split()))

def merge(a, b):
    """A recursive merge function."""
    if not a : return b
    if not b : return a
    if a[0] < b[0] : return [a[0]]+merge(a[1:], b)
    else : return [b[0]]+merge(a, b[1:])

def sorted(a):
    if len(a) <= 1 : return a
    else:
        mid = len(a) // 2
        left = sorted(a[:mid])
        right = sorted(a[mid:])
        return merge(left, right)
print(sorted(a))
