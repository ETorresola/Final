def credit_card_penalty(late_days, credit_card_balance):
    if late_days<15:
        return .05*credit_card_balance

    elif late_days<=30 and late_days>=15:
        return .10*credit_card_balance

    elif late_days<=60 and late_days >30:
        return .15*credit_card_balance

    else:
        return .2*credit_card_balance

print "penalty 1: ", credit_card_penalty(18,15000)
print "penalty 2: ", credit_card_penalty(31,7000)
print "penalty 3: ", credit_card_penalty(70,300)
print "penalty 4: ", credit_card_penalty(3,1000)