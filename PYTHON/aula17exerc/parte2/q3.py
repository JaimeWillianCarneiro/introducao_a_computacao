import 
def maxfreq (nome):
    a =file(nome, 'r')# L1
    f = []# L2
    for l in a:
        
        l = l.split()# L3
        for p in l:
            if len(p) >= 3:
                if f[p]!=0: # L4 
                    f[p] += 1
                else:
                    f.append(p)
                    # L5
    m = None
    for p in f:
        m = p
        t = 0
        for p in f.values(): # L6 :
            t += f[p]
            if f[p] > t:# L7 :
                m = p
    a.close()
    return m, t # L8

def main ():
    arq = input('Nome do arquivo: ')
    p, f = maxfreq(arq)
    print ('palavra:', p, 'freq. rel.:', f)

main()