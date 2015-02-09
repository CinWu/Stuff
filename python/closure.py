import random

def inc(x):
    return x+1

f = inc
#f works as inc

def dec(x):
    return x-1

functions = [inc,dec]

flist = [random.choice(functions) for x in range(10)]

fd = {'a':inc, 'b':dec}

def wrapper():
    print "In the wrapper before inner declared"
    def inner():
        print "In the inner function"
    inner()
    print "Still in the wrapper"

def make_adder(x):
    def f(n):
        return n+x
    return f

x = wrapper()
#print x() should print inner

add3 = make_adder(3)
add5 = make_adder(5)

def make_counter():
    count = [0]
    def inc():
        count[0] = count[0]+1
        return count[0]
    return inc

c1 = make_counter()
print c1()
print c1()

c2 = make_counter()
print c2()

def make_counter_class():
    count = [0]
    def inc():
        count[0] = count[0] + 1
    def dec():
        count[0] = count[0] - 1
    def reset():
        count[0] = 0
    def get():
        return count[0]
    return {'inc':inc,'dec':dec,'reset':reset,'get':get}

c1 = make_counter_class()
print c1['get']()
c1['inc']()
print c1['get']()        
