def listComprehension(list1):
    resultlist=[element for element in list1 if element%2==0 ]
    #for element in list1:
     #   if(element%2==0):
      #      resultlist.append(element)
    print(resultlist)



a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100,200]
listComprehension(a)
