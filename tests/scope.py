a_string = "This is a global variable"
b_list = [1,2]
c = 1
def foo():
     a_string = "test" # 1
     b_list = [3,4]
     c = 2  # error: c += 2
     print locals()
foo()
print 'a_string = %s, b_list = %s, c = %s' %(a_string, b_list,c) # 2


print '*'*20

def foo(x):
     print locals()

foo(1)

print '*'*20

def foo(x, y=1):
     print x - y
foo(1)
foo(2, 0)
foo(2, y=2)
foo(y=2, x=3)

