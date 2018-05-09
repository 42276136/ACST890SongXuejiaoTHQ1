#compute the income limits and income tax rates
limit_1 = 18200
limit_2 = 37000
limit_3 = 87000
limit_4 = 180000

rate_1 = 0
rate_2 = 0.190
rate_3 = 0.325
rate_4 = 0.370
rate_5 = 0.450

# read the gross income from the user
income = float(input("Enter the gross income:"))

# compute the amount of tax payable and after-tax income
if income < limit_1:
  tax = rate_1 * income
  aftertax_income = income - tax
elif income < limit_2:
  tax = rate_2 * (income - limit_1)
  aftertax_income = income - tax
elif income < limit_3:
  tax = 3572 + rate_3 * (income - limit_2)
  aftertax_income = income - tax
elif income < limit_4:
  tax = 19822 + rate_4 * (income - limit_3)
  aftertax_income = income - tax
else:
  tax = 54532 + rate_5 * (income - limit_4)
  aftertax_income = income - tax

print("on an income of $" + format(income, ",.2f"),"the income tax payable is $" + format(tax, ",.2f") + "his or her after-tax income is $" + format(aftertax_income, ",.2f") +  ".")

~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
~                                                                                                                                                                                                           
                                                                                                                                                                                          1,1           All
