class A:
   a = 1

class B(A):
   a = 2

class C(B):
   pass

c = C()
b=B()
c.a=5
print(c.a)
print(b.a)
print(issubclass(A,B))
print(issubclass(B,A))