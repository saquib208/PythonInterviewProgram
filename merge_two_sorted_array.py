
def left_right_merge(l,m):
    n=len(l)+len(m)
    i=0
    j=0
    k=0
    A=[0]*n

    while (i<len(l) and j<len(m)):
        if l[i]<m[j]:
            A[k]=l[i]
            i+=1
            k+=1
        else:
            A[k]=m[j]
            j+=1
            k+=1

    while (i<len(l)):
        A[k]=l[i]
        i+=1
        k+=1

    while (j<len(m)):
        A[k]=m[j]
        j+=1
        k+=1


    return A

l=[2,4,6]
m=[3,5,7]
#print(left_right_merge(l,m))


def merge_sort_2(a,b):
    c=[]
    while a and b:
        if a[0] < b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))

    # either a or b could still be non-empty
    print (c + a + b)

a = [3, 4, 6, 10, 11, 18]
b = [1, 5, 7, 12, 13, 19, 21]
print(merge_sort_2(a,b))