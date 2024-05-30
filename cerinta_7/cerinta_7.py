import matplotlib.pyplot as plt

def calculate_survival_rates(data):
    """
    Functie pentru calcularea ratei de supravietuire pentru copii si adulti.
    """
    children_survived = 0
    children_total = 0
    adults_survived = 0
    adults_total = 0

    for row in data:
        age = row[6]
        survived = row[1]
        
        try:
            age_value = float(age)
            survived_value = int(survived)
            if age_value < 18:
                children_total += 1
                if survived_value == 1:
                    children_survived += 1
            else:
                adults_total += 1
                if survived_value == 1:
                    adults_survived += 1
        except ValueError:
            continue

    children_survival_rate = (children_survived / children_total) * 100 if children_total > 0 else 0
    adults_survival_rate = (adults_survived / adults_total) * 100 if adults_total > 0 else 0

    return children_survival_rate, adults_survival_rate

def load_data(file_path):
    """
    Functie pentru incarcarea datelor dintr-un fisier CSV.
    """
    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        headers = lines[0].strip().split(',')
        for line in lines[1:]:
            values = line.strip().split(',')
            data.append(values)
    return headers, data

def plot_survival_rates(children_survival_rate, adults_survival_rate):
    """
    Functie pentru crearea unui grafic care sa evidentieze rata de supravietuire pentru copii si adulti.
    """
    categories = ['Copii', 'Adulti']
    survival_rates = [children_survival_rate, adults_survival_rate]

    plt.bar(categories, survival_rates, color=['blue', 'green'])
    plt.xlabel('Categorie')
    plt.ylabel('Rata de supravietuire (%)')
    plt.title('Rata de supravietuire pentru copii si adulti')
    plt.ylim(0, 100)
    plt.savefig('survival_rates.png')
    plt.close()

# 1. Incarcarea datelor
file_path = 'train.csv'
headers, data = load_data(file_path)

# 2. Calcularea ratei de supravietuire
children_survival_rate, adults_survival_rate = calculate_survival_rates(data)

# 3. Crearea graficului
plot_survival_rates(children_survival_rate, adults_survival_rate)

