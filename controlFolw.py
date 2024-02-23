bill_total=int(input("Enter a value between 10 to 300: "))
dicount=10
dicount2=20

if bill_total >=100 and bill_total<200:
    print("Bill is greater than 100!")
    bill_total=bill_total-dicount
elif bill_total>=200:
    print("Bill greater than 200")
    bill_total=bill_total-dicount2
else :
    print("Bill is less than 100")

print(f"Total bill is :{bill_total}")
#############################################
#Light is currently off
current = False
if not current:
    current = False
    print('Turning light off')
else:
    current = True
    print('Turning light on')
############################################
##Discount for loyal customers

loyaltCustomer = True
totalBill=49

if loyaltCustomer and totalBill >100:
    print("Loyal customer 20% discount")
    totalBill=totalBill-(float(totalBill/100))*20
elif totalBill>100:
     print("Got 10% discount")
     totalBill=totalBill-(float(totalBill/100))*10
else:
    print("Sorry no discount")

print(f"Total Bil : {totalBill}")
#The above code snippet first checks to see if the customer is part of the loyalty program and if they are spending over $100. If both conditions are met, a discount of 20% is applied to the bill. The elif statement will only be executed if the first if condition is not met. The elif statement will only check if the bill is over $100 and if it is, it will apply a discount of 10%  to the bill.

#Switch
#Match statements
