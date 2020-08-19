# table1: 1500, 3人
# table2: 2000, 3人
# table3: 3647, 4人


def warikan(amount, number_of_people):
    return f'一人あたり:{amount}円, 端数:{amount % number_of_people}円'


print(warikan(1500, 3))
print(warikan(2000, 3))
print(warikan(3647, 4))
