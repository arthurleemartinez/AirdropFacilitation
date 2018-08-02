print("This program will help you perform your airdrop.")
user_column = input("Please enter/paste a column of ethereum addresses.")
user_column = user_column[:4200]
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
        assert isinstance(object, list)
        usc = (user_column[i:i + n], n)
        a = usc
    return a


user_split_column = get_user_split_column()
print(get_user_split_column())
