from math import floor, inf

A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]


def find_maximum_subarray(A: list, low: int, high: int):
    if high == low:
        return low, high, A[low]
    else:
        mid = floor((low + high) / 2)
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, right_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def find_max_crossing_subarray(A: list, low: int, mid: int, high: int):
    left_sum = - inf
    summation = 0
    max_left = None
    for i in range(mid, low, -1):
        summation = summation + A[i]
        if summation > left_sum:
            left_sum = summation
            max_left = i

    right_sum = - inf
    summation = 0
    max_right = None
    for j in range(mid + 1, high):
        summation = summation + A[j]
        if summation > right_sum:
            right_sum = summation
            max_right = j

    return max_left, max_right, left_sum + right_sum


max_left, max_right, result = find_maximum_subarray(A, 0, len(A) - 1)
print(f"A = {A} \n\n"
      f"The maximum subarray B ⊆ A is from {max_left} to {max_right}, both inclusive.\n"
      f"B = {A[max_left:max_right + 1]} = {result}")
