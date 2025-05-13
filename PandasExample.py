import pandas as pd

data = {
    'Tempo (s)': [0, 1, 2, 3, 4],
    'Temperatura (°C)': [22.4, 23.1, 24.0, 24.5, 25.0]
}
df = pd.DataFrame(data)
print(df)
print("Temperatura média:", df['Temperatura (°C)'].mean())
