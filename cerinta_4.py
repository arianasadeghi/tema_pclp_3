def load_data(file_path):
    """
    Functie pentru incarcarea datelor dintr-un fisier CSV.
    """
    data = []
    with open(file_path, 'r') as file:
        # Citim toate liniile din fișier
        lines = file.readlines()
        # Extragem antetul (numele coloanelor)
        headers = lines[0].strip().split(',')
        # Parcurgem liniile dupa antet
        for line in lines[1:]:
            # Separam valorile din linie
            values = line.strip().split(',')
            # Adaugam valorile in lista
            data.append(values)
    return headers, data


def identify_missing_values(headers, data):
    """
    Functie pentru identificarea valorilor lipsa in datele incarcate.
    """
    missing_values = {}
    for i, header in enumerate(headers):
        # Initializam numarul de valori lipsa pentru fiecare coloana la 0
        missing_values[header] = 0
        for row in data:
            # Daca valoarea din coloana este vida
            if row[i] == '':
                # Incrementam numarul de valori lipsa pentru acea coloana
                missing_values[header] += 1
    return missing_values


def calculate_missing_values_percentage(data, column_index):
    """
    Functie pentru calcularea procentului de valori lipsa si a proportiei acestora pentru o anumita coloana.
    """
    # Numarul total de randuri in date
    total_rows = len(data)
    missing_count = 0
    for row in data:
        # Daca valoarea din coloana este vida
        if row[column_index] == '':
            # Incrementam numarul de valori lipsa
            missing_count += 1
    if total_rows == 0:
        return 0, 0
    
    # Calculam procentul de valori lipsa
    missing_percentage = (missing_count / total_rows) * 100
    # Calculam proportia valorilor lipsa
    missing_proportion = missing_count / total_rows
    return missing_count, missing_percentage, missing_proportion


# 1. Incarcarea Datelor
# Specifica calea catre fisierul CSV
file_path = 'train.csv'
headers, data = load_data(file_path)

# 2. Identificarea Valorilor Lipsă
missing_values = identify_missing_values(headers, data)
with open("cerinta_4.txt", "w") as output_file:
    output_file.write("Numarul de valori lipsa pentru fiecare coloana:\n")
    for column, count in missing_values.items():
        output_file.write(f"{column}: {count}\n")

# 3. Determinarea Procentului de Valori Lipsa si Proportia acestora pentru Fiecare Coloana
with open("cerinta_4.txt", "a") as output_file:
    output_file.write("\nProcentul si proportia de valori lipsa pentru fiecare coloana:\n")
    for i, header in enumerate(headers):
        missing_count, missing_percentage, missing_proportion = calculate_missing_values_percentage(data, i)
        output_file.write(f"Coloana '{header}':\n")
        output_file.write(f"  Numarul de valori lipsa: {missing_count}\n")
        output_file.write(f"  Procentul de valori lipsa: {missing_percentage:.2f}%\n")
        output_file.write(f"  Proportia de valori lipsa: {missing_proportion:.2f}\n")

# 4. Determinarea Procentului de Valori Lipsa pentru Fiecare Clasa (Coloana 'Survived')
# Gasim indexul coloanei 'Survived' in antet
survived_column_index = headers.index('Survived')
with open("cerinta_4.txt", "a") as output_file:
    output_file.write("\nProcentul de valori lipsa pentru fiecare clasa in coloana 'Survived':\n")
    # Parcurgem fiecare clasa posibila (0 sau 1)
    for cls in [0, 1]:
        missing_count, missing_percentage, missing_proportion = calculate_missing_values_percentage(data, survived_column_index)
        output_file.write(f"Clasa {cls}: {missing_percentage:.2f}%\n")
