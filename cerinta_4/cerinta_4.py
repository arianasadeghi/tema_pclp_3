import pandas as pd

# Citim fisierul CSV
df = pd.read_csv('train.csv')

# Identificam coloanele pentru care exista valori lipsa
columns_with_missing_values = df.columns[df.isnull().any()].tolist()

# Determinam numarul si proportia valorilor lipsa pentru fiecare coloana
missing_values_info = {}
for column in columns_with_missing_values:
    # Numarul total de valori lipsa in coloana
    total_missing_values = df[column].isnull().sum()
    # Procentul de valori lipsa in coloana
    percentage_missing_values = (total_missing_values / len(df)) * 100
    
    # Procentul de valori lipsa pentru fiecare clasa in coloana "Survived"
    survived_missing_percentage = (df[df['Survived'] == 1][column].isnull().sum() / len(df[df['Survived'] == 1])) * 100
    not_survived_missing_percentage = (df[df['Survived'] == 0][column].isnull().sum() / len(df[df['Survived'] == 0])) * 100
    
    # Salvam informatiile intr-un dictionar
    missing_values_info[column] = {
        'TotalMissingValues': total_missing_values,
        'PercentageMissingValues': percentage_missing_values,
        'SurvivedMissingPercentage': survived_missing_percentage,
        'NotSurvivedMissingPercentage': not_survived_missing_percentage
    }

# Scriem rezultatele intr-un fisier text
with open("cerinta_4.txt", "w") as output_file:
    for column, info in missing_values_info.items():
        output_file.write(f"Coloana '{column}':\n")
        output_file.write(f"  Numarul total de valori lipsa: {info['TotalMissingValues']}\n")
        output_file.write(f"  Procentul total de valori lipsa: {info['PercentageMissingValues']:.2f}%\n")
        output_file.write(f"  Procentul de valori lipsa pentru clasa 'Survived': {info['SurvivedMissingPercentage']:.2f}%\n")
        output_file.write(f"  Procentul de valori lipsa pentru clasa 'Not Survived': {info['NotSurvivedMissingPercentage']:.2f}%\n")
