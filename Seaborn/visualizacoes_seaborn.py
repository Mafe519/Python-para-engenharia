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

# Importando os dados do nosso arquivo separado
from dados_restaurante import carregar_dados_gorjetas, gerar_dados_correlacionados

# Configurando o estilo do Seaborn e localização em português
plt.rcParams['axes.formatter.use_locale'] = True
sns.set_theme(style="whitegrid")

# Carregando o dataset de gorjetas
print("Carregando dados...")
df = carregar_dados_gorjetas()
print("Primeiras linhas do dataset:")
print(df.head())

# Criando subplots para organizar os gráficos
print("\nCriando visualizações...")
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# 1. Gráfico de dispersão (Scatter plot) com regressão
print("1. Criando gráfico de dispersão com linha de regressão...")
sns.regplot(
    x="valor_conta", 
    y="gorjeta", 
    data=df, 
    scatter_kws={"color": "blue", "alpha": 0.5},
    line_kws={"color": "red"},
    ax=axes[0, 0]
)
axes[0, 0].set_title('Relação entre Valor da Conta e Gorjeta', fontsize=12)
axes[0, 0].set_xlabel('Valor Total da Conta (R$)')
axes[0, 0].set_ylabel('Valor da Gorjeta (R$)')

# 2. Gráfico de barras (Bar plot)
print("2. Criando gráfico de barras agrupado...")
sns.barplot(
    x="dia", 
    y="valor_conta", 
    hue="genero", 
    data=df,
    palette="viridis",
    ax=axes[0, 1]
)
axes[0, 1].set_title('Média de Conta por Dia e Gênero', fontsize=12)
axes[0, 1].set_xlabel('Dia da Semana')
axes[0, 1].set_ylabel('Valor Médio da Conta (R$)')

# 3. Gráfico de boxplot
print("3. Criando boxplot para análise de distribuição...")
sns.boxplot(
    x="dia", 
    y="valor_conta", 
    hue="horario", 
    data=df,
    palette="Set3",
    ax=axes[1, 0]
)
axes[1, 0].set_title('Distribuição de Valores por Dia e Horário', fontsize=12)
axes[1, 0].set_xlabel('Dia da Semana')
axes[1, 0].set_ylabel('Valor Total da Conta (R$)')

# 4. Gráfico de violino (Violin plot)
print("4. Criando gráfico de violino...")
sns.violinplot(
    x="dia", 
    y="valor_conta", 
    hue="fumante", 
    data=df, 
    palette="Set2",
    split=True,
    ax=axes[1, 1]
)
axes[1, 1].set_title('Distribuição por Dia e Status de Fumante', fontsize=12)
axes[1, 1].set_xlabel('Dia da Semana')
axes[1, 1].set_ylabel('Valor Total da Conta (R$)')

# Ajustando layout e adicionando título geral
plt.tight_layout()
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
sns.heatmap(
    corr_matrix,
    annot=True,      # Mostrar valores numéricos
    cmap='coolwarm', # Escala de cores: azul (negativo) para vermelho (positivo)
    vmin=-1,         # Valor mínimo para a escala de cores
    vmax=1           # Valor máximo para a escala de cores
)
plt.title('Mapa de Calor (Heatmap) de Correlações', fontsize=14)
plt.savefig('heatmap_exemplo.png', dpi=300, bbox_inches='tight')

# Criando um pairplot para visualizar relações entre múltiplas variáveis
print("\n6. Criando pairplot para análise multivariada...")
pair_plot = sns.pairplot(
    df,
    hue='genero',    # Colorir por gênero
    palette='Dark2', # Paleta de cores
    height=2.5,      # Tamanho de cada subplot
    vars=['valor_conta', 'gorjeta', 'pessoas'],  # Variáveis a incluir
    diag_kind='kde'  # Tipo de gráfico na diagonal (Kernel Density Estimate)
)
pair_plot.fig.suptitle('Relações entre Variáveis por Gênero', fontsize=16, y=1.02)
plt.savefig('pairplot_exemplo.png', dpi=300, bbox_inches='tight')

# Criando um gráfico adicional: countplot para variáveis categóricas
plt.figure(figsize=(12, 6))
sns.countplot(x='dia', hue='horario', data=df, palette='pastel')
plt.title('Contagem de Registros por Dia da Semana e Horário', fontsize=14)
plt.xlabel('Dia da Semana')
plt.ylabel('Quantidade')
plt.savefig('contagem_categorias.png', dpi=300, bbox_inches='tight')

# Criando um gráfico de distribuição
plt.figure(figsize=(12, 6))
sns.histplot(data=df, x='gorjeta', kde=True, bins=15)
plt.title('Distribuição dos Valores de Gorjeta', fontsize=14)
plt.xlabel('Valor da Gorjeta (R$)')
plt.ylabel('Frequência')
plt.savefig('distribuicao_gorjetas.png', dpi=300, bbox_inches='tight')

print("\nAnálise completa! Imagens salvas:")
print("- analise_gorjetas.png - Conjunto de gráficos principais")
print("- heatmap_exemplo.png - Mapa de calor de correlações")
print("- pairplot_exemplo.png - Matriz de gráficos de relações entre variáveis")
print("- contagem_categorias.png - Contagem de registros por categoria")
print("- distribuicao_gorjetas.png - Distribuição de valores de gorjeta")

# Exibir os gráficos na tela (comentar se não desejar exibir)
plt.show()
