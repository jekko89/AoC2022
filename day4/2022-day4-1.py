#open input file
file = open('input.txt', 'r')

#find overlaps in IDs for section assignments
#how many assignment pairs does one range fully contain the other?
overlap = 0
for line in file.readlines():
    counter = 0
    line = line.strip()
    sections = line.split(",")
    elf1 = []
    elf2 = []
    for x in sections:
        ids = x.split("-")
        #add all sections for appropriate elf
        for y in range(int(ids[0]), int(ids[1])+1):
            if counter == 0:
                elf1.append(y)
            if counter == 1:
                elf2.append(y)
        if counter == 0:
            counter += 1
    #inputs finished, now compare sets for overlap
    if(set(elf1) <= set(elf2)) | (set(elf2) <= set(elf1)):
        overlap += 1

print(overlap)
