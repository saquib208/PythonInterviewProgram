def binary_search(item_list, item):
    first = 0
    last = len(item_list) - 1
    found = False
    while (first <= last):
        mid = (first + last) // 2
        if item_list[mid] == item:
            return True
        elif item < item_list[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


print(binary_search([1, 2, 3, 5, 8], 1))
print(binary_search([1, 2, 3, 5, 8], 5))


a = [3,5,7,8,9,1]
c = 7
def linear_search(a,c):
    for i in a:
        if i == c:
            return a.index(i)
    else:
        return -1



print(linear_search(a,c))