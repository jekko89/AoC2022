input_file = open('input.txt', 'r')
#take input as instructions
directions = input_file.readlines()

#run instructions
headX = 0
headY = 0
headHistory = [[0,0]]
tailX = 0
tailY = 0
tailHistory = [[0,0]]
for line in directions:
    #process input
    temp = line.split()
    direction = temp[0]
    distance = int(temp[1])
    if direction == 'U':
        for x in range(0, distance):
            #move head
            headY += 1
            
            #check if tail needs to move
            tempDistanceX = headX - tailX
            tempDistanceY = headY - tailY

            #if distance is 2 update tail
            if tempDistanceY > 1 or tempDistanceY < -1:
                tailY += 1
                #if tail moved, ensure it's matching head's last X coordinate
                if tempDistanceX != 0:
                    tailX = headX

            #update history for tail and head
            if [headX, headY] in headHistory:
                pass
            else:
                headHistory.append([headX, headY])
            if[tailX,tailY] in tailHistory:
                pass
            else:
                tailHistory.append([tailX,tailY])

    elif direction == 'D':
        for x in range(0, distance):
            #move head
            headY -= 1
            
            #check if tail needs to move
            tempDistanceX = headX - tailX
            tempDistanceY = headY - tailY
            #if distance is 2 update tail
            if tempDistanceY > 1 or tempDistanceY < -1:
                tailY -= 1
                #if tail moved, ensure it's matching head's last X coordinate
                if tempDistanceX != 0:
                    tailX = headX

            #update history for tail and head
            if [headX, headY] in headHistory:
                pass
            else:
                headHistory.append([headX, headY])
            if[tailX,tailY] in tailHistory:
                pass
            else:
                tailHistory.append([tailX,tailY])

    elif direction == 'L':
        for x in range(0, distance):
            #move head
            headX -= 1
            
            #check if tail needs to move
            tempDistanceY = headY - tailY
            tempDistanceX = headX - tailX
            
            #if distance is 2 update tail
            if tempDistanceX > 1 or tempDistanceX < -1:
                tailX -= 1
                #if tail moved, ensure it's matching head's last Y coordinate
                if tempDistanceY != 0:
                    tailY = headY

            #update history for tail and head
            if [headX, headY] in headHistory:
                pass
            else:
                headHistory.append([headX, headY])
            if[tailX,tailY] in tailHistory:
                pass
            else:
                tailHistory.append([tailX,tailY])

    elif direction == 'R':
        for x in range(0, distance):
            #move head
            headX += 1
            
            #check if tail needs to move
            tempDistanceY = headY - tailY
            tempDistanceX = headX - tailX

            #if distance is 2 update tail
            if tempDistanceX > 1 or tempDistanceX < -1:
                tailX += 1
                #if tail moved, ensure it's matching head's last Y coordinate
                if tempDistanceY != 0:
                    tailY = headY

            #update history for tail and head
            if [headX, headY] in headHistory:
                pass
            else:
                headHistory.append([headX, headY])
            if[tailX,tailY] in tailHistory:
                pass
            else:
                tailHistory.append([tailX,tailY])


#print answer
print(len(tailHistory))
