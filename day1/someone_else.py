file = open('input.txt', 'r')

inventory = 0
inventory_list = []
for line in file.readlines():
    if line == "\n":
        inventory_list.append(inventory)
        inventory = 0
    else:
        inventory += int(line)
sum_top_inventories = sum(sorted(inventory_list)[-3:])  # Sort the list and sum last 3 entries (the highest ones)
print("Task 2 result: " + str(sum_top_inventories))
