# import class17
file_h = open('input.txt','r').read()

# # print(type(file_h))
# print(file_h)

data = file_h.split("\n")
# # print(data)


# for line in data:
#     print(line[1:-1].split(","))
output_h = open('output.txt','a')

for pair in data:
    pairs = pair.split(",")
    for i in range(len(pairs)):
        num = pairs[i]
        if i==0:
            num = num[1:]
        elif i == len(pairs) - 1:
            num = num[0:len(num)-1]
        # print(type(num))
        if int(num)%2 == 0:
            output_h.write(f"{num} : Even\n")
        else:
            output_h.write(f"{num} : Odd\n")
            
# for pair in data:
#     pairs = pair.split(",")
#     for num in pairs:
#         if int(num)%2 == 0:
#             print(num," : Even")
#         else:
#             print(num," :odd")
    # print(f"Prime number between {pairs[0]} and {pairs[1]}")
    # class17.prime_printer(int(pairs[0]),int(pairs[1]))
    # print()
    # print()
    
    
# TEXT = "my name is.how are you.goodbye.OKY"

# print(TEXT.split("."))

