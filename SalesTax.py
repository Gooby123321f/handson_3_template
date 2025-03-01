salesTaxRate = 0.06

def salesTaxCalc(total):
    return total * salesTaxRate

def totalAfterTaxCalc(total):
    return salesTaxCalc(total) + total