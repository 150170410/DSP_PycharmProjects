def checkPrime(num):
    for i in range(2,num):
        if(num%i)==0:
            print('Not a prime')
            break
        else:print('Number is prime')

def findAllPrime(low,up):
    for num in range(low,up):
        if num>1:
            for i in range(2,num):
                if(num%i)==0:
                    break
            else:
                print(num)








#inputnum=int(input('Please give a number:'))
#checkPrime(inputnum)
lowrange=int(input('PLease provide low range: '))
upperrange=int(input('please providr upper range: ' ))
findAllPrime(lowrange,upperrange)
