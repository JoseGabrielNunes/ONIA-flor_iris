import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
df = pd.read_csv('iris_data.csv')

# Exibir as primeiras linhas do dataset para verificar os dados
print(df.head())

# Análise da distribuição de cores das flores
cores = df['Cor'].value_counts()

# Gráfico de barras para a distribuição de cores
plt.figure(figsize=(8, 6))
cores.plot(kind='bar', color=['purple', 'blue', 'yellow', 'white'])
plt.title('Distribuição das Cores das Flores Íris')
plt.xlabel('Cores')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.show()

# Análise da altura mínima e máxima de cada espécie
plt.figure(figsize=(10, 6))

# Plotando altura mínima e máxima para cada espécie
plt.bar(df['Espécie'], df['Altura_Maxima_cm'], color='orange', alpha=0.7, label='Altura Máxima')
plt.bar(df['Espécie'], df['Altura_Minima_cm'], color='lightblue', alpha=0.7, label='Altura Mínima')

plt.title('Altura Mínima e Máxima das Espécies de Íris')
plt.xlabel('Espécie de Íris')
plt.ylabel('Altura (cm)')
plt.legend()
plt.xticks(rotation=45)
plt.show()

# Análise da popularidade ao longo das décadas
decadas = ['Anos 70', 'Anos 80', 'Anos 90', 'Anos 2000', 'Anos 2010']
popul_iris = df[decadas].mean()

# Gráfico de linha para a popularidade das flores ao longo das décadas
plt.figure(figsize=(10, 6))
plt.plot(decadas, popul_iris, marker='o', color='blue', label='Popularidade média')
plt.title('Popularidade das Espécies de Íris ao Longo das Décadas')
plt.xlabel('Décadas')
plt.ylabel('Popularidade (%)')
plt.legend()
plt.grid(True)
plt.show()
