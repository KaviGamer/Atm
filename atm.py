class ATM(object):
    def __init__(self):
        self.card_number = input("CARD NUMBER > ")
        self.pin_number = input("PIN NUMBER > ")

    def cashWithdrawal(self):
        removeCash = input("How much money do you want to withdraw from your card? > ")
        print("Widthdrawn ",removeCash," ruppees from your card")



card_details = ATM()
card_details.cashWithdrawal()