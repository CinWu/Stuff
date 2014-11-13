import random

##doesnt allow you to transform your function
def d1(x):
    r = x()
    return r+r

def doubler(func):
    def inner():
        result = func()
        return result + result
    return inner

def capit(func):
    def inner():
        result = func()
        return result.capitalize()
    return inner

##adding doubler is like later on saying get_name = doubler(get_name)
##Decorators:
#@capit
#@doubler
def get_name():
    names = ['tom','sue','alan','scott','sarah','howie']
    return random.choice(names)

##*args gives all the args listed
##**kwargs = keyword args
def sample(*args,**kwargs):
    print args
    print kwargs

def argprinter1(func):
    def inner(*args,**kwargs):
        print args
        print kwargs
        print func.__name__
        result = func(*args,**kwargs)
        ##we could do logging or something here
        return result
    return inner

@argprinter1
def f1(a,b,c):
    print a,b,c

##import decorator
from functools import wraps
def argprinterfinal(func):
    @wraps(func)
    def inner(*args,**kwargs):
        print args
        print kwargs
        print func.__name__
        result = func(*args,**kwargs)
        ##we could do logging or something here
        return result
    return inner

@argprinterfinal
def f2(a,b,c):
    print a,b,c
    
##Error because hello expects a variable but inner doesn't
#@doubler
#def hello(x):
#    return x


##Testing##

print get_name()
print d1(get_name)
print "-----------"

get_name = capit(get_name)
print get_name()
print "-----------"

get_name = doubler(get_name)
print get_name()
print "-----------"

sample('dog','cat')
print "-----------"

f1(1,2,3)
print f1.__name__
print "-----------"

f2(1,2,3)
print f2.__name__
print "-----------"
##-------##
