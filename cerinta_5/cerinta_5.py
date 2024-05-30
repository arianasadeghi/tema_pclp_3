import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Functie pentru incarcarea datelor dintr-un fisier CSV.
    """
    data = []
    with open(file_path, 'r') as file:
        # Citim toate liniile din fisier
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


def add_age_category_column(data, headers):
    """
    Functie pentru adaugarea unei coloane suplimentare care indica categoria de varsta.
    """
    # Adaugam un antet nou pentru coloana cu categoriile de varsta
    headers.append('Age Category')

    # Parcurgem fiecare rând de date si adaugam categoria de varsta corespunzatoare
    for row in data:
        # Extragem varsta pasagerului
        age = float(row[6]) if row[6] != '' else 0
        if age <= 20:
            age_category = '[0, 20]'
        elif age <= 40:
            age_category = '[21, 40]'
        elif age <= 60:
            age_category = '[41, 60]'
        else:
            age_category = '[61, max]'
        # Adaugam categoria de varsta in randul curent
        row.append(age_category)

    return headers, data


def write_result_to_file(headers, data, file_path):
    """
    Scrie rezultatul intr-un fisier.
    """
    with open(file_path, 'w') as file:
        # Scriem antetul în fisier
        file.write(','.join(headers) + '\n')

        # Scriem fiecare rand de date in fisier
        for row in data:
            file.write(','.join(map(str, row)) + '\n')


def plot_age_category_distribution(data, output_file):
    """
    Functie pentru generarea unui grafic care evidentiaza distributia categoriilor de varsta
    """
    # Extragem coloana cu categoriile de varsta
    age_categories = [row[-1] for row in data]

    # Calculam distributia categoriilor de varsta
    category_counts = {}
    for category in age_categories:
        if category in category_counts:
            category_counts[category] += 1
        else:
            category_counts[category] = 1

    # Generam graficul
    plt.figure(figsize=(8, 6))
    plt.bar(category_counts.keys(), category_counts.values(), color='skyblue')
    plt.title('Distributia Categoriilor de Varsta')
    plt.xlabel('Categorie de Varsta')
    plt.ylabel('Numar de Pasageri')
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Salvam graficul intr-un fisier imagine
    plt.savefig(output_file)
    # Inchidem figura pentru a elibera resursele
    plt.close()


# 1. Incarcarea datelor
# Specifica calea catre fisierul CSV
file_path = 'train.csv'
headers, data = load_data(file_path)

# 2. Adaugarea coloanei pentru categoria de varsta
headers, data = add_age_category_column(data, headers)

# 3. Scrierea rezultatului in fisier
write_result_to_file(headers, data, 'cerinta_5.txt')

# 4. Generarea graficului pentru distributia categoriilor de varsta
plot_age_category_distribution(data, 'age_category_distribution.png')
