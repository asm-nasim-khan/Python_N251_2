# lst = ["A","M","P"]
# lst.append("T")
# #       0   1   2   3
# #       1   2   3     x
# #      1.1
# print(lst[0])
# new_dict = {
#     1 : "Abc",
#     'man' : "M",
#     'p' : "P",
#     "eshikhon2020" : { "password": 12345, 'email': "abc@gmail.com", "name": "ABU MIA"  } # custom index
# }

# print(new_dict['eshikhon2020'])


# data = { "password": 12345, "email": "abc@gmail.com", "name": "ABU MIA"  }

# # print(data["password"])
# # method 1
# data["age"] = 20

# # method 2
# data.update({'nationality': "Asian"})
# print(data.values())

# for value in data.keys():
#     print(value, "=:=" ,data[value])
# lst_key = []
# lst_values = []

# for key,value in data.items():
#     lst_key.append(key)
#     lst_values.append(value)

# # print(lst_values)
# # print(lst_key)






keys =  ['password', 'email', 'name', 'age', 'nationality']
values = [12345, 'abc@gmail.com', 'ABU MIA', 20, 'Asian']

new_data = {}
for i in range(len(keys)):
    # new_data[ keys[i] ] = values[i]
    new_data.update({keys[i] : values[i]})
print(new_data)

