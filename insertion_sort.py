A = [2, 4, 6, 1, 3, 5, 7]
print(f'Unordered list: \n {A}')

for j, _ in enumerate(range(len(A))):
    key = A[j]
    i = j - 1

    while i >= 0 and A[i] > key:
        A[i + 1] = A[i]
        i = i - 1

    A[i + 1] = key

print(f'Ordered list: \n {A}')
