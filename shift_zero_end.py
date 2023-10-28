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

b=[1,0,3,0,4,0,0,8,5]
print(shift_zero_end(b))
