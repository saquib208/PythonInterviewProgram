

def product_except_self(a):
    m=[0]*len(a)
    p=1
    for i in range(len(a)):
        p=p*a[i]
    for j in range(len(a)):
        m[j]=p//a[j]

    return m

a=[8,9]
print(product_except_self(a))