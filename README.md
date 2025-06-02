# 📊 Análise de Vacinação COVID-19 no Brasil

Este projeto realiza uma análise exploratória simples com base nos dados de vacinação contra a COVID-19 fornecidos pelo Ministério da Saúde do Brasil (DataSUS). Ele utiliza bibliotecas do Python como `pandas`, `matplotlib` e `seaborn` para manipular os dados e gerar gráficos.

---

## 🗂️ Fonte dos Dados

Os dados utilizados neste projeto estão disponíveis publicamente no portal OpenDataSUS:

🔗 [Open DataSUS – COVID-19 Vacinação](https://opendatasus.saude.gov.br/dataset/covid-19-vacinacao)

---

## 🧪 Funcionalidades do Código

- Leitura de um arquivo CSV com os dados de vacinação
- Seleção de colunas relevantes para análise
- Limpeza de dados (remoção de registros nulos)
- Geração de gráfico de barras com a quantidade de doses aplicadas por tipo
- Cálculo da idade média dos vacinados

---

## 📷 Exemplo de Saída

O código gera um gráfico de barras como este:

![Gráfico_dados_vacinacao](https://github.com/user-attachments/assets/5b8faa30-97e6-4fbc-b265-9c6dc492f56a)

Também é exibido no terminal:
Idade média: 45.7


---

## 📌 Pré-requisitos

- Python 3.7 ou superior
- Bibliotecas:

```bash
pip install pandas matplotlib seaborn
