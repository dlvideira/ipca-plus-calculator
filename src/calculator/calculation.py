class Calculation:
    def __init__(self, annual_gross_percent, final_gross_total, tax_fee, final_net_value, net_income,
                 income_percentage, tax_rate, quote):
        self.quote = quote
        self.tax_rate = tax_rate
        self.income_percentage = income_percentage
        self.net_income = net_income
        self.final_net_value = final_net_value
        self.tax_fee = tax_fee
        self.final_gross_total = final_gross_total
        self.annual_gross_percent = annual_gross_percent
