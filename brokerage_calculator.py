#equity delivery calculator
bp=float(input("Enter the buying price: "))
sp=float(input("Enter the selling price: "))
q=int(input("Enter the quantity: "))
stock_exchange=input("Enter your exchange: ")
STT=((bp*q)+(sp*q))*0.001
stamp_duty=60
sebi=(10/10000000)*STT
exchange_charges=0.0000375*(sp*q)
GST=(sebi+STT)*1.18
profit=(sp*q)-(bp*q)
charges=STT+stamp_duty+sebi+GST+exchange_charges
print("Your total charges are",round(charges,2))
print("Your profit is ",round(profit,2))
print("Your net profit is",round(profit-charges,2))
