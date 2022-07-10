from .taxCalculator import calculate_tax_percent
from quote import get_quote
from calculation import Calculation


def get_calculation(initial_value, interest_rate, investment_term):
    quote = float(get_quote())

    tax_rate = calculate_tax_percent(investment_term)

    annual_gross_percent = round(((((100 + quote) / 100) * ((100 + interest_rate) / 100)) - 1) * 100, 2)

    final_gross_total = round((initial_value * ((100 + annual_gross_percent) / 100) ** investment_term), 2)

    tax_fee = round((final_gross_total - initial_value) * (tax_rate / 100), 2)

    final_net_value = round((final_gross_total - tax_fee), 2)

    net_income = round((final_net_value - initial_value), 2)

    income_percentage = round(((final_net_value - initial_value) / initial_value) * 100, 2)

    return Calculation(annual_gross_percent, final_gross_total, tax_fee, final_net_value, net_income, income_percentage,
                       tax_rate, quote)
