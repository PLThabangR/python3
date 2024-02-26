def add_two(n):
    return n+2

num = [1,2,3,4,5]

added_two = list(map(add_two,num))

print(added_two)

# a list comprehension to print cube 
num1= [1, 3, 5, 10, 16] 
sqrdNum = [n*2 for n in num1]  
print(sqrdNum)  

sqrd_Num = [n*2 for n in num1 if n>3]  
print(sqrd_Num)  