import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Funcție pentru încărcarea datelor dintr-un fișier CSV.
    """
    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()  # Citim toate liniile din fișier
        headers = lines[0].strip().split(',')  # Extragem antetul (numele coloanelor)
        for line in lines[1:]:  # Parcurgem liniile după antet
            values = line.strip().split(',')  # Separam valorile din linie
            data.append(values)  # Adăugăm valorile în listă
    return headers, data


def add_age_category_column(data, headers):
    """
    Funcție pentru adăugarea unei coloane suplimentare care indică categoria de vârstă.
    """
    # Adăugăm un antet nou pentru coloana cu categoriile de vârstă
    headers.append('Age Category')

    # Parcurgem fiecare rând de date și adăugăm categoria de vârstă corespunzătoare
    for row in data:
        age = float(row[6]) if row[6] != '' else 0  # Extragem vârsta pasagerului
        if age <= 20:
            age_category = '[0, 20]'
        elif age <= 40:
            age_category = '[21, 40]'
        elif age <= 60:
            age_category = '[41, 60]'
        else:
            age_category = '[61, max]'
        row.append(age_category)  # Adăugăm categoria de vârstă în rândul curent

    return headers, data


def write_result_to_file(headers, data, file_path):
    """
    Scrie rezultatul într-un fișier.
    """
    with open(file_path, 'w') as file:
        # Scriem antetul în fișier
        file.write(','.join(headers) + '\n')

        # Scriem fiecare rând de date în fișier
        for row in data:
            file.write(','.join(map(str, row)) + '\n')


def plot_age_category_distribution(data, output_file):
    """
    Funcție pentru generarea unui grafic care evidențiază distribuția categoriilor de vârstă.
    """
    # Extragem coloana cu categoriile de vârstă
    age_categories = [row[-1] for row in data]

    # Calculăm distribuția categoriilor de vârstă
    category_counts = {}
    for category in age_categories:
        if category in category_counts:
            category_counts[category] += 1
        else:
            category_counts[category] = 1

    # Generăm graficul
    plt.figure(figsize=(8, 6))
    plt.bar(category_counts.keys(), category_counts.values(), color='skyblue')
    plt.title('Distributia Categoriilor de Varsta')
    plt.xlabel('Categorie de Varsta')
    plt.ylabel('Numar de Pasageri')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_file)  # Salvăm graficul într-un fișier imagine
    plt.close()  # Închidem figura pentru a elibera resursele


# 1. Încărcarea Datelor
file_path = 'train.csv'  # Specifică calea către fișierul CSV
headers, data = load_data(file_path)

# 2. Adăugarea Coloanei pentru Categoria de Vârstă
headers, data = add_age_category_column(data, headers)

# 3. Scrierea Rezultatului în Fișier
write_result_to_file(headers, data, 'cerinta_5.txt')

# 4. Generarea Graficului pentru Distribuția Categoriilor de Vârstă
plot_age_category_distribution(data, 'age_category_distribution.png')
