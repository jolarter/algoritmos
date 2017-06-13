# comb(n,k) = comb(n-1,k-1)+comb(n-1,k)
# comb(n,0) = 1
# comb()
# comb()
# comb()

def comb(n,k):
    if k==0:
        r=1
    elif n<k:
        r=0
    else:
        r = comb(n-1,k-1)+comb(n-1,k)
    return r

print comb(10,5)
print comb(4,2)
print "Recursivo"
#print comb(45,6)

def combma(n,k,mem):
    if mem[n][k] == None:
        if k==0:
            mem[n][k]=1
        elif n<k:
            mem[n][k]=0
        else:
            mem[n][k] = combma(n-1,k-1,mem)+combma(n-1,k,mem)
    return mem[n][k]

def combm(n,k):
    mem = [[None for j in range(0,k+1)] for i in range(0,n+1)]
    r = combma(n,k,mem)
    print(mem)
    return r

print "Con memoria"
print combm(8,4)

def dynamiccom(n,k):
    mem = [[None for j in range(0,k+1)] for i in range(0,n+1)];
    for i in range(0,n+1):
        for j in range(0,k+1):
            if j == 0:
                mem[i][j] = 1
            elif i < j:
                mem[i][j] = 0
            else:
                mem[i][j] = mem[i-1][j-1]+mem[i-1][j]
    print(mem)
    return mem[n][k]

print "Dinamico"
#print dynamiccom(45,6)
print dynamiccom(8,4)

def dynamiccomb2(n,k):
    mem = [1] + [0 for j in range(1,k+1)]
    for i in range(1, n+1):
        for j in range(min(n,k),max(i-k-1,0),-1):
            mem[j] = mem[j]+mem[j-1]
            print(mem)
    return mem[k]

print dynamiccomb2(8,4)
