
def odd_even_partition(A):

    low=0
    high=len(A)
    i=-1
    for j in range(low,high):
        if A[j]%2==0:
            i+=1
            A[i],A[j]=A[j],A[i]
    return A

# A=[4,6,2,3,1,9,5]
# print(odd_even_partition(A))

def positive_negative_segregation(A):

    low=0
    high=len(A)
    i=-1
    for j in range(low,high):
        if A[j]<0:
            i+=1
            A[i],A[j]=A[j],A[i]
    return A

#
# A=[-1,-7,9,-3,2,6]
# print(positive_negative_segregation(A))


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