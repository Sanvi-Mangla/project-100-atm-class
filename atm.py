class Atm(object):
    def __init__(self, cardNumber, PinNumber):
        self.cardNumber=cardNumber
        self.PinNumber=PinNumber

    def CashWithdrawal(self):
        print("Cash Witdrawaled")

    def BalanceEnquiry(self):
        print("Balance left is 5,30,000")

Atm1= Atm("2478358905321864","4783")
Atm2= Atm("5378256783542895","5924")

print(Atm1.cardNumber)
print(Atm2.PinNumber)
        