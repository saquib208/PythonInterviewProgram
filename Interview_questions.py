cities = {'San Francisco': 'US', 'London':'UK',
        'Manchester':'UK', 'Paris':'France',
        'Los Angeles':'US', 'Seoul':'Korea'}


from collections import defaultdict


d = defaultdict(list)
print(d)

for k,v in cities.items():
    d[v].append(k)

print(d)


def isPrime(n):
   if n == 1:
      return False
   for t in range(2,n):
      if n % t == 0:
         return False
   return True

# >>> import os
# >>> print(os.getcwd())
# C:\TEST\dirA\dirB\dirC
# >>> print(os.path.dirname(os.getcwd()))
# C:\TEST\dirA\dirB
# >>> print(os.path.basename(os.getcwd()))
# dirC
# >>> print(os.path.split(os.getcwd()))
# ('C:\\TEST\\dirA\\dirB', 'dirC')
# >>> pathname = os.path.join(os.getcwd(),'myfile.py')
# >>> pathname
# 'C:\\TEST\\dirA\\dirB\\dirC\\myfile.py'
# >>> (dirname, filename) = os.path.split(pathname)
# >>> dirname
# 'C:\\TEST\\dirA\\dirB\\dirC'
# >>> filename
# 'myfile.py'

x = "hello World"
y = " ".join(x.split()[::-1])
print(y)
print(" ".join(x.split()[-1:1]))

print(x[::-1])


def reverse_number(n):
    num = 0
    while(n>0):
        rev = n%10
        num = 10*num+rev
        n=n//10

    return num

print(reverse_number(186))