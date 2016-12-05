def one(*args):
    print args  # 1

one()
one(1, 2, 3)

def two(x, y, *args):  # 2
    print x, y, args

two('a', 'b', 'c')

dic = {'a':1, 'b':2}
def thr(**k):
    print k
thr(**dic)
thr(a=1, b=2)



def add(x, y):
    print x + y

lst = [1, 2]
lst2 = (1, 3)
lst3 = xrange(0,2)
add(lst[0], lst[1])  # 1
add(*lst)  # 2
add(*lst2)
add(*lst3)

def add(*a, **k):
    print a,k
add(1,3,b=4,c=5) # error: add(1,3,b=4,c=5,6,d=7)
