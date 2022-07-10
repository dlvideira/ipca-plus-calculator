from calculator import get_calculation
from src.calculator import result_printer

initial_value = float(input('Valor inicial do investimento:').replace(',', '.'))
interest_rate = float(input('Taxa de juros do CDB:').replace(',', '.'))
investment_term = int(input('Tempo de investimento (anos):'))

result = get_calculation(initial_value, interest_rate, investment_term)

result_printer.print_result(initial_value, interest_rate, investment_term, result)
