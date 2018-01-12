def revString(indata):
    return indata[::-1]

def revSentence(strdata):
    mydata=strdata.split()
    result=''
    for element in mydata:
        result+=' '+revString(element)
    return result


print (revSentence('My name is Anthony'))
