def split_bill(amount, number_of_people):
    amount = amount // number_of_people
    return f'一人あたり:{amount}円, 端数:{amount % number_of_people}円'
