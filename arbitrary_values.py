import random
max_drop_per_person = int(input('What is the maximum amount of Exceed are we are dropping per person here?'))
x = []
y = []
for i in range(100):
    y = random.random() * max_drop_per_person
    zz = round(y, 6)
    x.append(zz)
    whitespace_containing_list = x
    final_list_values = str(whitespace_containing_list).replace(" ", "")
print("Printing out comma separated list...")
print(final_list_values)
