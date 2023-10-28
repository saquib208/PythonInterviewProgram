
def odd_even_partition(A):
    low=0
    high=len(A)
    i = 0
    for j in range(low,high):
        if A[j]%2==0:
            A[i],A[j]=A[j],A[i]
            i =+1
    return A

A=[4,1,2,3,19,9,5]
print(odd_even_partition(A))

def positive_negative_segregation(A):

    low=0
    high=len(A)
    i=0
    for j in range(low,high):
        if A[j]<0:
            A[i],A[j]=A[j],A[i]
            i +=1
    return A


A=[-1,-7,9,-3,2,6]
print(positive_negative_segregation(A))


def zero_one_partition(A):
    low=0
    high=len(A)
    i=-1
    for j in range(low,high):
        if A[j]==0:
            i+=1
            A[i],A[j]=A[j],A[i]
    return A

A=[0,1,0,1,1,1,0]
print(zero_one_partition(A))

def quick_sort_partition(A,low,high):

    pivot=A[high]
    partition=low
    for i in range(high):
        if A[i]<=pivot:
            A[i],A[partition]=A[partition],A[i]
            partition+=1

    A[partition],A[high]
    return partition

def quick_sort_logic(A,low,high):
    if (low<high):
        p=quick_sort_partition(A,low,high)
        print(p)
        quick_sort_logic(A,low,p-1)
        quick_sort_logic(A, p+1,high)










A=[10,6,2,11,1]
low=0
high=len(A)-1
quick_sort_logic(A,0,high)
print(A)


print(quick_sort_partition(A,low,high))