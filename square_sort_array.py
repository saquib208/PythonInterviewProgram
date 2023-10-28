f= [-3,-2,-1,0,5,6]

def square_sorted_array(arr):
    result = [0]*len(arr)
    left = 0
    right = len(arr) - 1
    current = len(arr) - 1
    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            result[current] = arr[left] ** 2
            left += 1
        else:
            result[current] = arr[right] ** 2
            right -= 1
        current -= 1
    return result

print(square_sorted_array(f))

