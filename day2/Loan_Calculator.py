print("Welcome to the Loan Calculator!")
Loan_Amount=float(input("Enter the Loan Amount: "))
Interest_Rate=float(input("Enter your Interest Rate:(Dont include the percentage sign) "))
Tenure=int(input("Enter the no of years you want to pay off the loan:"))
Monthly_Interest_Rate=Interest_Rate/1200
Tenure_in_months=Tenure*12
Monthly_EMI=Loan_Amount*Monthly_Interest_Rate*(((1+Monthly_Interest_Rate)**Tenure_in_months)/(((1+Monthly_Interest_Rate)**Tenure_in_months)-1))
Total_Amount_Repayable=Monthly_EMI*Tenure_in_months
Total_Interest_Payable=Total_Amount_Repayable-Loan_Amount
print("Monthly EMI IS: ",round(Monthly_EMI,2))
print("Total Amount Repayable IS: ",round(Total_Amount_Repayable,2))
print("Total Interest Payable IS: ",round(Total_Interest_Payable, 2))