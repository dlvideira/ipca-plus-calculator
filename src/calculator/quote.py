import requests
from datetime import date
from dateutil.relativedelta import relativedelta

base_endpoint = 'https://servicodados.ibge.gov.br/api/v3/agregados/{id}/periodos/{period}/variaveis/{variation}?localidades=N1[all]'

id = '1737'
period = (date.today() + relativedelta(months=-1)).strftime("%Y%m")
variation = '2265'


def get_quote():
    search_endpoint = base_endpoint \
        .replace("{id}", id) \
        .replace('{period}', period) \
        .replace('{variation}', variation)
    response = requests.get(search_endpoint).json()

    return next(iter(response))['resultados'][0]['series'][0]['serie'][period]
