# square = lambda lst: [x**2 for x in lst]

# print(square([3,7]))

# f(x) = 2x^2 + 2x + 7
# f(9)

# def f(x):
#     return 2*x**2 + 2*x + 7

# for item in [2,3,4,9]:
#     print(item,":",f(item))
    
# f = lambda lst: [2*x**2 + 2*x + 7 for x in lst]

# print(f([2,3,4,9]))


lst = [1,2,3,4,4,5,6]
# result = [item**2 for item in lst]
# # for item in lst:
# #     result.append(item**2)
# print(result)

# my_num = [i for i in range(10)]
# print(my_num)

# my_set = {item**2 for item in lst}

# print(my_set)
key = ['name','age','gender']
value = ['eshikhon',20,'male']

my_dict = {key[i]:value[i] for i in range(len(key))}
# print(my_dict)

# import datetime as dt

# # print(dt.datetime.tzinfo())
# print(dt.datetime.now().minute)
# print(dt.datetime.now().date())
# print(dt.datetime.now().time())
# print(dt.datetime.now().timetz())


# import math

# print(math.sqrt(25))
# print(25 ** 0.5)
# print(math.pow(3,2))
# print(math.factorial(3)) # 1*2*3
# print(math.pi)
# print(math.inf)

import json

data = json.dumps(my_dict)

# print(type(my_dict))
# print(data)

load_data = json.loads('{"name": "eshikhon", "age": 20, "gender": "male"}')
print(type(load_data))






