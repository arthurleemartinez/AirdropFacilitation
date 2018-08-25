import random
exceed_smart_contract:str = '0x1eae15d9f4fa16f5278d02d2f8bda8b0dcd31f71'
#max_drop_per_person = int(input('What is the maximum amount of Exceed are we are dropping per person here?'))
x = []
y = []
for i in range(100):
    y = random.random() * 1200
    zz = round(y, 8)
    x.append(zz)
    whitespace_containing_list = x
    final_list_values = str(whitespace_containing_list).replace(" ", "")
print('Copy and Paste this into the "ERC20 Address" box: {}'.format(exceed_smart_contract))
print("Printing out comma separated list...")
print(final_list_values)
