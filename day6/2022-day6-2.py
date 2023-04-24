#open input file
file = open('input.txt', 'r')

#inputs
for line in file.readlines():
    #create 14 character buffer
    buffer = []
    bufferMax = 14
    indexFound = True

    #create marker variable
    marker = 0

    #ensure buffer is at 14 characters
    for item in line:
        buffer.append(item)
        marker += 1
        if (len(buffer) == bufferMax):
            for x in buffer:
                if buffer.count(x) > 1:
                    indexFound = False
                    break
            if indexFound == True:
                #return index and break out of loop
                print(marker)
                break
            #clean up for next loop
            indexFound = True
            buffer.pop(0)
