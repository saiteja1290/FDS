import pandas as pd

a=pd.Series([4,3,7,9])
b=pd.Series([1,2,3,4])
print(a)
print("Datatype:", a.dtype)
print("Size:", a.size)
print("Shape:", a.shape)
print(b)
print("a+b:", a+b)

a.index=['one','two','three','four']
b.index=['three','one','five','two']
print("a+b:", a+b)
print("Sum of elements in a:",sum(a))

c=pd.Series({'maths':50,'physics':45,'chem':60})
d=pd.Series({'chem':23,'maths':50,'english':45})
print(c)
print(d)
print("c+d:",c+d)
