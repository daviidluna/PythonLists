mine = ['a promised', 'land', 'hehe']
print(mine)

yes = ['cabbage', 'eggplant', 'watermelon']
if 'watermelon' in yes:
    print('yes, watermelon is present in the list \'yes\'')

wait_list = ['amanda', 'fiber', 'oliver']
if 'oliver' in wait_list:
    print('yes he is on the wait list')

# Accessing list items
one = ['first series', 'second series', 'third']
print(one[2])
one_ = one[1:2]
print(one_)

two = ['fifty', 'shades', 'of grey', 'is', 'cool', 'yes']
print(two[:4])  # By leaving out the start value, the range will start at the first item
print(two[3:])  # By leaving out the end value, the range will go on to the end of the list

water = ['cool water', 'lukewarm', 'cold', 'hot']
print(water[:3])
print(water[2:])

comp = ['red one', 'blue one', 'grey oone', 'pink', 'food', 'yes']
print(comp[-5:-2])

list_of_food = ['chips', 'soda', 'candy', 'potatoes', 'eggplant', 'banana']
print(list_of_food[3:-1])
print(list_of_food[-6:-3])

list_of_students = ['mia', 'lial', 'ria', 'code', 'yep', 'yurpa']
if 'yurpa' in list_of_students:
    print('yes yurpa is there')

# Changing list items
this_list = ['iphone', 'android', 'nokia', 'sprint']
this_list[3] = 'galactic'
print(this_list)
