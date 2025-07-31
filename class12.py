my_list = [1,2,3,4,45,5,"Name",5.4] 

# String : List of Characters

name = "HappyBirthday59.5"
name_list = ["H","a","p","p","y","B","i","r","t","h","d",'a',"y"]
# vowel = 0
# conso = 0

# for i in range(len(name_list)):
#     print(name_list[i],end="")

# for cha in name_list: # for each loop
#     print(cha,end="")
# vowel = []
# conso = []
# for i in range(len(name_list)):
#     if name_list[i].lower() in "aeiou":
#         vowel.append(name_list[i])
#     else:
#         conso.append(name_list[i])

# print(vowel)
# print(conso)
# name_list[5] = "C"

# print()
# print(name_list)

# gm = "happy"

# print(id(gm))
# gm += "Birthday"
# # print(id(gm))

# lst = [10,20,30,40]
# print(id(lst))
# lst.append(99)

# lst += [100,200]

# lst.extend([500,1000])
# print(id(lst))

# print(lst)


# lst = [-2,0,-5,8,-8,7,12,45,90,-100]
# pos = []
# neg = []
# for item in lst:
#     if item >= 0:
#         pos.append(item)
#     else:
#         neg.append(item)

# print(pos)
# print(neg)


# lst = [10,13,15,12,17]
# total = 0
# for item in lst:
#     total += item
#     # if item%2 == 0:
#     #     print(item,": Even")
#     # else:
#     #     print(item,": Odd")
# print(total)

# lst = [10,13,15,10,12,17]

# # lst.pop(1) # removes the last element or given index

# # lst.remove(10)

# print(lst)

#tuple


my_tuple = (10,13,15,10,12,17)
print(type(my_tuple))
# total = 0
for item in my_tuple:
    # total += item
    if item%2 == 0:
        print(item,": Even")
    else:
        print(item,": Odd")
# print(total)