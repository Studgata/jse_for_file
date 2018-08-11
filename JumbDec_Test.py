import random
import Jumbling_Char


def RevJumblingBlock(number,randno):
    del number[-14:]
    print('\n')
    print('Salt removed: ', ''.join(number))
    print('\n')

    if (randno%2==0):
        number = ''.join(reversed(number))
        print('Original Jumbled String: ',number)
    else:
        number = ''.join(number)
        print('Original Jumbled String: ', number)

    num = len(number)-randno

    numlist=list(number)
    fix=len(numlist)
    #print('Length of array: ',fix)

    print('\n')
    numlen=1
    #print (numlen)
    i=randno-1
    while(numlen<=randno):
        j=0
        j=(fix%numlen)
        #print ("Swapping positions ",i,",",j)
        numlist[i],numlist[j]=numlist[j],numlist[i]
        numlen=numlen+1
        i=i-1
        #print(numlist)
    cv=''.join(numlist)
    print('Decrypted string: ',cv)
    print('\n')
    x=''
    for i in range(0,num):
        x=x+numlist[i]
    print("Recovered Line:",x )
    print('***********************************************************************************************************')
    print('\n')
    return cv


    
