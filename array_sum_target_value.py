# 1 st version O(n^2) complexity
def first_array_sum_taget(l, target):
    length = len(l)
    for i in range(length):
        for j in range(length):
            value=l[i] + l[j]
            if target == value and i != j:
                return l[i], l[j]
    else:
        return False

# l=[7,8,9,4,3]
# v=16
# print(first_array_sum_taget(l,v))

def second_array_sum_taget(l, target):
    low=0
    high=len(l)-1
    l.sort()

    while (low < high):
        value=l[low]+l[high]

        if value==target:
            return True
        elif target<value:
            high-=1
        else:
            low+=1
    return False

l=[7,2,5,9,4,3]
v=7
print(second_array_sum_taget(l,v))

def third_array_sum_taget(l,target):
    already_seen=set()
    for i in l:
        difference=target-i
        if difference in already_seen:
            return True
        else:
            already_seen.add(i)
    return False


l=[7,2,5,9,4,3]
v=14
print(third_array_sum_taget(l,v))




