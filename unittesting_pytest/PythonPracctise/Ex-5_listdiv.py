def checkListDiv(list1,list2):
    result=[]
    for num in b:
        if num in a and num not in result:
            result.append(num)
    return result


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(checkListDiv(a,b))
