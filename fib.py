#Programacion dinamica

def fib(n):
    if n==0 or n==1:
        r=1
        s=1
    else:
        r1,s1=fib(n-1)
        r2,s2=fib(n-2)
        r=r1+r2
        s=s1+s2+1
    return r,s

def fibma(n,mem):
    if mem[n]==None:
        if n==0 or n==1:
            mem[n]=1
            s=1
        else:
            r1,s1=fibma(n-1,mem)
            r2,s2=fibma(n-2,mem)
            mem[n]=r1+r2
            s=s1+s2+1
        return mem[n],s
    else:
        return mem[n],1

def fibm(n):
    mem = [None for i in range(0,n+1)]
    return fibma(n,mem)

def dynamicfib(n):
    mem = [None for i in range(0,n+1)]
    mem[0] = 1
    mem[1] = 1
    for i in range(2,n+1):
        mem[i] = mem[i-1]+mem[i-2]
    return mem[n]

def dynamicfib2(n):
    mem = [1,1]
    for i in range(2,n+1):
        mem[i & 1] = mem[(i-1) & 1] + mem[(i-2) & 1]
    return mem[n & 1]

print fib(30)
print fibm(30)
print dynamicfib(30)
print dynamicfib2(30)
