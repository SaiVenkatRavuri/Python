s=input("enter string:")
i=len(s)-1
res=""
while i>=0:
    res+=s[i]
    i-=1
print(res)
