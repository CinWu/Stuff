
##args is a tuple, can be used as a key in a hashtable
from functools import wraps
def memoize(func):
    t = {}
    @wraps(func)
    def inner(*args):
        print args
        if args in t:
            return t[args]
        else:
            t[args] = func(*args)
            return t[args]
    return inner

@memoize
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-2)+fib(n-1)

##much faster
def fib2(n,t={}):
    if n in t.keys():
        return t[n]
    elif n < 2:
        return 1
    else:
        r = fib2(n-2)+fib2(n-1)
        t[n] = r
        return r

@memoize
##longest common substring length
def lcslength(s1,s2,i,j):
    if i >= len(s1) or j >= len(s2):
        return 0
    elif s1[i] == s2[j]:
        return 1 + lcslength(s1,s2,i+1,j+1)
    else:
        return max(lcslength(s1,s2,i+1,j),lcslength(s1,s2,i,j+1))

import random
import string
def rstring(n):
    return "".join(random.choice(string.ascii_uppercase+string.digits) for x in range(n))

##Testing##

#print [fib(x) for x in range(1,35)]
#print [fib2(x) for x in range(1,35)]
#print fib(40)
#print lcslength("abcdefg","efrbca",0,0)
print lcslength(rstring(10),rstring(10),0,0)

##-------##

def decorate(f):
    def inner(*args,**kwargs):
        result = f(*args,**kwargs)
        return result
    return inner

def dec_with_param(decarg):
    print "declaring with dec_with_param"
    def decorate(f):
        def inner(*args,**kwargs):
            print "in inner w/ decarg: " + decarg
            result = f(*args,**kwargs)
            return result
        return inner
    return decorate

##@decorate hello = decorate(hello)
##@decorate('stuff') [hello = decorate('stuff')(hello)]?
@dec_with_param
def hello():
    return 'hello'

print hello()
