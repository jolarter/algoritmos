def u(j,w,weights,utilities):
    if j == 0:
        result = 0
    elif w < weights[j]:
        result = u(j - 1, w, weights,utilities)
    else:
        result = max(u(j-1, w, weights, utilities), utilities[j] + u(j-1, w - weights[j], weights, utilities))
    return result

def um(j,w,weights,utilities,m):
    if m [j][w] == None:
        if j == 0:
            result = 0
        elif w < weights[j]:
            result = u(j - 1, w, weights,utilities,m)
        else:
            result = max(u(j-1, w, weights, utilities,m), utilities[j] + u(j-1, w - weights[j], weights, utilities,m))
        m[j][w] = result
    else:
        result = m[j][w]
        return result

def umm(w,weights,utilities):
    n = len(weights)-1
    m = [[None for w in range(0,w+1)] for j in range(0,n+1)]
    print(m)
    '''return um(n,weight,weights,utilities,m)'''

def udyn0(w,weights,utilities):
    n = len(weights)-1
    m = [[0 for w in range(0,w+1)]]+[[None for w in range(0,w+1)] for j in range(1,n+1)]
    print (m)

w0=[1,2,3,4]
u0=[240,200,140,150]
umm(4,w0,u0)
udyn0(4,w0,u0)
