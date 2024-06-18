       for p in l:
            if len(p) >= 3:
                if p in f: # L4 
                    f[p] += 1
                else:
                    f[p] = 0
                    # L5
    m = None
    for p in f:
        m = p
        t = 0
        for p in l.keys(): # L6 :
            t += f[p]
            if f[p] < t:# L7 :
                m = p
    a.close()