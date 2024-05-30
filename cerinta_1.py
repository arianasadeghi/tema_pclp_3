import sys

def analyze_csv(file_path):
    """
    Functie pentru analiza unui fisier CSV si scrierea rezultatului intr-un fisier text.
    """
    # Deschidem fisierul de scriere
    with open("cerinta_1.txt", "w") as output_file:
        # Redirectionăm fluxul de iesire catre fisierul de scriere
        original_stdout = sys.stdout
        sys.stdout = output_file

        # Codul pentru analiza CSV
        with open(file_path, "r") as f:
            lines = f.readlines()

        header = lines[0].strip().split(',')
        num_columns = len(header)

        data_types = {col: [] for col in header}
        missing_values = {col: 0 for col in header}
        num_rows = 0
        unique_rows = set()

        for line in lines[1:]:
            num_rows += 1
            
            row = line.strip().split(',')
            row_tuple = tuple(row)
            unique_rows.add(row_tuple)

            for i, col in enumerate(header):
                if i < len(row):
                    value = row[i].strip()
                else:
                    value = ''
                
                if value == '':
                    missing_values[col] += 1
                else:
                    if is_integer(value):
                        data_types[col].append('int')
                    elif is_float(value):
                        data_types[col].append('float')
                    else:
                        data_types[col].append('str')

        dominant_data_types = {}
        for col, types in data_types.items():
            if 'str' in types:
                dominant_data_types[col] = 'str'
            elif 'float' in types:
                dominant_data_types[col] = 'float'
            elif 'int' in types:
                dominant_data_types[col] = 'int'
            else:
                dominant_data_types[col] = 'unknown'

        duplicate_rows = num_rows - len(unique_rows)

        print(f"Numarul de coloane: {num_columns}")
        print("Tipurile datelor din fiecare coloana:")
        for i, col in enumerate(header):
            dtype = dominant_data_types[col]
            print(f"  {i+1}. {col}: {dtype}")

        print("Numarul de valori lipsa pentru fiecare coloana:")
        for i, col in enumerate(header):
            count = missing_values[col]
            print(f"  {i+1}. {col}: {count}")

        print(f"Numarul de linii: {num_rows + 1}")
        print(f"Numarul de linii duplicate: {duplicate_rows}")

        # Redirectionam inapoi fluxul de iesire catre consola
        sys.stdout = original_stdout

def is_integer(s):
    """
    Functie pentru verificarea daca un sir poate fi convertit intr-un intreg.
    """
    try:
        int(s)
        return True
    except ValueError:
        return False

def is_float(s):
    """
    Functie pentru verificarea daca un sir poate fi convertit intr-un numar in virgula mobila.
    """
    try:
        float(s)
        return True
    except ValueError:
        return False

# Apelarea functiei pentru un fisier CSV specificat
file_path = 'train.csv'
analyze_csv(file_path)
