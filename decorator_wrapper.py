import time

def time_it(f):
    def wrapper(*args):
        start=time.time()
        result=f(*args)
        end=time.time()
        print(f.__name__+" took",(end-start)*1000,"millisecond")
        return result
    return wrapper

@time_it
def cube(n):
    c=[]
    for i in n:
        c.append(i*i*i)
    return c

# n=range(1,12000)
# print(cube(n))

def exp(a):
    def base(b):
        return b**a

    return base

square=exp(2)
cube=exp(3)

# print(square(9))
# print(cube(3))

def memoize(f):
    mem={}
    def wrapper(x):
        if x not in mem:
            mem[x]=f(x)
            return mem[x]
        return wrapper


def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

# n=range(20)
# t1=time.time()
# print(list(map(fib,n)))
# t2=time.time()

#print("Program took time in calculatiion",(t2-t1)*1000,"millisec")

def fact(n):
    if n==0 or n==1:
        return 1
    elif n<0:
        return "Invalid input"
    else:
        return n*fact(n-1)


print(fact(500))

