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



def find_triplets_with_zero_sum(arr) -> list[list]:
    """"
        Find all unique triplets in an array that sum to zero. Triplets are distinct,
        meaning the same combination can occur no more than once.
    """
    arr.sort()
    triplets = []

    for i in range(len(arr) - 2):
        if i > 0 and arr[i - 1] == arr[i]:
            continue
        # left, right indexes of arr
        l, r = i + 1, len(arr) - 1
        while l < r:
            s = arr[i] + arr[l] + arr[r]
            if s == 0:
                triplets.append([arr[i], arr[l], arr[r]])
                l =+ 1
                r -= 1    
                while l < r and arr[l] == arr[r]:
                    l += 1
                while l < r and arr[r] == arr[r + 1]:
                    r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return triplets
                    
                
