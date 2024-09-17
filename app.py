import streamlit as st

from utils.api import api_call
from utils.data import convert_data, filter_data
from utils.log import info
from utils.columns import CRS, STATUS_FILA, STATUS_FILA, COUNTS, INDEX, VACCINES_COLUMNS

# Global configurations
st.set_page_config(layout= 'wide')
st.header(':material/vaccines: Vacina Sampa', divider='red')

@st.cache_data(ttl=60, max_entries=500)
def fetch_data():
    info('Fetch data')
    response_json = api_call()
    dataframe = convert_data(response_json)
    return dataframe

data = fetch_data()
st.toast(":rainbow[:material/api: Atualizando dados!]")

# Sidebar
st.sidebar.title(':material/search: Pesquisa')
with st.sidebar:
    search = st.text_input('Termo de busca', placeholder='Busca de equipamento e endereço')

st.sidebar.title(':material/filter_alt: Filtros')
with st.sidebar.expander('Região'):
    region_list = list(data[CRS].unique())
    region = st.multiselect('Selecione as regiões', region_list, region_list)
with st.sidebar.expander('Status da fila'):
    queue_status_list = list(data[STATUS_FILA].unique())
    queue_status = st.multiselect('Selecione o status da fila', queue_status_list, queue_status_list)
with st.sidebar.expander('Distrito'):
    district_list = list(data['distrito'].unique())
    district = st.multiselect('Selecione o distrito', district_list, district_list)

st.sidebar.title(':material/view_column: Colunas')
with st.sidebar.expander('Colunas'):
    columns_list = list(data.columns)
    columns = st.multiselect('Selecione as colunas', columns_list, columns_list)

# Filtered data
filtered_data = filter_data(data[columns], 
                            search=search,
                            district=district, 
                            region=region,
                            queue_status=queue_status)

# Metric section (data can be filtered)
with st.expander('Métricas gerais', icon=':material/score:', expanded=True):
    
    col1, col2, col3 = st.columns([2, 3, 3])

    # last update present on data
    with col1:
        st.subheader(':material/calendar_month: Data de atualização')
        st.metric('', filtered_data['data_hora'].max().strftime('%d/%m/%Y %H:%M:%S'))

    # Chart: count queues/status
    with col2:
        st.subheader(':material/hourglass_top: Status das filas')
        counts_status_fila = filtered_data[STATUS_FILA].value_counts().reset_index(name=COUNTS)
        counts_status_fila.sort_values(by=[COUNTS], ascending=False)
        st.bar_chart(counts_status_fila, 
                     x=STATUS_FILA, 
                     y=COUNTS, 
                     x_label='Quantidade',
                     y_label='Status da fila',
                     color=STATUS_FILA,
                     horizontal=True)

    # Chart: count vaccines available (> 0)
    with col3:
        st.subheader(':material/syringe: Unidades com vacinas')
        count_vaccines = filtered_data[(filtered_data[VACCINES_COLUMNS] == True)].count().reset_index(name=COUNTS)
        count_vaccines = count_vaccines[count_vaccines[COUNTS] != 0].sort_values(by=[COUNTS], ascending=False)
        st.bar_chart(count_vaccines, 
                x=INDEX, 
                y=COUNTS, 
                x_label='Quantidade de vacinas',
                y_label='Unidade',
                color=INDEX,
                horizontal=True)

# Table data filtered
with st.container():
    st.subheader(':material/database: Dados', divider='red')
    st.dataframe(filtered_data, use_container_width=True)
    st.markdown(f'A tabela possui **:red[{filtered_data.shape[0]}]** linhas e **:red[{filtered_data.shape[1]}]** colunas')
