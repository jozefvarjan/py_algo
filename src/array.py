def find_equilibrium_index(arr):
    """"
        The Equilibrium index in an array is a position where the sum of elements
        on the left is equal to the sum of elements on the right. 
        Aim is to find balance point in data by identifying an index.
    """
    total_sum = sum(arr)
    left_sum = 0
    for i, num in enumerate(arr):
        right_sum = total_sum - left_sum - num
        if left_sum == right_sum:
            return i
        left_sum += num
    return -1 # no equilibrium index found