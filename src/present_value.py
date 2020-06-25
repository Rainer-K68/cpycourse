"""Calculate the present value for a list of cash flows.
"""

cashflows = [-100, -2, 3, 6, 8, 110]
rate = 0.03  # interest rate
q = 1 + rate # discount factor

present_value = 0
for (i, cf) in enumerate(cashflows):
    present_value += cf * q**(-i)

print('Present value for {} and interest rate {}:\n    pv = {}'.format(
    cashflows, rate, present_value))
