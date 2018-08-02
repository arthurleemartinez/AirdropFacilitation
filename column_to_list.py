# initialize user interface
from typing import List, Any

print("This program will help you perform your airdrop.")
user_column: str = input("Please enter/paste your entire column of ethereum addresses.")
user_column = user_column[:75]
list_column = []
# every ethereum address is equal to 42 char
n = 42
# iterate in list and separate it by ethereum address
def get_user_split_column():
    a = []
    """
    :rtype: list
    """
    for i in range(0, len(user_column), n):
        assert isinstance(Any, list)
        usc: List[ Any] = (user_column[i:i + n], n)
        a: List[Any] = usc
    return a

user_split_column = get_user_split_column()
print(get_user_split_column())
