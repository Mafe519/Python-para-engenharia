

import pandas as pd
import numpy as np

def carregar_dados_gorjetas():
    """
    Carrega o dataset de gorjetas de restaurante.
    
    O dataset contém os seguintes campos:
    - valor_conta: valor total da conta (em reais)
    - gorjeta: valor da gorjeta (em reais)
    - genero: gênero do cliente (Feminino, Masculino)
    - fumante: se o cliente é fumante (Sim, Não)
    - dia: dia da semana (Dom, Sab, Qui, Sex)
    - horario: horário da refeição (Almoço, Jantar)
    - pessoas: número de pessoas na mesa
    
    Returns:
        DataFrame: Dataset de gorjetas
    """
    # Dataset simplificado e traduzido para português (apenas 50 registros)
    dados = {
        'valor_conta': [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78, 
                        10.27, 35.26, 15.42, 18.43, 14.83, 21.58, 10.33, 16.29, 16.97, 20.65, 
                        17.92, 20.29, 15.77, 39.42, 19.82, 17.81, 13.37, 12.69, 21.70, 19.65, 
                        9.55, 18.35, 15.06, 20.69, 17.78, 24.06, 16.31, 16.93, 18.69, 31.27, 
                        16.04, 17.46, 13.94, 9.68, 30.40, 18.29, 22.23, 32.40, 28.55, 18.04],
                        
        'gorjeta': [1.01, 1.66, 3.50, 3.31, 3.61, 4.71, 2.00, 3.12, 1.96, 3.23, 
                   1.71, 5.00, 1.57, 3.00, 3.02, 3.92, 1.67, 3.71, 3.50, 3.35, 
                   4.08, 2.75, 2.23, 7.58, 3.18, 2.34, 2.00, 2.00, 4.30, 3.00, 
                   1.45, 2.50, 3.00, 2.45, 3.27, 3.60, 2.00, 3.07, 2.31, 5.00,
                   2.24, 2.54, 3.06, 1.32, 5.60, 3.00, 5.00, 6.00, 2.05, 3.00],
                   
        'genero': ['Feminino', 'Masculino', 'Masculino', 'Masculino', 'Feminino', 
                  'Masculino', 'Masculino', 'Masculino', 'Feminino', 'Masculino',
                  'Masculino', 'Feminino', 'Masculino', 'Masculino', 'Feminino', 
                  'Masculino', 'Feminino', 'Masculino', 'Masculino', 'Masculino',
                  'Masculino', 'Masculino', 'Feminino', 'Masculino', 'Masculino', 
                  'Masculino', 'Masculino', 'Masculino', 'Masculino', 'Feminino',
                  'Feminino', 'Masculino', 'Feminino', 'Masculino', 'Masculino', 
                  'Masculino', 'Feminino', 'Masculino', 'Masculino', 'Masculino',
                  'Masculino', 'Feminino', 'Masculino', 'Masculino', 'Feminino',
                  'Feminino', 'Masculino', 'Masculino', 'Feminino', 'Masculino'],
                  
        'fumante': ['Não', 'Não', 'Não', 'Não', 'Não', 'Não', 'Não', 'Não', 'Não', 'Não',
                   'Não', 'Não', 'Não', 'Não', 'Não', 'Não', 'Não', 'Não', 'Não', 'Não',
                   'Não', 'Não', 'Não', 'Não', 'Não', 'Não', 'Não', 'Não', 'Não', 'Não',
                   'Não', 'Não', 'Não', 'Não', 'Não', 'Não', 'Não', 'Não', 'Não', 'Não',
                   'Não', 'Não', 'Não', 'Não', 'Não', 'Não', 'Não', 'Não', 'Não', 'Sim'],
                   
        'dia': ['Dom', 'Dom', 'Dom', 'Dom', 'Dom', 'Dom', 'Dom', 'Dom', 'Dom', 'Dom',
               'Dom', 'Dom', 'Dom', 'Dom', 'Dom', 'Dom', 'Dom', 'Dom', 'Dom', 'Dom',
               'Dom', 'Dom', 'Dom', 'Dom', 'Dom', 'Dom', 'Dom', 'Dom', 'Dom', 'Dom',
               'Dom', 'Dom', 'Dom', 'Dom', 'Dom', 'Dom', 'Dom', 'Dom', 'Dom', 'Dom',
               'Dom', 'Dom', 'Dom', 'Dom', 'Dom', 'Dom', 'Dom', 'Dom', 'Dom', 'Dom'],
               
        'horario': ['Jantar', 'Jantar', 'Jantar', 'Jantar', 'Jantar', 'Jantar', 'Jantar',
                   'Jantar', 'Jantar', 'Jantar', 'Jantar', 'Jantar', 'Jantar', 'Jantar',
                   'Jantar', 'Jantar', 'Jantar', 'Jantar', 'Jantar', 'Jantar', 'Jantar',
                   'Jantar', 'Jantar', 'Jantar', 'Jantar', 'Jantar', 'Jantar', 'Jantar',
                   'Jantar', 'Jantar', 'Jantar', 'Jantar', 'Jantar', 'Jantar', 'Jantar',
                   'Jantar', 'Jantar', 'Jantar', 'Jantar', 'Jantar', 'Jantar', 'Jantar',
                   'Jantar', 'Jantar', 'Jantar', 'Jantar', 'Jantar', 'Jantar', 'Jantar',
                   'Jantar'],
                   
        'pessoas': [2, 3, 3, 2, 4, 4, 2, 4, 2, 2, 
                  2, 4, 2, 4, 2, 2, 3, 3, 3, 3,
                  2, 2, 2, 4, 2, 4, 2, 2, 2, 2, 
                  2, 2, 2, 4, 2, 4, 1, 2, 2, 4, 
                  2, 2, 2, 2, 4, 2, 2, 2, 2, 4]
    }
    
    # Criar DataFrame e retornar
    return pd.DataFrame(dados)

def gerar_dados_correlacionados(num_amostras=100, num_variaveis=5, semente=42):
    """
    Gera dados aleatórios correlacionados para demonstrar o heatmap.
    
    Args:
        num_amostras: Número de observações a gerar
        num_variaveis: Número de variáveis a gerar
        semente: Valor para reprodutibilidade
        
    Returns:
        DataFrame: Dados correlacionados gerados aleatoriamente
        DataFrame: Matriz de correlação desses dados
    """
    np.random.seed(semente)
    
    # Gerando dados aleatórios
    dados = pd.DataFrame(np.random.randn(num_amostras, num_variaveis),
                        columns=['A', 'B', 'C', 'D', 'E'])
    
    # Calculando a matriz de correlação
    matriz_correlacao = dados.corr()
    
    return dados, matriz_correlacao

# Descrição resumida do dataset
descricao_dataset = """
Este dataset contém informações sobre gorjetas dadas em um restaurante.
Ele inclui variáveis como valor total da conta, gorjeta, gênero do cliente,
status de fumante, dia da semana, hora da refeição e tamanho do grupo.

O dataset é frequentemente usado em análises estatísticas e visualizações
para demonstrar a relação entre esses diferentes fatores e o valor da gorjeta.
"""

if __name__ == "__main__":
    # Se este arquivo for executado diretamente, mostra informações sobre o dataset
    df = carregar_dados_gorjetas()
    print(descricao_dataset)
    print("\nPrimeiras 5 linhas do dataset:")
    print(df.head())
    print("\nEstatísticas resumidas:")
    print(df.describe())
    print("\nVerificando formatos dos dados:")
    print(f"Total de registros: {len(df)}")
    for coluna in df.columns:
        print(f"Coluna '{coluna}': {len(df[coluna])} valores")
