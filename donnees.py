import csv
import random

# Générer les données aléatoires
tab=[random.randint(1, 100) for _ in range(10000)]
tab_sorted = sorted(tab)
tab2=[random.uniform(20, 2) for _ in range(10000)]
tab2_sorted = sorted(tab2)
#data = [(random.randint(1, 100), random.uniform(10, 2)) for _ in range(5000)]
#data_sorted = sorted(data, key=lambda x: x[0])
#data_sorted = sorted(data, key=lambda x: (x[0], x[1]))
data = list(zip(tab_sorted, tab2_sorted))
# Écrire les données dans un fichier CSV
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Quantite', 'Prix'])
    for row in data:
        writer.writerow(row)
