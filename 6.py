def primenumber():
    num = int(input("Enter the number: "))
    check = 0
    for i in range(2, num):
        if (num % i) == 0:
            check = 1
            break

    if check == 1:
        print( num , "is not a prime number")
    else:
        print( num , "is a prime number" )
primenumber()

def firsttwenty():
    myList = []
    for n in range(2,72):
        for i in range(2,n):
            if(n%i==0):
                break
        else:
            myList.append(n)
    print (myList)
    rangeList = len(myList)
    
    def fakeprime(myList,rangeList):
        fakeList = []
        for i in range(0,rangeList-1):
            fakenumber = myList[i] * myList[i+1]
            fakeList.append(fakenumber)
        print(fakeList)
    return fakeprime(myList,rangeList)

firsttwenty()


