# Function Definition
def get_loan(principal, annual_interest_rate, duration):
    if annual_interest_rate == 0:
        return principal / duration * 12
    # Values and Parameters
    r = annual_interest_rate / 100 / 12
    n = duration * 12
    monthlypayment = principal * r * (1 + r) ** n / (1 + r) ** n - 1
    return monthlypayment
