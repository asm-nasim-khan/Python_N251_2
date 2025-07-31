
# lst = [1,3,5,5,100]

# my_iter = iter(lst)

# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

# def my_generator():
#     yield 10
#     yield 12
#     yield 199
#     yield 200
    
# my_gen = my_generator()
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))


# decorator

# def my_decorator(my_func):
#     def wrapper():
#         my_func()
#         print("Before the function")
#         print("After")
#     return wrapper
    
# @my_decorator  
# def greetings():
#     print("Good morning")

# greetings()




# for i in range(len(lst)):
#     print(lst[i])
    

# for num in lst:
#     print(num)



# import pandas as pd

# import openpyxl as opx

# file = pd.read_excel('sample_data.xlsx',sheet_name="Sheet1")
# df = pd.read_csv('sample_data.csv')

# print(df.head())
# df.iloc[1,1] = 100
# print(df.head())



from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, Color

ft = Font(color="ff0080")
myfile = load_workbook("sample_data.xlsx")
sheet = myfile.active
sheet['B3'] = 150
sheet['B3'].alignment = Alignment(horizontal='center', vertical='center')
sheet['B3'].font = ft
# sheet['B5'] = 52
# sheet['B5'].alignment = Alignment(horizontal='center', vertical='center')
# sheet['C5'] = "Gulshan"

# sheet['A6'] = "Abdul"
# sheet['B6'] = 55
# sheet['B6'].alignment = Alignment(horizontal='center', vertical='center')
# sheet['C6'] = "Malibagh"
myfile.save("sample_data.xlsx")
myfile.close()



