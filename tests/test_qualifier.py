# Import pathlib
from pathlib import Path

#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import 
from qualifier.utils.fileio import save_csv

# Import Filters
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size


"""
testing save_csv 
Note to checker: sorry I am stuck, please provide feedback on how to solve this.

def test_save_csv():
    save_status == True
    enter
    csvpath = fileio.save_csv(Path('./data/output/qualifying_loans.csv'))
"""    

#testing calculator, calling the monthly_debt_ratio function passing to values = .375
def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

#testing calculator, calling the loan to value function passing to values = .84
def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

"""
testing filters, passing values:
bank_data = to extract results from ./data/daily_rate_sheet.csv 
current_credit_score = user credit score: 750
debt = user total monthly debt: 1500
income = user total monthly income: 4000
loan = user's desired loan amount: 21000
home_value = user's home value: 250000

"""
def test_filters():
    bank_data = fileio.load_csv(Path('./data/daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84


