from rich.console import Console
from rich.table import Table


def money_value(value):
    return 'R$ ' + str(value)


def percent(value):
    return str(value) + ' %'


def print_result(initial_value, interest_rate, investment_term, result):
    base_calc_table = Table(title="Dados base para cálculos IPCA+:")
    base_calc_table.add_column('Dado', style="cyan bold", no_wrap=True)
    base_calc_table.add_column('Valor', style="blue bold")

    base_calc_table.add_row('Valor Presente', money_value(initial_value))
    base_calc_table.add_row('Taxa de Rendimento', percent(interest_rate))
    base_calc_table.add_row('Tempo de Investimento', str(investment_term) + ' ano(s)')
    base_calc_table.add_row('IPCA (12 meses)', percent(result.quote))
    base_calc_table.add_row('Alíquota', percent(result.tax_rate))

    result_table = Table(title="Projeção de Resultados IPCA+:")
    result_table.add_column('Dado', style="cyan bold")
    result_table.add_column('Valor', style="green bold", justify='right')

    result_table.add_row('Rendimento Anual Bruto', percent(result.annual_gross_percent))
    result_table.add_row('Valor Futuro Bruto', money_value(result.final_gross_total))
    result_table.add_row('Imposto de Renda', money_value(result.tax_fee))
    result_table.add_row('Valor Futuro Líquido', money_value(result.final_net_value))
    result_table.add_row('Rendimento', money_value(result.net_income))
    result_table.add_row('Rendimento', percent(result.income_percentage))

    Console.print(Console(), base_calc_table, result_table)
