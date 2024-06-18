def f(w):
    return w[0]

def l(w):
    return w[len(w)-1]

def m(w):
    n = len(w)
    return w[1:n-1]

def p(w):
    if len(w) <= 1:
        return True
    if f(w) != l(w):
        return False
    return p(m(w))

def main():
    print(p("allen"))
    print(p("bob"))
    print(p("o"))
    print(p("ma "))
    print(p([1,2, 3, 3, 2, 1]))
    print(p("12321"))
main()