

# THE LOAN QUALIFIER CLI

This is a commmand line application that matches loans to users, and allows to save qualifying loan data to a csv file for shaing on a spreadsheet. 


---

## Technologies

This project is written in Python with the following packages:

* fire 

* questionary 

* pytest



---

## Installation Guide

Before running the application first install the following dependencies.

```python
  pip install fire
  pip install questionary
  pip install pytest
```
Clone to your local repo and run **app.py**

---

## Examples


>"...
*? Enter a file path to a rate-sheet (.csv): ./data/daily_rate_sheet.csv
*? What's your credit score? 750
? What's your current amount of monthly debt? 500
? What's your total monthly income? 10000
? What's your desired loan amount? 25000
? What's your home value? 1000000
The monthly debt to income ratio is 0.05
The loan to value ratio is 0.03.
Found 15 qualifying loans
? Do you want save this csv file Yes
? enter path myloanlist.csv"




---

## Usage

? When prompted for Enter a file path to a rate-sheet (.csv), 
    enter: "./data/daily_rate_sheet.csv"
? Enter credit score
? Enter total monthly debt
? Enter total current monthly income
? Enter desired loan amount
? Enter home value
? When prompted if you would love to select csv file? Select Y for Yes, N for No
? If yes, enter a path 
? If no, you will automatically exit the loan qualifier app


---

## Contributors

[Van Miller Sarcov Maquilan](https://www.linkedin.com/in/van-miller-sarcov-maquilan-20b472202/) 


---

## License

Feel free to add to this code, and use for your own project. :)
