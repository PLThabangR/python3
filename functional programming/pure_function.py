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