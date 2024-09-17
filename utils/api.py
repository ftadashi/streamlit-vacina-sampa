import time
import requests

from utils.log import debug, error, critical

base_url = 'https://deolhonafila.prefeitura.sp.gov.br'
url = base_url + '/processadores/dados.php'
header = {
    'Referer': base_url,
    'Origin': base_url,
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'trailers'
}
payload = {
    'dados': 'dados'
}

def api_call():
    start = time.time()
    response = requests.post(url, data=payload, verify=False)
    response_json = response.json()
    end = time.time()
    debug('Time spend to load data ' + str(end - start))
    return response_json
