import pandas as pd

from utils.columns import DATA_HORA, UNSED_COLUMNS, NUMERIC_COLUMNS, BOOLEAN_COLUMNS

def convert_data(response_json):
    dataframe = parse_data(response_json)
    dataframe = convert_columns_types(dataframe)
    dataframe = cleanup_columns(dataframe)
    #debug(dataframe.info())
    return dataframe

def parse_data(response_json):
    return pd.DataFrame.from_dict(response_json)

def cleanup_columns(dataframe):
    # remoção de colunas desnecessárias
    return dataframe.drop(UNSED_COLUMNS, axis=1)
    
def convert_columns_types(dataframe):
    # conversão de tipos de dados numericos
    for column in NUMERIC_COLUMNS:
        dataframe[column] = pd.to_numeric(dataframe[column])
    # conversão de tipos de data/hora
    dataframe[DATA_HORA] = pd.to_datetime(dataframe[DATA_HORA], format='%Y-%m-%d %H:%M:%S')
    # conversão de tipos booleanos
    for column in BOOLEAN_COLUMNS:
        dataframe[column] = dataframe[column].astype(int).astype('bool')
    return dataframe

def filter_data(dataframe, search, district, region, queue_status):
    q = '''
    ( `equipamento`.str.contains(@search, case=False) or \
    `endereco`.str.contains(@search, case=False) ) and \
    `distrito` in @district and \
    `crs` in @region and \
    `status_fila` in @queue_status \
    '''
    return dataframe.query(q, engine='python')