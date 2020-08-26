from django.test import TestCase

# Create your tests here.
l1 = ['a', 'b', 'c', 'd','l']
l2 = [2, 6, 9, 6,9]
dic = dict(zip(l1, l2))
print(dic)

print(['val%s'% i for i in range(1, 7)])

import random
print(random.randint(1, 100))