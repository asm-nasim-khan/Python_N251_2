# def Greetings(age ):
#     if age==20:
#         return
#     print(age)
#     Greetings(age+1)
    

# x = Greetings(13)


def is_prime(x):
    # 5 ==> 1, 5
    divisor_count = 0
    for i in range(2,x):
        if x % i == 0:
            divisor_count = divisor_count + 1
    return divisor_count

def prime_printer(start,end):
    for i in range(start,end):
        if i==1:
            continue
        count = is_prime(i)
        if count == 0:
            print(i,end=",")

# print(__name__)
if __name__=='__main__':
    prime_printer(1,21)