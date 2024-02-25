my_list=[1,2,3]
#creating a pure funcction
#a pure function does not edit the global state
def add_to_list(list,item):
   
    nl= list.copy()
    nl.append(item)
    return nl

new_list = add_to_list(my_list,10)

print(my_list)
print(new_list)

def sum(n):
   if n == 1:
       return 0
   return n + sum(n-1)

a = sum(5)
print(a)
some = ["aaa", "bbb"]

def aa(some):
   return

numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
   return numbers < 50

small = list(map(lesser, numbers))
print(small)