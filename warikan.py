def warikan(amount, number_of_people):
    amount = amount // number_of_people
    return f'一人あたり:{amount}円, 端数:{amount % number_of_people}円'


print(warikan(amount=1500, number_of_people=3))
print(warikan(amount=2000, number_of_people=3))
print(warikan(amount=3647, number_of_people=3))
