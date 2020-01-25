def cal_expenses(exp):
    """
    :param exp:
    :return:
    """
    total = 0
    for i in exp:
        total = total+i
    return total


johns_expenses = [100, 200, 300]
sams_expenses = [400, 500, 100]

johns_total=cal_expenses(johns_expenses)
sams_total=cal_expenses(sams_expenses)

print("John's total expenses are :",johns_total)
print("Sam's total expenses are :",sams_total)