import pandas as pd

# Citirea fisierului CSV
df = pd.read_csv('train.csv')

# Determinarea numarului de coloane
num_columns = len(df.columns)

# Determinarea tipurilor de date pentru fiecare coloana
data_types = df.dtypes

# Calcularea numarului de valori lipsa pentru fiecare coloana
missing_values = df.isnull().sum()

# Determinarea numarului de linii
num_rows = len(df)

# Verificarea existentei liniilor duplicate
duplicate_rows = df.duplicated().sum()

# Deschiderea fisierului cerinta_1.txt in modul de scriere
with open('cerinta_1.txt', 'w') as file:
    # Scrierea rezultatelor in fisier
    file.write(f"Numarul de coloane: {num_columns}\n")
    file.write("\nTipurile datelor din fiecare coloana:\n")
    file.write(f"{data_types}\n")
    file.write("\nNumarul de valori lipsa pentru fiecare coloana:\n")
    file.write(f"{missing_values}\n")
    file.write(f"\nNumarul de linii: {num_rows}\n")
    file.write(f"Numarul de linii duplicate: {duplicate_rows}\n")
