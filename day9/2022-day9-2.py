#Day 9 - Part 2: https://adventofcode.com/2022/day/9
with open('input.txt', 'r') as file:
    input_file = file
    directions = input_file.readlines()

class rope:
    x=0
    y=0

ropeList = []
for item in range(0, 10):
    ropeList.append(rope())
tailHistory = [[0,0]]

def follow(child, parent):
    distanceX = parent.x - child.x
    distanceY = parent.y - child.y

    if distanceX == 2 and distanceY == 0:
        child.x += 1
    elif distanceX == -2 and distanceY == 0:
        child.x -= 1
    elif distanceY == 2 and distanceX == 0:
        child.y += 1
    elif distanceY == -2 and distanceX == 0:
        child.y -= 1

    elif distanceX == 2 and distanceY == 2:
        child.x += 1
        child.y += 1
    elif distanceX == 2 and distanceY == -2:
        child.x += 1
        child.y -= 1
    elif distanceX == -2 and distanceY == 2:
        child.x -= 1
        child.y += 1
    elif distanceX == -2 and distanceY == -2:
        child.x -= 1
        child.y -= 1

    elif distanceX == 2 and parent.y != child.y:
        child.x += 1
        child.y = parent.y
    elif distanceX == -2 and parent.y != child.y:
        child.x -= 1
        child.y = parent.y
    elif distanceY == 2 and parent.x != child.x:
        child.y += 1
        child.x = parent.x
    elif distanceY == -2 and parent.x != child.x:
        child.y -= 1
        child.x = parent.x

#process directions
for line in directions:
    #process input
    temp = line.split()
    direction = temp[0]
    distance = int(temp[1])
    if direction == 'U':
        for x in range(0, distance):
            #move head
            ropeList[0].y += 1
            
            #check if tails need to move
            for tail in range(1, 10):
                follow(ropeList[tail], ropeList[tail-1])

            #update history for final tail
            if[ropeList[9].x,ropeList[9].y] in tailHistory:
                pass
            else:
                tailHistory.append([ropeList[9].x,ropeList[9].y])

    elif direction == 'D':
        for x in range(0, distance):
            #move head
            ropeList[0].y -= 1
            
            #check if tails need to move
            for tail in range(1, 10):
                follow(ropeList[tail], ropeList[tail-1])

            #update history for final tail
            if[ropeList[9].x,ropeList[9].y] in tailHistory:
                pass
            else:
                tailHistory.append([ropeList[9].x,ropeList[9].y])

    elif direction == 'L':
        for x in range(0, distance):
            #move head
            ropeList[0].x -= 1
            
            #check if tails need to move
            for tail in range(1, 10):
                follow(ropeList[tail], ropeList[tail-1])

            #update history for final tail
            if[ropeList[9].x,ropeList[9].y] in tailHistory:
                pass
            else:
                tailHistory.append([ropeList[9].x,ropeList[9].y])

    elif direction == 'R':
        for x in range(0, distance):
            #move head
            ropeList[0].x += 1
            
            #check if tails need to move
            for tail in range(1, 10):
                follow(ropeList[tail], ropeList[tail-1])

            #update history for final tail
            if[ropeList[9].x,ropeList[9].y] in tailHistory:
                pass
            else:
                tailHistory.append([ropeList[9].x,ropeList[9].y])

#print answer
print(len(tailHistory))
