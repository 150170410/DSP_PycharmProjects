def checklist(number):
    x=range(1,50)
    res=[]
    for element in x:
        if(element%number==0):
            res.append(element)
    return res


num=int(input("PLease provide a number: "))
print(checklist(num))


