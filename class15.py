lst = ["mango","Banana","Pineapple","apple","Guava"]

# print(lst[1])

my_fruits = {
    "m": "mango",
    "b": "Banana",
    "p": "pineapple",
    "a": "apple",
    "g": "Guava",
    (1,2,3) : "list"
}

# print(my_fruits.keys())
# print(my_fruits.values())
# print(my_fruits.items())

# for key in my_fruits.keys():
#     print(my_fruits[key])

# for key,value in my_fruits.items():
#     print( value)

# my_fruits["new"] = "Bangladesh"
# my_fruits.update( {1:"One", 2: "two"} )
# print(my_fruits)


# var = float(input("Please Enter a number:"))
# print(var + 10 )
# print(var*2)

# start = 0
# end = 10
# step = 2
# for i in range(start,end,step):
#     if i == 6:
#         break
#     print(i)
# print("done")


# lst = []
# while True:
#     num = input("Enter a number: ")
#     if num == "stop":
#         break
#     lst.append(int(num))

# print(lst)


start = 0
end = 10
step = 2
for i in range(start,end,step):
    print("OKY")
    if i == 6:
        continue
    print(i)
print("done")

start = 0
end = 10
step = 2
for i in range(start,end,step):
    if i == 60:
        break
    print(i)
else:
    print("done")