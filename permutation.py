

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


def permute(s, answer):
    if (len(s) == 0):
        print(answer, end="  ")
        return
    for i in range(len(s)):
        ch = s[i]
        left_substr = s[0:i]
        right_substr = s[i + 1:]
        rest = left_substr + right_substr
        permute(rest, answer + ch)


# Driver Code

s = 'abc'
permute(s, answer)