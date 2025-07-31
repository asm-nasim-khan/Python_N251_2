# text = "12,20,30,50,64,73"

# num = text.split(",")

# print(num)

text = "(31,2),(10,23),(35,19)"
data = text.split(",")
my_list = []
temp = []
for item in data:
    if item[0] =="(":
        temp.append(int(item[1:]))
    else:
        temp.append(int(item[:-1]))
        my_list.append(tuple(temp))
        temp = []
        
# print(my_list)


# text = "name: Eshikhon, age: 28, address: Dhaka"
# data = text.split(",")
# # print(data)
# my_dict = {}
# for pair in data:
#     temp = pair.split(":")
#     key = temp[0].strip()
#     value = temp[1].strip()
#     my_dict[key] = value
# print(my_dict)

# print("   Eshikhon    ".strip())


email = "abc@gmail.com,nasim123@yahoo.com,1eshikhon@.com"
data = email.split(",")
for item in data:
    print(item)
    