print("This program will help you perform your airdrop.")
user_column = input("Please enter/paste a column of ethereum addresses.")
user_column = user_column[:4200]
list_column = []
# every ethereum address is equal to 42 char
n = 42
allowance = '1000'
exceed = '0x1eAe15d9f4FA16f5278D02d2f8bDA8b0dcd31f71'


def get_allowance(str):
    return str


def get_contract_address(str):
    return 'Contract Address (Token): %s' % exceed


contract_address = get_contract_address()

# iterate in list and separate it by ethereum address


def get_user_split_column():
    a = []
    """
    :rtype: list
    """
    item in user_colum = character
    for characters in user_column:
        i = character
        assert isinstance(object, list)
        usc = (user_column[i:i + n], n)
        a = usc
    return a


def get_list_column():
    list_column = list_column.append(get_user_split_column())


user_split_column = get_user_split_column()


print(get_contract_address(exceed))
print(get_allowance('1000'))
print(get_user_split_column())
print(get_list_column())
