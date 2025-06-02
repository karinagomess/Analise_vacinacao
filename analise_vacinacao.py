import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Base de Dados - https://opendatasus.saude.gov.br/dataset/covid-19-vacinacao

# Caminho do arquivo CSV
df = pd.read_csv(r"C:\Users\karin\Documents\Projetos\Projeto_analise_vacinacao\dados _vacinacao.csv", sep=';', encoding='utf-8-sig')


# Seleciona colunas úteis
print(df.columns.tolist())
df = df[['paciente_idade', 'paciente_enumsexo', 'vacina_dataAplicacao',
         'vacina_descricao_dose', 'estabelecimento_municipio_nome']]


 
df.dropna(inplace=True)


# Tipos de dose aplicadas
df['vacina_descricao_dose'].value_counts().plot(kind='bar')
plt.title("Tipos de dose aplicadas")
plt.ylabel("Quantidade")
plt.xlabel("tipo de Dose")
plt.tight_layout()
plt.show()

print("Idade média:", df['paciente_idade'].mean())