favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for desert in favorites:
    print("I like ",desert)

for x,desert in enumerate(favorites):
    print(x,"I like ",desert)

count =1
while count< len(favorites):
    print(count,"While I like",favorites[count])
    count+=1

for desert in favorites:
    if desert == "Churros":
        print("My favourite is :",desert)
        break
    else:
        print("Not my favourite :",desert)    

#Using conitnue
for dessert in favorites:
    if dessert == 'Churros':
        continue
    print('Other desserts I like are', dessert)