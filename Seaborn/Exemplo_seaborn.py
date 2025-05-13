"""
Exemplo detalhado de visualização de dados com Seaborn

Este script demonstra o uso da biblioteca Seaborn para criar diferentes
tipos de gráficos estatísticos usando um dataset de gorjetas de restaurante.
É um exemplo didático para uso em aulas de visualização de dados.
"""

# Importações necessárias
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# Importando os dados do arquivo separado
from dados_restaurante import carregar_dados_gorjetas, gerar_dados_correlacionados

# Configurando o estilo do Seaborn para todas as visualizações
sns.set_theme(style="whitegrid")  # Configura um tema com linhas de grade em fundo branco

# Carregando o dataset de gorjetas de nosso módulo separado
df = carregar_dados_gorjetas()
print("Visualizando as primeiras linhas do dataset:")
print(df.head())
print("\nInformações do dataset:")
print(df.info())

# Criando subplots para organizar os gráficos
# Isso cria uma grade 2x2 de subplots, com tamanho total de 15x10 polegadas
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# 1. Gráfico de dispersão (Scatter plot) com regressão
# O gráfico de regressão mostra a relação entre conta total e gorjeta,
# incluindo uma linha de tendência linear que ajuda a visualizar a correlação
print("\n1. Criando gráfico de dispersão com linha de regressão...")
sns.regplot(
    x="total_bill",  # Variável independente (eixo x)
    y="tip",         # Variável dependente (eixo y)
    data=df,         # DataFrame contendo os dados
    scatter_kws={"color": "blue", "alpha": 0.5},  # Personalizando os pontos
    line_kws={"color": "red"},  # Personalizando a linha de regressão
    ax=axes[0, 0]    # Posicionando no primeiro subplot
)
axes[0, 0].set_title('Relação entre Conta Total e Gorjeta', fontsize=12)
axes[0, 0].set_xlabel('Valor Total da Conta (em dólares)')
axes[0, 0].set_ylabel('Valor da Gorjeta (em dólares)')

# 2. Gráfico de barras (Bar plot)
# Este gráfico mostra a média do valor da conta por dia da semana e gênero
print("2. Criando gráfico de barras agrupado...")
sns.barplot(
    x="day",         # Categorias no eixo x
    y="total_bill",  # Valores a serem agregados (média por padrão)
    hue="sex",       # Variável para agrupar (dividir) as barras
    data=df,         # DataFrame contendo os dados
    palette="viridis", # Escala de cores para diferenciar os grupos
    ax=axes[0, 1]    # Posicionando no segundo subplot
)
axes[0, 1].set_title('Média de Conta por Dia e Gênero', fontsize=12)
axes[0, 1].set_xlabel('Dia da Semana')
axes[0, 1].set_ylabel('Valor Médio da Conta (em dólares)')

# 3. Gráfico de boxplot
# Este gráfico mostra a distribuição dos valores de conta por dia e período
print("3. Criando boxplot para análise de distribuição...")
sns.boxplot(
    x="day",         # Categorias no eixo x
    y="total_bill",  # Valores para análise de distribuição
    hue="time",      # Variável para agrupar os boxplots
    data=df,         # DataFrame contendo os dados
    palette="Set3",  # Escala de cores
    ax=axes[1, 0]    # Posicionando no terceiro subplot
)
axes[1, 0].set_title('Distribuição de Valores por Dia e Turno', fontsize=12)
axes[1, 0].set_xlabel('Dia da Semana')
axes[1, 0].set_ylabel('Valor Total da Conta (em dólares)')

# 4. Gráfico de violino (Violin plot)
# Mostra a distribuição dos dados como um kernel density estimate,
# combinando as características de boxplots e density plots
print("4. Criando gráfico de violino...")
sns.violinplot(
    x="day",         # Categorias no eixo x
    y="total_bill",  # Valores para análise de distribuição
    hue="smoker",    # Variável para dividir os violinos
    data=df,         # DataFrame contendo os dados
    palette="Set2",  # Escala de cores
    split=True,      # Divide o violino ao meio para mostrar os grupos lado a lado
    ax=axes[1, 1]    # Posicionando no quarto subplot
)
axes[1, 1].set_title('Distribuição por Dia e Status de Fumante', fontsize=12)
axes[1, 1].set_xlabel('Dia da Semana')
axes[1, 1].set_ylabel('Valor Total da Conta (em dólares)')

# Ajustando layout e adicionando título geral
plt.tight_layout()  # Ajusta automaticamente os subplots para evitar sobreposição
fig.suptitle('Análise de Gorjetas em um Restaurante', fontsize=16, y=1.05)

# Salvando o gráfico
print("\nSalvando o gráfico com os subplots...")
plt.savefig('analise_gorjetas.png', dpi=300, bbox_inches='tight')

# Criando um heatmap com um novo conjunto de dados gerados
print("\n5. Criando heatmap de correlação...")
plt.figure(figsize=(10, 8))
# Gerar dados correlacionados aleatórios usando nossa função personalizada
corr_data, corr_matrix = gerar_dados_correlacionados(num_amostras=100, num_variaveis=5, semente=42)

# Criando o mapa de calor (heatmap)
# O mapa de calor mostra o coeficiente de correlação entre cada par de variáveis
sns.heatmap(
    corr_matrix,     # Matriz de correlação
    annot=True,      # Mostra os valores numéricos em cada célula
    cmap='coolwarm', # Escala de cores: azul para correlação negativa, vermelho para positiva
    vmin=-1,         # Valor mínimo para a escala de cores
    vmax=1           # Valor máximo para a escala de cores
)
plt.title('Mapa de Calor (Heatmap) de Correlações', fontsize=14)
plt.savefig('heatmap_exemplo.png', dpi=300, bbox_inches='tight')

# Criando um pairplot para visualizar relações entre múltiplas variáveis
print("\n6. Criando pairplot para análise multivariada...")
# O pairplot cria uma matriz de gráficos mostrando as relações entre pares de variáveis
pair_plot = sns.pairplot(
    df,                  # DataFrame contendo os dados
    hue='time',          # Variável categórica para colorir os pontos
    palette='Dark2',     # Escala de cores
    height=2.5,          # Altura de cada subplot
    diag_kind='kde'      # Tipo de gráfico na diagonal: Kernel Density Estimate
)
pair_plot.fig.suptitle('Relações entre Variáveis por Turno', fontsize=16, y=1.02)
plt.savefig('pairplot_exemplo.png', dpi=300, bbox_inches='tight')

print("\nAnálise completa! Imagens salvas: 'analise_gorjetas.png', 'heatmap_exemplo.png', 'pairplot_exemplo.png'")
print("Os gráficos mostram diferentes aspectos do mesmo dataset e demonstram a variedade")
print("de visualizações possíveis com o Seaborn.")

# Exibir os gráficos (comentar esta linha se não quiser que os gráficos sejam exibidos)
plt.show()
