def fibonicci(num):
    if num<2:return num
    else:return fibonicci(num-1)+fibonicci(num-2)


inputnum=int(input('How many nos u want'))

for i in range(inputnum):
    print(fibonicci(i))
