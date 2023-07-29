g = 10 #===>> This is Global

def func1(n):
    l = 5 #===>> This is Local
    m = 23
    print(l,m)
    
    # to change the GLOBAL variables use the 'global' keywords:
    global g
    g = g + 50
    print(g,l,m)

    print(n, "I have printed")

    '''Conclusion :===>> Any variable which is inside any FUNCTION is called LOCAL variable BUT those variable which is outside the FUNCTION is called GLOBAL variabels'''

func1("This is me")    