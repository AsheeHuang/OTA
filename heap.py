def PARENT(i):
    return (int(i / 2))


def LEFT(i):
    return 2 * i


def RIGHT(i):
    return 2 * i + 1

#max heap
def HEAPFY(A, i):
    largest = -1
    l = LEFT(i)
    r = RIGHT(i)
    if l < len(A):
        if A[l][1] < A[i][1]:
            largest = l
        else:
            largest = i
    if r < len(A):
        if A[r][1] < A[largest][1]:
            largest = r
    if largest != i & largest != -1:
        tmp = A[i]
        A[i] = A[largest]
        A[largest] = tmp
        HEAPFY(A, largest)


def BUILD_HEAP(A):
    for i in range(int(len(A) / 2), -1, -1):
        HEAPFY(A, i)
def push(A,val) :
    A.append(val)
    i = len(A)

    while i != 0 and val > A[PARENT(i)] :
        A[i] = A[PARENT(i)]
        i /= 2
    A[i] = val
