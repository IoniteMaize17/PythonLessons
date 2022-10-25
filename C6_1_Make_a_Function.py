#function is a small partial program, do 1 activity within 1 program
#
def my_fake_lambda(a, b):
  return a * b

def myfunc(n):
  return lambda a : a * n
  #return inner_function(10, n)

def multply_by_1(n):
  return n*1
def multply_by_2(n):
  return n*2


function_list = []

for i in range(1000):
  function_list.append(myfunc(i))

print(   function_list[5](10)        )
print(   function_list[7](10)        )
print(   function_list[8](10)        )

#mytripler = myfunc(3)
#print(type(myfunc))

#print(myfunc(3))
