"""
    Loop
            1. For Loop (Smart)
            2. While Loop
            
            * For each loop
            * Do while Loop
    
    """
# print(list(range(1,21,3))) # Start(including), Stop(excluding) , Step

# print(list(range(5,21))) # Start(including), Stop(excluding) , Step = 1

# print(list(range(21))) # Start(including) = 0 , Stop(excluding) , Step = 1

# for i in range(1001):
#     if i%2== 0:
#         print(i,"is Even")
#     else: print(i, "is Odd")

# start = 1
# stop = 101
# step = 1
# while start<stop:
#     if start%2== 0:
#         print(start,"is Even")
#     else: print(start, "is Odd")
#     start = start + step # increment
    
#     # 0,2,4,6,8
# start = start + step*2(start/3) # increment   
# 0, -7, 9, - 8, 23

start = 23

if start%2== 0:
    print(start,"is Even")
else: 
    print(start, "is Odd")

if start%2== 0:print(start,"is Even")
else:print(start, "is Odd")

print(str(start)+" is Even" if start%2 == 0 else str(start)+" is Odd")

print(start,"is Even") if start%2 == 0 else print(start,"is Odd")