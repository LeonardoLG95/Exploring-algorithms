import math

A = [9, 0, 59, 86, 69, 1, 4, 5, 97, 33, 36, 96, 84, 75, 42, 2, 3, 4, 5, 6, 7, 2, 4, 5, 7, 1, 2, 3, 6]
print(f'Unordered list {A}, length {len(A)}')


def merge_sort(A, p: int, r: int):
    if p < r:
        q = int((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


def merge(A: list, p: int, q: int, r: int):
    n1 = q - p + 1
    n2 = r - q

    L = [n for n in range(1, n1 + 1)]
    R = [n for n in range(1, n2 + 1)]

    for i in range(n1):
        L[i] = A[p + i - 1]
    for j in range(n2):
        R[j] = A[q + j]

    L.append(math.inf)
    R.append(math.inf)

    i = 0
    j = 0
    for k, _ in enumerate(range(r)):
        if k < p - 1:
            continue

        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
            continue

        A[k] = R[j]
        j += 1


merge_sort(A, 1, len(A))

print(f'Ordered list {A}, length {len(A)}')
