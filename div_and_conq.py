import math


def find_max_crossing_subarray(A, low, mid, high):
    left_sum = 0
    _sum = 0
    max_left = 0
    
    #Soma da esquerda
    for i in range(mid, low - 1, -1):
        _sum = _sum + A[i]
        if _sum > left_sum:
            left_sum = _sum
            max_left = i

    right_sum = 0
    _sum = 0
    max_right = 0
    
    #Soma da direita
    for i in range(mid + 1, high + 1):
        _sum = _sum + A[i]
        if _sum > right_sum:
            right_sum = _sum
            max_right = i
    
    return max_left, max_right, (left_sum + right_sum)


def find_max_subarray(A, low, high):
    # Caso base
    if high == low:
        return low, high, A[low]
    
    # Calcula o meio do array
    mid = int((low + high) / 2)
    
    # Vá para o vetor da esquerda
    # então vá para o da direita
    # somar os elementos dos dois vetores
    left_low, left_high, left_sum = find_max_subarray(A, low, mid)
    right_low, right_high, right_sum = find_max_subarray(A, mid + 1, high)
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


if __name__ == "main":
    A = [0, 18, 20, -7, 12, -5, -22]
    print(find_max_subarray(A, 0, len(A) - 1))
