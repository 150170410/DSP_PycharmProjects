import random


a=random.sample(range(2,50),10)
b=random.sample(range(4,40),12)
result=(i for i in set(a) if i in b)
print(result)
