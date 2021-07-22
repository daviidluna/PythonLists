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
