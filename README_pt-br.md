# 📊 Analisando o Impacto da Recessão nas Vendas de Automotores nos Estados Unidos

![Dashboard - Report 1: Recession Period Statistics](../dashboard/report_1_recession_period_stats.png)

**Categoria:** Visualização de Dados  
**Segmento de Atuação:** Vendas  
**Tecnologias:** `Pandas`, `Matplotlib`, `Seaborn`, `Folium`, `Plotly`, `Dash`

## 📝 Descrição

Este projeto tem como objetivo criar visualizações informativas e interativas para analisar o impacto de diferentes períodos de recessão nas vendas de automóveis nos Estados Unidos. Por meio da manipulação e exploração dos dados históricos, buscamos entender como variáveis econômicas e sazonais influenciaram o comportamento do consumidor ao longo dos anos.

Inclui dois relatórios de painel interativos criados com Plotly e Dash para explorar os dados de forma visual e dinâmica.

## 📁 Estrutura do Projeto

```
📦analyzing_impact_recession_auto_sales_with_plotly/
 ┣ 📂data/
 ┣ 📂notebooks/
 ┣ 📂images/
 ┣ 📂dashboard/
 ┣ 📜README.md
 ┗ 📜requirements.txt
```

## 🔍 Objetivos de Aprendizado

- Criar gráficos com Matplotlib e Seaborn para explorar tendências históricas.
- Usar mapas interativos com Folium para visualizar dados geográficos.
- Construir visualizações interativas com Plotly e dashboards com Dash.
- Interpretar dados econômicos e identificar padrões durante recessões.

## 📊 Resultados e Insights

- As vendas de automóveis caíram significativamente durante os períodos de recessão.
- Veículos sedans e executivos mostraram maior resiliência.
- Fatores como desemprego, confiança do consumidor e sazonalidade afetam as vendas.
- Mapas interativos destacaram variações regionais nas vendas.

## 📈 Dataset Utilizado

- [historical_automobile_sales.csv](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv)

### Principais Variáveis:

- `Date`, `Recession`, `Automobile_Sales`, `GDP`, `Unemployment_Rate`,
- `Consumer_Confidence`, `Price`, `Vehicle_Type`, `Competition`

## 🚀 Como Executar

```bash
git clone https://github.com/seuusuario/analyzing_impact_recession_auto_sales_with_plotly.git
cd analyzing_impact_recession_auto_sales_with_plotly
pip install -r requirements.txt
jupyter notebook notebooks/auto_sales_analysis.ipynb
```

## 📚 Referências

- [Pandas Documentation](https://pandas.pydata.org/)
- [Seaborn Tutorial](https://seaborn.pydata.org/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Plotly Express Guide](https://plotly.com/python/plotly-express/)
- [Folium Documentation](https://python-visualization.github.io/folium/)
- [Dash Docs](https://dash.plotly.com/)
- [Consumer Confidence Index - OECD](https://data.oecd.org/leadind/consumer-confidence-index-cci.htm)
- [U.S. Recession History - NBER](https://www.nber.org/research/data/us-business-cycle-expansions-and-contractions)