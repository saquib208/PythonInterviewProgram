

def bubble_sort(a):
    n=len(a)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

    return a
#a=[9,8,2,1,4,7,3]
#print(bubble_sort(a))


def selection_sort(a):
    n=len(a)
    for i in range(0,n):
        minIndex=i
        for j in range(i+1,n):
            if a[minIndex]>a[j]:
                minIndex=j
        a[i],a[minIndex]=a[minIndex],a[i]

    return a

# a=[7,5,8,1,2]
# print(selection_sort(a))

def insertion_sort(a):
    for i in range(1,len(a)):
        pivot=i
        value=a[i]

        while(pivot>0 and a[pivot-1]>value):
            a[pivot]=a[pivot-1]
            pivot=pivot-1
        a[pivot]=value

    return a


a=[7,5,8,1,2]
print(insertion_sort(a))