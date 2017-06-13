def printa(A,s,t):
    cadena = ""
    for i in range(0,len(s)+1):
        for j in range(0,len(t)+1):
            cadena += " "
            if i == 0 and j == 0:
                cadena += ""
            elif j == 0:
                cadena += s[0:i]
            elif i == 0:
                cadena += t[0:j]
            else:
                cadena += "None" if A[i-1][j-1]==None else str(A[i-1][j-1])
            cadena += "\t|"
        cadena += "\n"
    print cadena

def d(i,j,s,t):
    if min(i,j)==-1:
        result = max(i,j)+1
        c = 'b'
    elif s[i] == t[j]:
        result = d(i-1,j-1,s,t)
        c = 'c'
    else:
        result = min(d(i-1,j,s,t),d(i,j-1,s,t),d(i-1,j-1,s,t))+1
        c = 'd'
    """print(i,j,s[0:i+1],t[0:j+1],result,c)"""
    return result

def cd(s,t):
    return d(len(s)-1,len(t)-1,s,t)

"""print cd ("sitten","sitted")"""
"""print cd ("sitti","sitten")"""

def dm(i,j,s,t,m):
    if m[i][j] == None:
        if min(i,j)==-1:
            m[i][j] = max(i,j)+1
            c = 'b'
        elif s[i] == t[j]:
            m[i][j] = dm(i-1,j-1,s,t,m)
            c = 'c'
        else:
            m[i][j] = min( dm(i-1,j,s,t,m) , dm(i,j-1,s,t,m) , dm(i-1,j-1,s,t,m) ) + 1
            c = 'd'
        """printa(m,s,t)"""
        """print(i,j,s[0:i+1],t[0:j+1],m[i][j],c)"""
    return m[i][j]

def cdm(s,t):
    r = 0
    i = len(s)-1
    j = len(t)-1
    m = [[None for a in range(0,j+1)] for b in range(0,i+1)]
    printa (m,s,t)
    r = dm(i,j,s,t,m)
    printa (m,s,t)
    return r

"""print cdm ("123def","ghi123")"""

"""print cdm("sitti","sitten")"""
def dm2(i,j,s,t,m):
    if m[i][j] == None:
        if min(i,j)==-1:
            m[i][j] = max(i,j)+1
            c = 'b'
        elif s[i] == t[j]:
            m[i][j] = dm(i-1,j-1,s,t,m)
            c = 'c'
        else:
            m[i][j] = min( dm(i-1,j,s,t,m) , dm(i,j-1,s,t,m) , dm(i-1,j-1,s,t,m) ) + 1
            c = 'd'
        """printa(m,s,t)"""
        """print(i,j,s[0:i+1],t[0:j+1],m[i][j],c)"""
    return m[i][j]

def cdm2(s,t):
    r = 0
    i = len(s)-1
    j = len(t)-1
    m = [[None for a in range(0,j+1)] for b in range(0,i+1)]
    printa (m,s,t)
    r = dm(i,j,s,t,m)
    printa (m,s,t)
    return r

print cdm2("123def","ghi123")
""" python levenshtein.py > log.txt ls -l > log.txt """
