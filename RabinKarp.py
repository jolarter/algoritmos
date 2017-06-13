def RabinKarp(text, subtext, d, q):
    n = len(text)
    m = len(subtext)
    h = (d**(m-1))%q
    p = 0
    t = 0
    result = []
    for i in range(m):
        p = (d*p+ord(subtext[i]))%q
        t = (d*t+ord(text[i]))%q
    for s in range(n-m+1): # note the +1
        if p == t: # check character by character
            match = True
            for i in range(m):
                if subtext[i] != text[s+i]:
                    match = False
                    break
            if match:
                result = result + [s]
        if s < n-m:
            t = (t-h*ord(text[s]))%q # remove letter s
            t = (t*d+ord(text[s+m]))%q # add letter s+m
            t = (t+q)%q # make sure that t >= 0
    return result
    
print(RabinKarp("266266266266", "626", 257, 11))
print(RabinKarp("xxxxxx", "xx", 40999999, 999999937))
