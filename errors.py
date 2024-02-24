def divide_by(a,b):
    return a/b

try:
    ans = divide_by(40,2)
    print(ans)
except Exception as e:
    print("Error:",e)