def get_total(a, b):
    #local variable declared inside a function
    total = a + b;
    return total

print(get_total(5, 2))
7

# Accessing variable outside of the function:
print(total)
#NameError: name 'total' is not defined

def get_total(a, b):
    #enclosed variable declared inside a function
    total = a + b

    def double_it():
        #local variable
        double = total * 2
        print(f"The total is doubled:{double}")

    double_it()
    return total

#double variable will not be accessible
print(get_total(2,2))


special = 5

def get_total(a, b):
    #enclosed scope variable declared inside a function
    total = a + b
    print("A",special)

    def double_it():
        #local variable
        double = total * 2
        print("B",special)

    double_it()

    return total

get_total(2,2)