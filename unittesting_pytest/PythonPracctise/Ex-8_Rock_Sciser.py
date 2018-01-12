import sys
def rockScisser(u1,u2):
    a='rock'
    b='scisser'
    c='paper'
    if(u1==a and u2==b):print('User1 wins')
    elif((u1==b and u2==c)):print('User1 wins')
    elif((u1==c and u2==a)):print('User1 wins')
    else:print('Invalid input provided')
    sys.exit()



user1=input("Hi user1, please give your option: ")
user2=input("Hi user1, please give your option: ")

rockScisser(user1,user2)
