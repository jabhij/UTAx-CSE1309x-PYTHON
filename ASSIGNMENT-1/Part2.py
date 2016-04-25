# Function Definition
def reamining_loan(principal, annual_interest_rate, duration , number_of_payments):
    # Handling Divide by Zero error
    if annual_interest_rate == 0:
        return principal * (1 - principal/duration*12)
    # Values and Parameters
    r = annual_interest_rate / 100 / 12
    n = duration * 12
    reamining_loan_bal = principal * (1+r)**n - (1+r)**principal / (1+r)**n - 1
    return reamining_loan_bal
