# Python para Engenharia - Material Didático

Este repositório contém materiais e exemplos práticos para o ensino de Python voltado à Engenharia.

## Pré-requisitos

- Python 3.x instalado no computador
- pip (gerenciador de pacotes do Python)

## Instalação das Dependências

Para instalar todas as bibliotecas necessárias, execute os seguintes comandos no terminal:

```bash
pip install pandas numpy matplotlib
pip install scipy sympy
pip install pygame
pip install flask
pip install seaborn
pip install pillow qrcode
pip install tkinter
```

## Estrutura do Projeto e Como Executar

### Exemplos Básicos

1. **PandasExample.py** - Exemplo de manipulação de dados com Pandas
   ```bash
   python PandasExample.py
   ```

2. **plot.py** - Visualização de dados com Matplotlib
   ```bash
   python plot.py
   ```

3. **pygameExample.py** - Exemplo de interface gráfica com Pygame
   ```bash
   python pygameExample.py
   ```

4. **scipyExample.py** - Computação científica com SciPy
   ```bash
   python scipyExample.py
   ```

5. **sympyExample.py** - Matemática simbólica com SymPy
   ```bash
   python sympyExample.py
   ```

### Exemplos de Fixação

1. **fibonacci.py** - Implementação da sequência de Fibonacci
   ```bash
   python ExemplosFixacao/fibonacci.py
   ```

2. **triangulo.py** - Cálculos com triângulos
   ```bash
   python ExemplosFixacao/triangulo.py
   ```

### Flask (Desenvolvimento Web)

1. **Exemplo_simples_site.py** - Site simples com Flask
   ```bash
   python Flask/Exemplo_simples_site.py
   ```

2. **Exemplo_site_completo.py** - Site mais elaborado com Flask
   ```bash
   python Flask/Exemplo_site_completo.py
   ```

### Seaborn (Visualização de Dados)

1. **Exemplo_seaborn.py** - Gráficos estatísticos com Seaborn
   ```bash
   python Seaborn/Exemplo_seaborn.py
   ```

### Tkinter (Interface Gráfica)

1. **gerador_QRcode.py** - Gerador de QR Code com interface gráfica
   ```bash
   python tkinter/gerador_QRcode.py
   ```

## Observações Importantes

- Certifique-se de que o Python está instalado corretamente executando `python --version` no terminal
- Em alguns sistemas, pode ser necessário usar `pip3` ao invés de `pip`
- Em sistemas Linux, pode ser necessário instalar o tkinter separadamente usando:
  ```bash
  sudo apt-get install python3-tk
  ```
- Para executar os exemplos, navegue até a pasta do projeto no terminal antes de executar os comandos

## Problemas Comuns

1. **ModuleNotFoundError**: Significa que uma biblioteca não está instalada. Use o pip para instalar.
2. **Permission Denied**: Use `sudo pip install` no Linux/Mac ou execute o prompt de comando como administrador no Windows.
3. **SSL Certificate Error**: Em caso de erro de certificado, você pode usar:
   ```bash
   pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org <nome-do-pacote>
   ```