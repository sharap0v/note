import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
# data.head()
print(data)
pd.get_dummies(data['whoAmI'])
# print(data['whoAmI'])
head = set()
for i in range(len(data['whoAmI'])):
    head.add(data['whoAmI'][i])
print(head)
for i in range(len(data['whoAmI'])):
    print(i, "  ", end='')
    for j in head:
        print(int(data['whoAmI'][i] == j), "     ", end='')
    print()