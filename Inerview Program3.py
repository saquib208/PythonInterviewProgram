# Program to check if a Python list contains elements of another list

def list_contains(List1, List2):
    set1 = set(List1)
    set2 = set(List2)
    if set1.intersection(set2):
        return True
    else:
        return False


# Test Case 1
List1 = ['a', 'e', 'i', 'o', 'u']
List2 = ['x', 'y', 'z', 'l', 'm']
#print("Test Case#1 ", list_contains(List1, List2))

# Test Case 2
List1 = ['a', 'e', 'i', 'o', 'u']
List2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
#print("Test Case#2 ", list_contains(List1, List2))


# Program to check if a Python list contains elements of another list

def list_contains(List1, List2):
    check = False

    # Iterate in the 1st list
    for m in List1:

        # Iterate in the 2nd list
        for n in List2:

            # if there is a match
            if m == n:
                check = True
                return check

    return check


# Test Case 1
List1 = ['a', 'e', 'i', 'o', 'u']
List2 = ['x', 'y', 'z', 'l', 'm']
#print("Test Case#1 ", list_contains(List1, List2))

# Test Case 2
List1 = ['a', 'e', 'i', 'o', 'u']
List2 = ['a', 'b', 'c', 'd', 'e']
#print("Test Case#2 ", list_contains(List1, List2))

#Given two array of string,determine whether correspondins element contains a common substring.

x=['ab','cd','wc']
y=["af","ab","wf"]
Result=["Yes","No","Yes"]

def common_substring(x,y):
    a=[]
    for i in range(len(x)):
            if set(x[i]).intersection(set(y[i])):
                #print("True")
                a.append('True')
            else:
                #print("False")
                a.append('False')
    return a


print(f'commom substring-->>{common_substring(x,y)}')


def pallindrome_string(x):
    left=0
    right=len(x)-1
    while (left<=right):
        if x[left] != x[right]:
            return False
        left += 1
        right -= 1
    return True

print(pallindrome_string('redrum murder'))
#
# print(pallindrome_string('madam12'))

#email search
# import re
# e=re.search(r'[0-9a-zA-Z.]+@[a-zA-Z]+\.(com|co\.in)$','abc@gmail.com')
# e.group()

myList={('jerry', 33, 'R&D'), ('jake', 44, 'IT'), ('john', 28, 'Accounts'), ('tom', 32, 'HR')}

def nav_myList(p):
    for i,j,z in p:
        if j>32:
            print (i)

y= [('Ram', 33, 'R&D'), ('Nina', 44, 'IT'), ('Gupta', 28, 'Accounts'), ('tom', 32, 'HR')]

def sorting(x):
    x.sort(key=lambda x:x[1])
    return x

print(sorting(y))


def Sort_Tuple(tup):
    # getting length of list of tuples
    lst = len(tup)
    for i in range(0, lst):
        for j in range(0, lst - i - 1):
            if (tup[j][1] > tup[j + 1][1]):
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    return tup


# Driver Code
tup = [('for', 24), ('is', 10), ('Geeks', 28),
       ('Geeksforgeeks', 5), ('portal', 20), ('a', 15)]

print(Sort_Tuple(tup))
import string
print(nav_myList(myList))


def substring_count(s,sub):
    count=0
    for i in range(len(s)):
        if s[i:i+len(sub)] == sub:
            count+=1
    return count
#{substring_count("abcdabctradbc",'bc')}
print(f"substring_count-->>{substring_count('abcdabctradbc','bc')}")

def group_anagram(anagram):
    result={}
    for i in anagram:
        x="". join(sorted(i))
        print(x)
        if x in result:
            result[x].append(i)
        else:
            result[x]=[i]
    print(result)
    return list(result.values())

anagram=["eat", "tea", "tan", "ate", "nat", "bat"]
#anagram=['test','rest','sett']
#print(group_anagram(anagram))
print(f"Anagram-->{group_anagram(anagram)}")

