with open('input.txt','r') as f:
    n=list(eval(f.readline()))
print(n)
x=sorted(n)
print(x)
x.sort(reverse=True)
print(x)
print(len(n))
print(max(n))
print(min(n))
print(n+[111])
n[2]=222
print(n)
with open('output.txt','w') as f:
    f.write(str(n))
