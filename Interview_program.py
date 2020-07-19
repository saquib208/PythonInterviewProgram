
def reverse(n):
    rev = 0

    while(n>0):
        rev=rev*10+n%10
        n=n//10

    return rev

#print(reverse(123))

def rotate(l,r):
    y=l[r:]+l[:r]
    print(y)
# l=[3,4,2,8,7]
# index=2
# print(rotate(l,index))


def second_highest(l):
    highest=l[0]
    second_max=l[1]
    for i in range(len(l)):
        if l[i]>highest:
            second_max = highest
            highest=l[i]
        elif l[i]>second_max:
            second_max=l[i]

    return second_max

# x=[3,8,12,9]
# print(second_highest(x))


k=[4,3,2,2,1,1,2,2,7,6,6,7]

c=[(i,k.count(i)) for i in k if k.count(i)>1 ]
print(set(c))

str="Thsi is duplicate duplicate word word count"
def count_duplicate(s):
    d={}
    for i in str.split():
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d

#print(count_duplicate(str))

#Print duplicate element in the list

def find_duplicate(d):
    for i in range(len(d)):
        for j in range(i+1,len(d)):
            if (d[i]==d[j]):
                print(d[i])

# d=["python","java","c","python"]
# print(find_duplicate(d))

test_result=[(4,'Ram',25),(1,'Adam',30),(8,'Jon',45)]
test_result.sort(key=lambda x:x[2])
# print(test_result)

