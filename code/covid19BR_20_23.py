# Importacao das bibliotecas

import pandas as pd
import bar_chart_race as bcr

# Eliminar os avisos
import warnings
warnings.filterwarnings('ignore')

# Leitura dos datasets baixados do portal oficial de dados da Covid-19 no Brasil - Ministerio da Saude
covidbr2020 = pd.read_csv(r'covidbr_2020.csv', on_bad_lines='skip', sep=',', encoding='latin-1')
covidbr2021 = pd.read_csv(r'covidbr_2021.csv', on_bad_lines='skip', sep=',', encoding='latin-1')
covidbr2022 = pd.read_csv(r'covidbr_2022.csv', on_bad_lines='skip', sep=',', encoding='latin-1')
covidbr2023 = pd.read_csv(r'covidbr_2023.csv', on_bad_lines='skip', sep=',', encoding='latin-1')

# Concatenar os varios datasets para apenas um
df_covidbr_20_23 = pd.concat([covidbr2020, covidbr2021, covidbr2022, covidbr2023], axis=0, ignore_index=True)

# Formatar a data para modo Datetime
df_covidbr_20_23['data'] = df_covidbr_20_23['data'].astype('datetime64[ns]')

# Eliminar as linhas com dados nulos ou inconsistentes
df_covidbr_20_23.dropna(subset=['municipio'], inplace=True)

# Agrupamento e soma dos valores conforme a divisão de regiao do Brasil
df_grouped = df_covidbr_20_23.groupby(['regiao', 'data'])['obitosAcumulado'].sum().reset_index()

# Pivotar o dataset para que a data seja a primeira coluna
df_covid_bcr = df_grouped.pivot_table(index='data', columns='regiao', values='obitosAcumulado')

# Reorganizar as colunas para corresponder a ordem original
df_covid_bcr = df_covid_bcr[df_grouped['regiao'].unique()]
print(df_covid_bcr)

# Plotando o grafico de barras pelo Bar Chart Race
bcr.bar_chart_race(
    df=df_covid_bcr,
    filename='covidbr_20_232.mp4',
    orientation='h',
    sort='desc',
    n_bars=5,
    fixed_order=False,
    fixed_max=True,
    steps_per_period=5,
    interpolate_period=False,
    label_bars=True,
    bar_size=.70,
    period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
    period_fmt='%d %m, %Y',
    period_summary_func=lambda v, r: {'x': .99, 'y': .18,
                                      's': f'Total: {v.nlargest(6).sum():,.0f}',
                                      'ha': 'right', 'size': 8, 'family': 'Arial'},
    perpendicular_bar_func=None,
    period_length=70,
    figsize=(5, 3),
    dpi=144,
    cmap='Set1',
    title='Mortes por COVID-19 por região',
    title_size=14,
    bar_label_size=7,
    tick_label_size=7,
    shared_fontdict={'family': 'Arial', 'color': '.1'},
    scale='linear',
    writer=None,
    fig=None,
    bar_kwargs={'alpha': .7},
    filter_column_colors=False)
