money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

money_capital += salary #решение 1-м способом
while money_capital >= 0:
    #money_capital = money_capital - (spend - salary) #решение 2-м способом
    money_capital = money_capital - spend #решение 1-м способом
    month += 1
    spend = spend * (1+increase) ** month

print(month)
