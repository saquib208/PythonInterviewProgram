
def first_array_sum_taget(l, target):
    length = len(l)
    for i in range(length):
        for j in range(length):
            value=l[i] + l[j]
            if target == value and i != j:
                return l[i], l[j]
    else:
        return "Not Found"

l=[2,5,6,7,9]