

def product_except_self(a):
    m=[0]*len(a)
    p=1
    for i in range(len(a)):
        p=p*a[i]
    for j in range(len(a)):
        m[j]=abs(p)//a[j]

    return m

#a=[2,4,3]

a=[-1,0,3]

#print(product_except_self(a))

def get_product_arary(x):
    n=len(x)
    left,right = [1]*n,[1]*n
    product_array= []

    for i in range(1,n):
        left[i]=left[i-1]*x[i-1]
    print(left)

    for i in range(1,n):
        right[i] = right[i-1]*x[::-1][i-1]
    print(right)
    for i in range(n):
        product_array.append(left[i]*right[::-1][i])
    return product_array
#print(get_product_arary(b))

def product_except_self_2(arr):
    n=len(arr)
    print(n)
    result=[0]*n
    rp =1
    for i in range(0,n):
        result[i]=rp
        rp =rp*arr[i]
    print("Result-->",result)
    rp =1
    for i in range(n-1,-1,-1):
        result[i]=result[i]*rp
        rp =rp*arr[i]


    return result


b = [2,-1,5,4]
#
# print(product_except_self_2(b))


def product_except_self(arr):
    result = []
    left = []
    prod = 1
    for x in arr:
        left.append(prod)
        prod *= x
    print("left",left)
    right = []
    prod = 1
    for i in (reversed(arr)):
        right.append(prod)
        prod *= i
    print("right",right)
    n= len(arr)
    for i in range(n):
        result.append(left[i]*right[n-1-i])
    return result


# arr=[2,3,4]
# print(product_except_self(arr))


def product_except_self_3(arr):
    n = len(arr)
    result = [1]*n
    right =[1]*n
    left = [1]*n

    right[0] =1
    left[n-1] = 1

    for i in range(1,n):
        left[i] = arr[i-1]*left[i-1]
    print("left",left)

    for i in range(n-2,-1,-1):
        right[i]=arr[i+1]*right[i+1]
    print("right",right)

    for i in range(n):
        result[i] =left[i]*right[i]
    return result

arr=[-1,2,3,4]
print(product_except_self_3(arr))
