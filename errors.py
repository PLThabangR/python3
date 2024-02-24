def divide_by(a,b):
    return a/b

try:
    ans = divide_by(40,0)
    print(ans)
except Exception as e:
    print("Error:",e)
    print(e.__class__)
except Exception as e:
    print(e)