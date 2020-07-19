

def permutation(x):
    if len(x)==0:
        return []
    elif len(x)==1:
        return [x]
    else:

        l = []
        for i in range(len(x)):
            p=x[i]
            p1=x[:i]+x[i+1:]
            for j in permutation(p1):
                l.append("".join([p]+[j]))
        return l


print(permutation('cat'))

print(len(permutation('golf')))

