a = list(map(int, input("Enter a list : ").split()))
#Insertion Sort.
def sort(a):
    i = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j>=0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a
print("sorted list :", sort(a))
