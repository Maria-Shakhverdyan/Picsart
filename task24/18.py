def compound_interest(principal, rate, time, n):
    return principal * (1 + rate / n) ** (n * time)

def loan_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 12
    payments = years * 12
    if monthly_rate == 0:
        return principal / payments
    return principal * monthly_rate * (1 + monthly_rate) ** payments / ((1 + monthly_rate) ** payments - 1)

def investment_return(initial_value, final_value):
    return ((final_value - initial_value) / initial_value) * 100

fin_oper = {
    'compound_interest': compound_interest,
    'loan_payment': loan_payment,
    'investment_return': investment_return
}

def financial_calculator(operation, **kwargs):
    if operation not in fin_oper:
        raise ValueError("Chka senc ban")
    finance_func = fin_oper[operation]

    try:
        result = finance_func(**kwargs)
        return result
    except TypeError as e:
        raise ValueError(f"Invalid arguments for {operation}: {e}")


try:
    ci = financial_calculator(
        'compound_interest', 
        principal=1000, 
        rate=0.05, 
        time=5, 
        n=4
    )
    print(f"The compound interest is: {ci:.2f}")

    lp = financial_calculator(
        'loan_payment', 
        principal=50000, 
        annual_rate=0.04, 
        years=15
    )
    print(f"The loan payment is: {lp:.2f}")

    ir = financial_calculator(
        'investment_return', 
        initial_value=1000, 
        final_value=2000
    )
    print(f"The investment return is: {ir:.2f}%")

except ValueError as e:
    print(e)