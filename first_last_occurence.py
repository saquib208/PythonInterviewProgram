
def first_left_occurence(l,n):

    low=0
    h=len(l)-1
    result=-1

    while(low<=h):
        mid=(low+h)//2


        if l[mid]==n:
            result=mid
            h=mid-1
        elif l[mid]<n:
            low=mid+1
        else:
            h=mid-1

    return result

# l=[1,2,3,3]
# print(first_left_occurence(l,3))


def last_right_occurence(l,n):

    low=0
    h=len(l)-1
    result=-1

    while(low<=h):
        mid=(low+h)//2


        if l[mid]==n:
            result=mid
            low=mid+1
        elif l[mid]<n:
            low=mid+1
        else:
            h=mid-1

    return result


l=[1,2,3,3,4]

print(last_right_occurence(l,3))