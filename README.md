# tema_pclp_3

Documentatie
https://www.w3schools.com/python/python_file_open.asp
https://www.w3schools.com/python/python_file_write.asp
https://www.w3schools.com/python/pandas/pandas_series.asp
https://saturncloud.io/blog/5-easy-ways-to-get-pandas-dataframe-row-count/
https://medium.com/@matthewghannoum/pandas-basics-everything-you-need-to-know-for-90-of-your-projects-972a964a1377
https://www.geeksforgeeks.org/introduction-to-python/
https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
https://www.practicaldatascience.org/notebooks/class_5/week_5/46_making_plots_pretty.html
https://www.geeksforgeeks.org/plotting-histogram-in-python-using-matplotlib/


Implementare

Pentru cerintele 1, 3 si 4 am ales sa folosesc libraria pandas, pentru a ma asigura
ca datele din fisier sunt luate corect, initial am incercat sa parcurg fisierul
cu ajutorul for-urilor, dar existau niste erori in modul in care erau
prelucrate coloanele si datele de pe acestea.

Cerinta_1
Pentru a realiza analiza initiala a setului de date, am efectuat urmatoarele
operatiuni: intai citesc fisierul train.csv, utilizand biblioteca pandas, pe
care o folosesc si pentru a incarca datele intr-un cadru de date. Apoi determin
numarul de coloane din setul de date, am determinat tipul de date din fiecare
coloana, am calculat numarul de valori lipsa din fiecare coloana, observand
faptul ca o valoare lipsa este marcata prin prezenta a doua virgule una dupa
alta. Apoi am stabilit numarul total de linii din setul de date, iar in final,
am verificat daca exista linii duplicate in setul de date.

Cerinta_2
Functia `analyze_passenger_data` este definita pentru a efectua analiza datelor
pasagerilor din setul de date si a genera statistici relevante, precum si
grafice pentru vizualizare. Apoi calculez procentul de pasageri care au
supravietuit si procentul de pasageri care nu au supravietuit, informatii pe
care le salvez in fisierul de iesire. Dupa, calculez procentul de pasageri
pentru fiecare clasa si se salveaza in fisierul de iesire. Calculez procentul
de pasageri de sex masculin si procentul de pasageri de sex feminin si se
salveaza in fisierul de iesire. Cu informatiile generate generez cele trei
grafice cerute.

Cerinta_3
Utilizez din nou biblioteca Pandas si citesc fisierul train.csv care contine
setul de date. Apoi selectez doar coloanele numerice din setul de date pentru
a genera histograma pentru fiecare dintre acestea. Cu datele extrase generez
histograme utilizand functia plt.hist() din biblioteca Matplotlib.

Cerinta_4
Am folosit biblioteca pandas pentru a citi corect datele din fisierul train.csv
cu ajutorul functiei read_csv, care pe langa citirea fisierului, incarca si
datele intr-un obiect DataFrame numit df. Apoi, identific coloanele care contin
cel putin o valoare lipsa, apoi folosind tolist() am convertit coloanele
identificate intr-o lista. Parcurg fiecare coloana cu valori lipsa identificata
anterior, iar pentru fiecare coloana calculez numarul de valori lipsa si
procentul acestora in raport cu numarul total de randuri si mai calculez si
procentul de valori lipsa pentru fiecare clasa in coloana "Survived".

Cerinta_5
Deschid fisierul si citesc fiecare linie, extrag antetul si parcurg
liniile dupa antet, apoi separ valorile din fiecare linie si le adaug intr-o
lista de date, returnand antetul si datele intr-un tuplu. Adaug o coloana
suplimentara care indica categoria de varsta, corespunzatoare in functie de
varsta pasagerului si adauga categoria de varsta in randul curent si
actualizeaza antetul. Pe baza rezultatelor generez un grafic care evidentiaza
distributia categoriilor de varsta.

Cerinta_6
Inceputul acestei cerinte este similar cu cel al cerintei anterioare, dupa
extragerea datelor, numar barbatii supravietuitori in fiecare categorie de
varsta, si actualizez un dictionar care stocheaza numarul de barbati
supravietuitori in fiecare categorie de varsta, iar in urma rezultatelor date
realizez graficul cerut.

Cerinta_7
Calculez rata de supravietuire pentru copii si adulti, parcurgand datele si
verificand varsta si daca a supravietuit. Calculez numarul total de copii si
adulti si numarul de copii si adulti care au supravietuit, apoi calculez rata
de supravietuire pentru copii si adulti si returnez ratele de supravietuire
pentru copii si adulti. Pe baza datelor aflate creez graficul cerut.

Cerinta_9
Intai extrag titlul din numele unei persoane, parcurg lista de titluri si
verific daca unul dintre acestea se gaseste in numele persoanei, iar in caz
de potrivire returneaza primul titlu gasit sau un sir vid in caz contrar.
Verific daca titlurile corespund sexului persoanelor, definind un dictionar
care asociaza titlurile cu sexul asteptat. Apoi verific daca titlul se
potriveste cu sexul si adaug raspunsul intr-o noua coloana.

