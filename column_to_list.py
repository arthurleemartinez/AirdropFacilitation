# initialize user interface
from typing import List, Any

print("This program will help you perform your airdrop.")
user_column: str = input("Please enter/paste your entire column of ethereum addresses.")
list_column = []
# every ethereum address is equal to 42 char
n = 42
# iterate in list and separate it by ethereum address
def get_user_split_column():
    for i in range(0, len(user_column), n):
        usc: List[ Any] = (user_column[i:i + n], n)
        a: List[Any] = usc
    return a
user_split_column = get_user_split_column()
def remove_0x():
    address_removed_prefix = user_split_column[2:-2]		  
    return address_removed_prefix
rem_0x = remove_0x()
