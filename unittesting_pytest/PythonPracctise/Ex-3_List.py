def listTest(listdata,num):
    print(listdata)
    reslist=[]
    for element in listdata:
        if(element<num):
            print(element)
            reslist.append(element)
    print(reslist)









num=int(input("Hi user, please give a no: "))
a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
listTest(a,num)
