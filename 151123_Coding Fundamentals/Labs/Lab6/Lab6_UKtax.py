'''
In this lab you'll write a function for calculating personal tax in UK.
'''

## Rules for personal tax in UK
## Personal allowance:		£11,850	 
## 0 to 34,500 			taxed at 20%		
## 34,501 to 150,000 		taxed at 40%		
## Over 150,000 			taxed at 45%		


def getIncomeTax(salary):


    tax_amount=None

    salary_after_allowance=salary-11_850

    if salary_after_allowance>150_000:
        tax_pct=0.45
        tax_amount=salary_after_allowance*tax_pct

    elif salary_after_allowance>34_500:
        tax_pct=0.40
        tax_amount=salary_after_allowance*tax_pct
    
    else:
        tax_pct=0.20
        tax_amount=salary_after_allowance*tax_pct

    print(f'Your salary is £{salary:,}')
    print(f'Your salary after allowance is £{salary_after_allowance:,}')
    print(f'Your tax percentage is {tax_pct*100:.0f}%')
    print(f'Your tax amount is £{tax_amount:,}')

    return tax_amount


if __name__ == '__main__':

    salary=int(input("Please enter your salary as an integer without commas: "))
    tax_amount=getIncomeTax(salary)


