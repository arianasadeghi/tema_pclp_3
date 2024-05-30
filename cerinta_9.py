def extract_title(name):
    """
    Funcție pentru extragerea titlului din numele unei persoane.
    """
    titles = ['Mr', 'Miss', 'Mrs', 'Master', 'Dr', 'Rev', 'Major', 'Col', 'Mlle', 'Mme', 'Ms', 'Sir', 'Lady', 'Don', 'Jonkheer', 'Countess', 'Capt']
    for title in titles:
        if title in name:
            return title
    return ""


def verify_titles_with_sex(data, headers):
    """
    Funcție pentru verificarea dacă titlurile de noblețe corespund cu sexul persoanei.
    """
    title_to_sex = {
        'Mr': 'male',
        'Master': 'male',
        'Don': 'male',
        'Sir': 'male',
        'Dr': 'male',
        'Rev': 'male',
        'Major': 'male',
        'Col': 'male',
        'Capt': 'male',
        'Jonkheer': 'male',
        'Mrs': 'female',
        'Miss': 'female',
        'Ms': 'female',
        'Mme': 'female',
        'Mlle': 'female',
        'Lady': 'female',
        'Dona': 'female'
    }

    headers.append('Title Matches Sex')

    for row in data:
        name = row[4]  # Name is in the 4th column (index 3)
        sex = row[5]   # Sex is in the 5th column (index 4)
        title = extract_title(name)
        expected_sex = title_to_sex.get(title, None)
        if expected_sex is None:
            row.append('Unknown')
        else:
            row.append('Yes' if expected_sex == sex else 'No')

    return headers, data

def load_data(file_path):
    """
    Funcție pentru încărcarea datelor dintr-un fișier CSV.
    """
    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        headers = lines[0].strip().split(',')
        for line in lines[1:]:
            values = line.strip().split(',')
            data.append(values)
    return headers, data

def write_result_to_file(headers, data, file_path):
    """
    Scrie rezultatul într-un fișier.
    """
    with open(file_path, 'w') as file:
        file.write(','.join(headers) + '\n')
        for row in data:
            file.write(','.join(row) + '\n')

# 1. Încărcarea Datelor
file_path = 'train.csv'
headers, data = load_data(file_path)

# 2. Verificarea Titlurilor cu Sexul
headers, data = verify_titles_with_sex(data, headers)

# 3. Scrierea Rezultatului în Fișier
write_result_to_file(headers, data, 'cerinta_9.txt')
