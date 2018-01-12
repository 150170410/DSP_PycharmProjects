import random

def gussGame():
    rn=random.randint(1,20)
    guess=0
    count=0
    while(guess!=rn and guess!="exit"):
        guess=input('Hi!!. provide your no: ')
        if guess=="exit":
            break
        count+=1
        if(int(guess)<rn):print("No is little less")
        elif(int(guess)>rn):print("No is little more")
        else:print("You Got it"+'in',count,'no of retries')


a=random.sample(range(2,50),10)
b=random.sample(range(4,40),12)
result=(i for i in a if i in b)
print(result)

#gussGame()
