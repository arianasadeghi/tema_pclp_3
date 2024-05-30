import matplotlib.pyplot as plt

def analyze_passenger_data(file_path, output_file):
    # Initializam variabilele pentru calculul statisticilor
    total_passengers = 0
    survived_passengers = 0
    not_survived_passengers = 0
    class_counts = {'1': 0, '2': 0, '3': 0}
    male_passengers = 0
    female_passengers = 0

    # Deschidem fisierul si citim datele
    with open(file_path, "r", encoding='utf-8') as f:
        # Trecem peste antet
        next(f)
        
        # Procesam fiecare linie din fisier
        for line in f:
            # Splituim linia in campuri
            fields = line.strip().split(',')

            # Incrementam numarul total de pasageri
            total_passengers += 1

            # Determinam daca pasagerul a supravietuit sau nu
            if fields[1] == '1':
                survived_passengers += 1
            else:
                not_survived_passengers += 1

            # Determinam clasa pasagerului și actualizam contorul
            class_counts[fields[2]] += 1

            # Determinam sexul pasagerului si actualizam contorul
            if fields[5] == 'male':
                male_passengers += 1
            elif fields[5] == 'female':
                female_passengers += 1

    # Calculam procentele
    survival_percentage = (survived_passengers / total_passengers) * 100
    not_survival_percentage = (not_survived_passengers / total_passengers) * 100
    class_percentages = {cls: (count / total_passengers) * 100 for cls, count in class_counts.items()}
    male_percentage = (male_passengers / total_passengers) * 100
    female_percentage = (female_passengers / total_passengers) * 100

    # Salvam rezultatele in fisierul specificat
    with open(output_file, 'w') as output:
        output.write(f"Procentul persoanelor care au supravietuit: {survival_percentage:.2f}%\n")
        output.write(f"Procentul persoanelor care nu au supravietuit: {not_survival_percentage:.2f}%\n")
        output.write("Procentul pasagerilor pentru fiecare clasa:\n")
        for cls, percentage in class_percentages.items():
            output.write(f"  Clasa {cls}: {percentage:.2f}%\n")
        output.write(f"Procentul barbatilor: {male_percentage:.2f}%\n")
        output.write(f"Procentul femeilor: {female_percentage:.2f}%\n")

    # Cream un grafic pentru vizualizarea procentelor si salvam imaginile
    labels = ['Survived', 'Not Survived']
    sizes = [survival_percentage, not_survival_percentage]
    # Separatia pentru primul slice
    explode = (0.1, 0)
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    # Face ca pie chart-ul sa fie circular
    plt.axis('equal')
    plt.title('Survival Percentage')
    plt.savefig('survival_percentage.png')
    plt.close()

    labels = ['Class 1', 'Class 2', 'Class 3']
    sizes = [class_percentages['1'], class_percentages['2'], class_percentages['3']]
    # Separatia pentru primul slice
    explode = (0.1, 0, 0)
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    # Face ca pie chart-ul sa fie circular
    plt.axis('equal')
    plt.title('Passenger Class Percentage')
    plt.savefig('passenger_class_percentage.png')
    plt.close()

    labels = ['Male', 'Female']
    sizes = [male_percentage, female_percentage]
    # Separatia pentru primul slice
    explode = (0.1, 0)
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    # Face ca pie chart-ul sa fie circular
    plt.axis('equal')
    plt.title('Gender Percentage')
    plt.savefig('gender_percentage.png')
    plt.close()

# Apelarea functiei cu calea catre fisierul de date si fisierul de iesire
analyze_passenger_data('train.csv', 'cerinta_2.txt')
