#equity delivery calculator
def equity_delivery():
    bp=float(input("Enter the buying price: "))
    sp=float(input("Enter the selling price: "))
    q=int(input("Enter the quantity: "))
    stock_exchange=input("Enter your exchange: ") #enter b for BSE & n for NSE
    turnover=(bp*q)+(sp*q)
    brokerage=20
    STT=(turnover)*0.001
    stamp_duty=(bp*q)*0.00015
    sebi=(10/10000000)*turnover
    if stock_exchange==n:
      exchange_charges=0.0000297*(sp*q)
    else:
      exchange_charges=0.0000375*(sp*q)
    GST=(brokerage+sebi+STT+exchange_charges)*1.18
    profit=(sp*q)-(bp*q)
    charges=brokerage+STT+stamp_duty+sebi+GST+exchange_charges
    print("Your total charges are",round(charges,2))
    print("Your profit is ",round(profit,2))
    print("Your net profit is",round(profit-charges,2))
