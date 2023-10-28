def reverse_each_word(word):
    w=[]
    words=word.split()
    for i in range(len(words)-1,-1,-1):
        w.append(words[i])
    return " ".join(w)


word = "My first python program"
print(reverse_each_word(word))


def digital_root(n):
    s=0
    while(n>0):
        t=n%10
        s+=t
        n=n//10

        if s > 9:
            s = digital_root(s)

    return s
#n=int(191)
#print(digital_root(n))


def word_count(ss):
    d = {}
    for w in ss.split():
        d[w] = d.get(w, 0) + 1
    return d


ss="""I figured it out
I figured it out from black and white
Seconds and hours
Maybe they had to take some time"""
#print(word_count(ss))

import  math
def isPrime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

#print(isPrime(4))

def fib(n):
    f=[]
    a,b=0,1
    if n==0:
        return 0
    elif n==1:
        return 0,1
    else:
        f.append(a)
        f.append(b)
        for i in range(2,n):
            c=a+b
            f.append(c)
            a=b
            b=c
        return f


print(fib(3))

def fib_recursive(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib_recursive(n-1)+fib_recursive(n-2)


print(fib_recursive(5))

def fib(n):
    p, q = 0, 1
    while(p < n):
        yield p
        p, q = q, p + q

x = fib(10)    # create generator object


#Find the sublist in the list
def sub_list(a,b):
    x = b in [a[i:len(b) + i] for i in range(len(a))]
    return x

a = [2,4,3,5,7]
b = [5,7]
print("Sub list-->>",sub_list(a,b))


def get_str(s):
    if len(s)<2:
        return "Empty string"
    elif len(s)==2:
        return s*2
    else:
        return s[:2]+s[-2:]

#s="saquib"
s="a"

#print(get_str(s))

def isPrime(n):

    for i in range(2,n):
        if n%i==0:
            return False

    return True

resu=list(map(isPrime,range(2,20)))

# print(isPrime(3))
# for i in range(2,10):
#     if isPrime(i):
#         print ('Is prime {}'.format(i))
#     else:
#         print('Not prime {}'.format(i))

def fact(n):
    fact=1
    if n<0:
        print("Factorial does not exists")
    elif n==0 or n==1:
        print("The factorial of 1 is 1")
    else:
        for i in range(1,n+1):
            fact=fact*i
        print("The factorial of {} is {}".format(n,fact))

fact(0)

def fact2(n):
    return 1 if(n==1 or n==0) else n*fact2(n-1)

print(fact2(4))

fib1 = lambda n: n if n < 2 else fib1(n-1) + fib1(n-2)

# print(list(map(fib1,range(4))))

def anagram(s1,s2):
    if sorted(s1)==sorted(s2) and len(s1)==len(s2):
        return True
    else:
        return False



a='abc'
b='dca'
print(anagram(a,b))

def reverse_word(x):
    l=x.split(" ")
    return ' '.join(l[-1::-1])
print(reverse_word("Hello WOrld"))


def fibonaci(n):
    a,b=0,1
    print (a,b,end=" ")
    while n-2:
        c=a+b
        a=b
        b=c
        print(c,end=' ')
        n=n-1

    return " "

print(fibonaci(10))

def armstrong(n):
    s=0
    t=n
    while t>0:
        c=t%10
        s+=c**3
        t=t//10
    if n==s:
        return "Armstrong Number"
    else:
        return "Not Armstrong Number"

print(armstrong(153))

print(armstrong(151))


def is_Sublist(l, s):
    sub_set = False

    if s == l:
        sub_set = True
    elif len(s) > len(l):
        sub_set = False

    else:
        for i in range(len(l)):
            if l[i] == s[0]:
                n = 1
                while (n < len(s)) and (l[i + n] == s[n]):
                    n += 1

                if n == len(s):
                    sub_set = True

    return sub_set

a = [2,4,3,5,7]
b = [4,3,5,7]
c = [2,5,7]
s1='abcdeffg'
s2='de'
print(is_Sublist(a, b))
print(is_Sublist(s1, s2))

def single_number(x):
    result=0
    for i in range(len(x)):
        result ^=x[i]
    return result
x=[1,2,2,1,4]

print(single_number(x))

# Two pointer lef and right initialise to zero if right see zero
# just increment it else swap the number,increment left and right counter

def shift_zero_end(b):
    n=len(b)
    if (n==0 and n==1):
       return []
    left,right=0,0
    while (right<n):
        if b[right]==0:
            right+=1
        else:
            b[left],b[right]=b[right],b[left]
            left+=1
            right+=1
    return b

#b=[1,0,3,0,4,0,0,8,5]


b=[0,0,3,0,4,0,0,8,5]
print(shift_zero_end(b))


def pallindrom(s1,s2):
    for i1 in range(len(s1)):
        i2=len(s2)-i1-1
        if s1[i1]!=s2[i2]:
            return False

    return True

def larger_than_string(a,b):
    if (len(a)>len(b)):
        return True
    elif (len(a)<len(b)):
        return False
    for i in range(len(a)):
        if a[i]==b[i]:
            continue
        elif a[i]>b[i]:
            return True
        else:
            return False

    return False

print(larger_than_string("113","113"))

s1='lmn'
s2='567'

print(s1.join(s2))