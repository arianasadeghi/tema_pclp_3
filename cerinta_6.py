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


def count_survived_males_by_age_category(data):
    """
    Funcție pentru numărarea bărbaților supraviețuitori în fiecare categorie de vârstă.
    """
    survived_males_by_age_category = {'[0, 20]': 0, '[21, 40]': 0, '[41, 60]': 0, '[61, max]': 0}
    for row in data:
        if row[5] == 'male' and row[1] == '1':
            age_category = row[-1]  # Extragem categoria de vârstă
            survived_males_by_age_category[age_category] += 1
    return survived_males_by_age_category


# 1. Încărcarea Datelor
file_path = 'train.csv'  # Specifică calea către fișierul CSV
headers, data = load_data(file_path)

# 2. Adăugarea Coloanei pentru Categoria de Vârstă
headers, data = add_age_category_column(data, headers)

# 3. Calcularea Numărului de Bărbați Supraviețuitori în Fiecare Categorie de Vârstă
survived_males_by_age_category = count_survived_males_by_age_category(data)

# 4. Afișarea Numărului de Bărbați Supraviețuitori în Fiecare Categorie de Vârstă
for age_category, count in survived_males_by_age_category.items():
    print(f"{age_category}: {count}")

# 5. Realizarea Graficului
plt.bar(survived_males_by_age_category.keys(), survived_males_by_age_category.values())
plt.xlabel('Categorie de Varsta')
plt.ylabel('Numar de Barbati Supravietuitori')
plt.title('Numar de Barbaai Supravietuitori in Fiecare Categorie de Varsta')
plt.xticks(rotation=45)
plt.tight_layout()

# 5. Salvarea Graficului ca Fișier PNG
plt.savefig('age_distribution_survived_males.png')
