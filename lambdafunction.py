f = lambda x,y: x + y
print(f(2,3))

a = lambda g: lambda h: lambda i: g * h * i
print(a(2)(3)(5))

o = lambda j: lambda k,m: lambda l: (j * (k + m)) % l
print(o(2)(3,4)(5))