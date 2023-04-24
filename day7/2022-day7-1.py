def get_directory(file):
    #create base directory
    directory = {"/root": 0}
    current = ""
    for line in file.readlines():
        #take user input.  Split to get each command separately.
        line = line.split()
        if(line[0]) == '$':
            #it is user input
            if line[1] == "cd":
                if line[2] == "..":
                    #go up one path level
                    current = current[:current.rindex("/")]
                elif line[2] == "/":
                    #set path level back to root
                    current = "/root"
                else:
                    #create new dictionary entry and initialize size to 0
                    current = current + "/" + line[2]
                    directory[current] = 0
            elif line[1] == "ls":
                #run list directory, but no change in sizes for dictionary
                pass
        else:
            if line[0] != "dir":
                temp = current
                while temp != "":
                    #add to dictionary directory total
                    directory[temp] += int(line[0])
                    temp = temp[:temp.rindex("/")]
    return directory

def solve_part_1(directory):
    total = 0
    for x in directory.items():
        #only get the size, not the key
        x = x[1]
        if x < 100000:
            total += x
    print(total)

#Solve problem
input_file = open('input.txt', 'r')
directory = get_directory(input_file)
solve_part_1(directory)
