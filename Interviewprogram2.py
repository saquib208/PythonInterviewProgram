def reverse_each_word(word):
    w=[]
    words=word.split()
    for i in range(len(words)-1,-1,-1):
        w.append(words[i])
    return " ".join(w)


# word = "My first python program"
# print(reverse_each_word(word))


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
print(word_count(ss))
