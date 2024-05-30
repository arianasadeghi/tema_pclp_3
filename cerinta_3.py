import pandas as pd
import matplotlib.pyplot as plt

# Citirea fisierului CSV
df = pd.read_csv('train.csv')

# Selectia coloanelor numerice
numeric_columns = df.select_dtypes(include=['int64', 'float64'])

# Generarea si salvarea histogramei pentru fiecare coloana numerica
for column in numeric_columns.columns:
    plt.figure(figsize=(8, 6))
    plt.hist(numeric_columns[column].dropna(), bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Histograma pentru coloana "{column}"')
    plt.xlabel('Valoare')
    plt.ylabel('Numar de exemple')
    plt.grid(True)
    # Salveaza histograma intr-un fisier PNG
    plt.savefig(f'histogram_{column}.png')
    # Inchide figura curenta pentru a elibera resursele
    plt.close()
