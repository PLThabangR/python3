#str[start:stop:step]

trial="reverse"
new_trail = trial[::-1]
print(new_trail)

#######################
data = [2,3,5,7,11,13,17,19,23,29,31]

# Ex1: List comprehension: updating the same list
data=[x+2 for x in data]
print("Updating the list: ", data)

new_data=[x*2 for x in data]
print("Creating new list",new_data)

fourx = [x for x in new_data if x%2==0]
print("Divisible by four ",fourx)