def a2(*args):

    a= []

    for i in args:
        a.append(i)
        print(a)
    return a


q,w,e = a2('a','b','c')
print(q,w,e)
