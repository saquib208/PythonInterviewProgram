
def reverse(n):
    rev = 0

    while(n>0):
        rev=rev*10+n%10
        n=n//10

    return rev

#print(reverse(123))

def rotate(l,r):
    y=l[r:]+l[:r]
    return y

l=[3,4,2,8,7]
index=1
print(f"Rotate number -->{rotate(l,index)}")


def second_highest(l):
    highest=l[0]
    second_max=l[1]
    for i in range(len(l)):
        if l[i]>highest:
            second_max = highest
            highest=l[i]
        elif l[i]>second_max:
            second_max=l[i]
    return second_max,highest

x=[3,8,12,9,-1,15,10]
print(x)
print(f'Second Max-->>{second_highest(x)}')

def third_highest(l):
    highest=l[0]
    second_max=l[1]
    third_max=l[2]
    for i in range(len(l)):
        if l[i]>highest:
            second_max = highest
            highest=l[i]
        elif l[i]>second_max:
            second_max=l[i]
            third_max = second_max
        elif l[i]>third_max:
            third_max=l[i]

    return third_max,second_max,highest

x=[-3,-8,-2,-9,-1,-5,-10]
print(x)
print(f'Third Max-->>{third_highest(x)}')


k=[4,3,2,2,1,1,2,2,7,6,6,7]

c=[(i,k.count(i)) for i in k if k.count(i)>1 ]
print(set(c))

str="This is duplicate duplicate word word count"


def count_duplicate(s):
    d = {}
    for i in str.split():
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
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

def find_duplicate_2(l):
    d={}
    for i in l:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return [i for i,j in d.items() if j>1]
#d=["python","java","c","python"]
#print(find_duplicate_2(d))


# d=["python","java","c","python"]
# print(find_duplicate(d))

test_result=[(4,'Ram',25),(1,'Adam',30),(8,'Jhon',45)]
test_result.sort(key=lambda x:x[2])
# print(test_result)

def remove_duplicate_occurence(l,a,n):
    count=0
    for i in range(0,len(l)):
        if a in l[i]:
            count +=1
            if count==n:
                del l[i]
                break
    return l

#
# l=['Hi','Hello','Bye','Hello','Bye','Hello']
# a='Hello'
# n=2
# print(remove_duplicate_occurence(l,a,n))

def common_substring(a,b):
    flag=0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j] and set(a[i]).intersection(set(b[j])):
                flag=1

    if flag:
        print ("Yes")
    else:
        print("No")

def revesrse_char(l):
    low=0
    high=len(l)-1
    while(low<high):
        l[low],l[high]=l[high],l[low]
        low+=1
        high-=1

    return l

#l=['h','e','l','l','o']
#print(revesrse_char(l))

def conut_digit(n):
    c=0
    while(n>0):
        c+=1
        n=n//10

    return c

print(conut_digit(494036))

def revesrse_string(s):
    rev=""

    for i in range(len(s)-1,-1,-1):
        rev=rev+s[i]

    return rev


print(revesrse_string("Hello world"))


