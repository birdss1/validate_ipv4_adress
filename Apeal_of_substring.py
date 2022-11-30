s=input()

l=[]
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        l.append(s[i:j])

# l = [s[i: j] for i in range(len(s))
#           for j in range(i + 1, len(s) + 1)]
print(l)
ans=0
for i in l:
    a=set(i)
    ans+=len(a)
print(ans)
