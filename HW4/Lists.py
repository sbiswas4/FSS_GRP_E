def collect(t,f):
    print "collect"
    out=[]
    if t:
        for i,v in enumerate(t):
            out[i] = v
    return out
def copy(t):
    return type(t) != 'table' and t or collect(t, copy)
