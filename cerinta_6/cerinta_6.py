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

    # Parcurgem fiecare rand de date si adaugam categoria de varsta corespunzatoare
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


def count_survived_males_by_age_category(data):
    """
    Functie pentru numararea barbatilor supravietuitori in fiecare categorie de varsta.
    """
    survived_males_by_age_category = {'[0, 20]': 0, '[21, 40]': 0, '[41, 60]': 0, '[61, max]': 0}
    for row in data:
        if row[5] == 'male' and row[1] == '1':
            # Extragem categoria de varsta
            age_category = row[-1]
            survived_males_by_age_category[age_category] += 1
    return survived_males_by_age_category


# 1. Incarcarea datelor
# Specifica calea catre fisierul CSV
file_path = 'train.csv'
headers, data = load_data(file_path)

# 2. Adaugarea coloanei pentru categoria de varsta
headers, data = add_age_category_column(data, headers)

# 3. Calcularea numarului de barbati supravietuitori in fiecare categorie de varsta
survived_males_by_age_category = count_survived_males_by_age_category(data)

# 4. Afisarea numarului de barbati supravietuitori in fiecare categorie de varsta
for age_category, count in survived_males_by_age_category.items():
    print(f"{age_category}: {count}")

# 5. Realizarea graficului
plt.bar(survived_males_by_age_category.keys(), survived_males_by_age_category.values())
plt.xlabel('Categorie de Varsta')
plt.ylabel('Numar de Barbati Supravietuitori')
plt.title('Numar de Barbaai Supravietuitori in Fiecare Categorie de Varsta')
plt.xticks(rotation=45)
plt.tight_layout()

# 6. Salvarea graficului ca fisier PNG
plt.savefig('age_distribution_survived_males.png')
