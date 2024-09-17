# Default column name
INDEX = 'index'
COUNTS = 'counts'
EQUIPAMENTO = 'equipamento'
ENDERECO = 'endereco'
TIPO_POSTO = 'tipo_posto'
ID_TIPO_POSTO = 'id_tipo_posto'
ID_DISTRITO = 'id_distrito'
DISTRITO = 'distrito'
ID_CRS = 'id_crs'
CRS = 'crs'
DATA_HORA = 'data_hora'
INDICE_FILA = 'indice_fila'
STATUS_FILA = 'status_fila'
CORONAVAC = 'coronavac'
ASTRAZENECA = 'astrazeneca'
PFIZER = 'pfizer'
INTERCAMBIALIDADE = 'intercambialidade'
JANSSEN = 'janssen'
INFLUENZA = 'influenza'
PFIZER_PED = 'pfizer_ped'
CORONA_PED = 'corona_ped'
PFIZER_BABY = 'pfizer_baby'
PFIZER_BIVALENTE = 'pfizer_bivalente'
DENGUE = 'dengue'
C19_MONO_XBB = 'c19_mono_xbb'
COVID19_MENOR_12 = 'covid19_menor_12'
COVID19_MAIOR_12 = 'covid19_maior_12'
ID_TB_UNIDADES = 'id_tb_unidades'

DEFAULT_COLUMNS = [
    EQUIPAMENTO,
    ENDERECO,
    TIPO_POSTO,
    ID_TIPO_POSTO,
    ID_DISTRITO,
    DISTRITO,
    ID_CRS,
    CRS,
    DATA_HORA,
    INDICE_FILA,
    STATUS_FILA,
    CORONAVAC,
    ASTRAZENECA,
    PFIZER,
    INTERCAMBIALIDADE,
    JANSSEN,
    INFLUENZA,
    PFIZER_PED,
    CORONA_PED,
    PFIZER_BABY,
    PFIZER_BIVALENTE,
    DENGUE,
    C19_MONO_XBB,
    COVID19_MENOR_12,
    COVID19_MAIOR_12,
    ID_TB_UNIDADES,
]

UNSED_COLUMNS = [
    TIPO_POSTO,
    ID_TIPO_POSTO,
    ID_DISTRITO,
    ID_CRS,
    INDICE_FILA,
    ID_TB_UNIDADES,
]

NUMERIC_COLUMNS = [
    ID_TIPO_POSTO,
    ID_DISTRITO,
    ID_CRS,
    INDICE_FILA,
    ID_TB_UNIDADES
]

BOOLEAN_COLUMNS = [
    CORONAVAC,
    ASTRAZENECA,
    PFIZER,
    INTERCAMBIALIDADE,
    JANSSEN,
    INFLUENZA,
    PFIZER_PED,
    CORONA_PED,
    PFIZER_BABY,
    PFIZER_BIVALENTE,
    DENGUE,
    C19_MONO_XBB,
    COVID19_MENOR_12,
    COVID19_MAIOR_12
]

VACCINES_COLUMNS = BOOLEAN_COLUMNS