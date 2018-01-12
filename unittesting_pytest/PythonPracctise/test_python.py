#------even and div by 4/odd----------
def checkEven(InputData):
    if(InputData%2==0):
        print(InputData,"is an even number")
        if(InputData%4==0):
            print(InputData,"is divissile by 4 too")
    else:print("Number is odd")

#-------------check given no is prime------
def checkPrime(num):
    for i in range(2,num):
        if(num%i)==0:
            print('Not a prime')
            break
        else:print('Number is prime')

#-------- find all prime nos in a range-----
def findAllPrime(low,up):
    for num in range(low,up):
        if num>1:
            for i in range(2,num):
                if(num%i)==0:
                    break
            else:
                print(num)

#-----------generate fibonocci series with n nos--------
def fibonicci(num):
    if num<2:return num
    else:return fibonicci(num-1)+fibonicci(num-2)

inputnum=int(input('How many nos u want'))
for i in range(inputnum):
    print(fibonicci(i))

#finding factorial of a number
def fact_orial(a):
	i=1
	feb=1
	while(i<=a):
		feb*=i
		i=i+1
		print feb
	return feb

#Passing value
x=int(input('Give a number:'))
print fact_orial(x)

#----------check a string is pallindrome----------
def stringList(data):
    if(data==data[::-1]):
        print(data+" is a pallindrome")
    else:print(data+" Sorry . is not a pallindrome")

#a=input("Please give a String: ")
stringList("madam")

#--------reverse each word of a string-----
def revString(indata):
    return indata[::-1]

def revSentence(strdata):
    mydata=strdata.split()
    result=''
    for element in mydata:
        result+=' '+revString(element)
    return result

print (revSentence('My name is Anthony'))

#program to count the number of vowels.

def count_vowel(sentence):
	num=0
	for char in sentence:
		if char in 'aeiouAEIOU':
			num+=1
	return num


sentence=raw_input('Write a sentence: ')
print count_vowel(sentence)


#To find program to find GCD of 2 numbers
def mygcd(a,b):

	if(b==0):
		return a
	else:
		return mygcd(b,a%b)

#Passing value from console
x=int(input("Enter first number: "))
y=int(input("Enter first number: "))

print ("GCD of ",x,'&',y,'is',mygcd(x,y))

#program to find GCD of 2 numbers
def gcd_2(a,b):
	if(b==0):
		return a
	else:
		return gcd_2(b,a%b)

def gcd_n(mylist):
	if(len(mylist)<=2):
		print '::Please provide atleast 2 nos::'
	else:
		res=gcd_2(mylist[0],mylist[1])
		for i in mylist[2:]:
			res=gcd_2(res,i)
		return res
#------search for a element in a list----

def SearchElement(alist,ele):
    for i in alist:
        if i==ele:return True
    else:return False

a = [1, 3, 5, 30, 42, 43, 500]
print(SearchElement(a,30))

#--------find list of element less than a given no from a list
def listTest(listdata,num):
    print(listdata)
    reslist=[]
    for element in listdata:
        if(element<num):
            print(element)
            reslist.append(element)
    print(reslist)

#----find list of nos in a range div by a given num
def checklist(number):
    x=range(1,50)
    res=[]
    for element in x:
        if(element%number==0):
            res.append(element)
    return res

num=int(input("PLease provide a number: "))
print(checklist(num))
#-------------compare two list and create new list--------

def checkListDiv(list1,list2):
    result=[]
    for num in b:
        if num in a and num not in result:
            result.append(num)
    return result

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(checkListDiv(a,b))

#------------create list of even nos from a given list in one line--------
def listComprehension(list1):
    resultlist=[element for element in list1 if element%2==0 ]
    #for element in list1:
     #   if(element%2==0):
      #      resultlist.append(element)
    print(resultlist)

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100,200]
listComprehension(a)

#--------------using random function-----

import random

a=random.sample(range(2,50),10)
b=random.sample(range(4,40),12)
result=(i for i in set(a) if i in b)
print(result)

#-----find both end values of a list-----

def listEnds(data):
    return [data[0],data[len(data)-1]]

a = [5, 10, 15, 20, 25]
print (listEnds(a))

#----------remove duplicates from a list-----
def removeDuplicate(a):
    return set(a)

a = [1,2,3,4,3,2,1]
print(a)
print(removeDuplicate(a))


