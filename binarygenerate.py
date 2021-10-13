def dec_binary(p1: int, p2: int) -> str:
    for val in range(1, p1+1):
        #set the initial value
        mylist = []
        mystr = ""
        #while function to generate the binary in list
        while val != 0:
            mylist.append(val % 2)
            val = val // 2
        #append the binary list to the digit we want
        if len(mylist) != p2:
            for times in range(p2-len(mylist)):
                mylist.append(0)
        #reverse the binary list
        mylist.reverse()
        #print(mylist)  #print the list
        #covert the list to str
        for item in mylist:
            mystr = mystr + str(item)
        #print(mystr)
        #print("0"+mystr)  #if we want short binary
        print("1"+mystr)  #if we want long binary