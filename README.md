# Mortes por Covid-19 no Brasil por região

## O projeto:

Analisar com a visualização de corrida de barras (Bar Chart Race) os números de mortes por região brasileira no período de 2020 a 2023.

### Contexto:

O período da pandemia no Brasil talvez tenha sido um dos mais ricos para a análise de dados. A área da Saúde é, por suas características, pródiga em fornecer dados e informações sobre diversos temas. E a pandemia não fugiu à regra.

Leve-se em conta, também, que o Brasil foi um dos poucos países no mundo a demorar para criar regras, buscar referências e, em várias ocasiões, negar o perigo que a Covid-19 traria à sua população. O então governo federal só começou a tomar providências quando os números se tornaram assustadores pela frequência e quantidade.

A imprensa noticiou diariamente rankings de casos e mortes pelo país inteiro. Algumas regiões sempre estiveram na frente devido a fatores como densidades demográficas e características urbanísticas. Soma-se ao cenário casos de mal uso do dinheiro público, corrupção e desperdício.

Como consequência, hábitos foram modificados, outros, adquiridos, até que os órgãos públicos iniciassem a campanha de vacinação - o Brasil foi um dos últimos a iniciar este processo.

## Objetivo:

Utilizando os dados do portal [**Coronavírus BRASIL**](https://covid.saude.gov.br/) cuja atualização quando da produção deste projeto foi 26/04/2023, produziu-se um modelo de visualização mais dinâmico, no caso, uma corrida de barras (Bar Chart Race). Os casos foram agrupados por região do Brasil (Norte, Nordeste, Sudeste, Sul e Centro-Oeste).

O resultado permite demonstrar que áreas mais densamente povoadas são mais suscetíveis ao maior número de casos (contaminação e mortes).

## Estrutura do repositório:

* **data:** arquivos **.csv** baixados no site da Secom;
* **img:** capturas de tela e gráficos do projeto;
* **code:** estrutura dos códigos para **Jupyter Notebook** (.ipynb) e **VSCode** (.py);
* **english version:** a translate of **reademe.md** (.pdf).

## Linguagem utilizada:

* **Python**

## Bibliotecas:

* **Pandas**
* **Módulo Bar Chart Race**

# Arquivos adicionais:

* **ffmpeg** - que deve ser baixado e instalado no computador para gerar o gráfico em **.mp4**
* Baixar o ffmpeg (windows): [link](https://www.gyan.dev/ffmpeg/builds/)
**Para outros OSs, acessar o [link](https://ffmpeg.org/)
* Instalar: [link](https://www.youtube.com/watch?v=qSlxv68Xpkw&list=PLOraXz1HoXBZHpMYytIjzm0eMoDyfMLZp&index=38)

## Metodologia:

Após baixar os dados do Portal CORONAVÍRUS BRASIL, verificou-se que os dados em formato **.csv** estavam divididos por semestre. Assim, um arquivo "HIST_PAINEL_COVIDBR_2020_Parte1_26abr2023.csv" e assim por diante. Para facilitar, todos foram renomeados para "COVIDBR_2020_Parte1.csv", bem como os demais.

Assim, ficou mais fácil para tratar os dados utilizando **Pandas** para visualizar o dataset, raspar os dados para os valores necessários, concatenar os datasets em apenas um dataset, filtrar por região, somar e agrupar os valores e, finalmente, pivotar o dataset utilizando a coluna "data" como index (referência para criar o Bar Chart Race).

<img src="/img/dataset.png">

###
Em seguida, após a conferência de que as informações estavam da forma desejada, configurou-se o código do Bar Chart Race e, finalmente, gerar a animação em **.mp4** (abaixo, captura de tela do resultado).

<img src="/img/captura.png">

###
## Considerações:

Aqui, vale alguns comentários sobre o resultado final. Verificou-se que, sem surpresas, a Região Sudeste foi a mais afetada pelos efeitos do Coronavírus - tanto pela densidade demográfica quanto pelo fato urbanístico (principalmente em periferias, famílias inteiras vivem em áreas menores, o que aumenta o contato e a contaminação pela doença).

Por outro lado, a Região Nordeste aparece em segundo. Isso pode ser creditado à insuficiência de infra-estrutura na área da saúde (postos, hospitais e condições de receber e tratar pacientes contaminados).

Bem perto, a Região Sul. Neste caso, durante o acompanhamento dos números de vacinação, verificou-se que foi a região mais "negacionista" em relação à pandemia desde sua decretação pela OMS. Campanhas contra a vacinação e posicionamentos políticos de governadores e prefeitos ampliaram os efeitos.

Norte e Centro-Oeste os últimos, mais em função da baixa densidade demográfica. Com as populações mais dispersas, os níveis de contaminação e morte foram menores.

Um evento que vale destacar na Região Norte foi o que ficou conhecido como "crise do oxigênio", em que os governos estadual e federal não deram a atenção necessária para a falta de oxigênio nos hospitais, tão necessário para o tratamento dos contaminados por Covid-19.
