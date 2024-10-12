import csv
from collections import Counter

# Lista cu vocale și consoane în funcție de frecvență
vocale = "eaâiăoîu".upper()
consoane = "rstnlcdpmvzgfhbșț".upper()

# Funcție pentru a verifica dacă cuvântul este complet ghicit
def este_cuvant_complet(cuvant_partial):
    return '*' not in cuvant_partial

# Funcție pentru a calcula frecvența literelor în cuvântul complet
def calculeaza_frecventa_litere(cuvant_complet):
    # Folosim Counter pentru a număra frecvențele literelor
    return Counter(cuvant_complet)

# Funcție pentru a ghici literele dintr-un cuvânt
def ghiceste_cuvant(cuvant_partial, cuvant_complet, limita_locala):
    incercari = 0
    litere_folosite = set()

    # Calculăm frecvența literelor în cuvântul complet
    frecventa_litere = calculeaza_frecventa_litere(cuvant_complet)

    # Sortăm literele în funcție de frecvență, literele mai frecvente apar primele
    litere_de_ghicit = sorted(frecventa_litere, key=lambda x: (-frecventa_litere[x], x))

    # Buclă pentru ghicirea literelor
    while not este_cuvant_complet(cuvant_partial) and incercari < limita_locala:
        for litera in litere_de_ghicit:
            if litera in litere_folosite:  # Verificăm să nu refolosim literele
                continue

            # Incrementăm numărul de încercări
            incercari += 1

            # Verificăm dacă litera există în cuvântul complet
            if litera in cuvant_complet:
                litere_folosite.add(litera)
                # Actualizăm cuvântul parțial pentru a include literele ghicite
                cuvant_partial = "".join([litera if cuvant_complet[i] == litera else cuvant_partial[i] for i in range(len(cuvant_complet))])
                # Afișăm mesajul că litera a fost ghicită corect
                print(f'Încercare {incercari}: {cuvant_partial} (ghicit: {litera})')
            else:
                # Afișăm mesajul că litera nu a fost ghicită
                print(f'Încercare {incercari}: {cuvant_partial} (neghicit: {litera})')

            # Dacă cuvântul este complet, ne oprim
            if este_cuvant_complet(cuvant_partial):
                break

    return cuvant_partial, incercari

# Funcție pentru a procesa fișierul CSV
def proceseaza_fisierul(fisier):
    total_incercari = 0
    limita_locala = 1200  # Limita locală pentru toate cuvintele

    with open(fisier, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')

        for row in reader:
            cod, cuvant_partial, cuvant_complet = row
            print(f'Procesăm cuvântul: {cuvant_partial} -> {cuvant_complet}')  # Verificăm ce cuvânt este procesat

            # Apelăm funcția de ghicire pentru fiecare cuvânt
            cuvant_final, incercari = ghiceste_cuvant(cuvant_partial, cuvant_complet, limita_locala)

            # Afișăm rezultatele pentru fiecare cuvânt
            print(f'{cod}; {cuvant_final}; {cuvant_complet}; Număr încercări: {incercari}')

            # Adăugăm încercările la totalul general
            total_incercari += incercari

    # Afișăm suma totală a încercărilor
    print(f'Suma totală a încercărilor: {total_incercari}')

# Calea către fișierul de intrare
fisier = "cuvinte.csv"

# Apelăm funcția principală
proceseaza_fisierul(fisier)
