import random
import copy

# Abschnitt 01: Sortierfunktionen
def bubble_sort(sort_n):
    """
    Bubble Sort: Dieser Algorithmus vergleicht wiederholt benachbarte Elemente
    in der Liste und vertauscht sie, falls sie in der falschen Reihenfolge sind.
    Dies wird fortgesetzt, bis die gesamte Liste sortiert ist.
    """
    n = len(sort_n)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sort_n[j] > sort_n[j + 1]:
                sort_n[j], sort_n[j + 1] = sort_n[j + 1], sort_n[j]

def selection_sort(sort_n):
    """
    Selection Sort: Dieser Algorithmus teilt die Liste in einen sortierten und
    einen unsortierten Teil. In jedem Durchgang wird das kleinste Element im
    unsortierten Teil gefunden und mit dem ersten unsortierten Element getauscht.
    """
    n = len(sort_n)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if sort_n[min_idx] > sort_n[j]:
                min_idx = j
        sort_n[i], sort_n[min_idx] = sort_n[min_idx], sort_n[i]

def insertion_sort(sort_n):
    """
    Insertion Sort: Dieser Algorithmus baut die sortierte Liste schrittweise auf,
    indem jedes neue Element an der richtigen Position in den bereits sortierten
    Teil der Liste eingefügt wird.
    """
    for i in range(1, len(sort_n)):
        key = sort_n[i]
        j = i - 1
        while j >=0 and key < sort_n[j]:
            sort_n[j + 1] = sort_n[j]
            j -= 1
        sort_n[j + 1] = key

# Abschnitt 02: Funktion zum Programmbeenden
def beenden_check():
    """
    Bietet die Möglichkeit, das Programm an jeder Stelle zu beenden.
    Bei Eingabe von 'ja' wird das Programm komplett beendet.
    """
    if input("Möchten Sie das Programm beenden? (ja/nein): ").lower() == "ja":
        print("Programm wird beendet.")
        exit()

# Abschnitt 03: Hauptprogramm
def main():
    while True:
        # Abschnitt 03.1: Eingabe von Zahlenbereich und Anzahl der Elemente
        print("\nGeben Sie den Zahlenbereich und die Anzahl der Elemente ein.")
        try:
            range_num = int(input("Zahlenbereich von 1 bis (inklusive): "))
            item_range = int(input("Anzahl der Elemente: "))
            if range_num < item_range or item_range <= 0:
                raise ValueError
        except ValueError:
            print("Ungültige Eingabe.")
            beenden_check()
            continue

        sort_num = random.sample(range(1, range_num + 1), item_range)
        print(f"Generierte Zahlenliste: {sort_num}")

        # Abschnitt 03.2: Auswahl des Sortieralgorithmus
        while True:
            print("\nWählen Sie einen Sortieralgorithmus. Hier sind die Optionen:")
            print("1. Bubble Sortierung: Ein einfacher Algorithmus, der wiederholt durch die Liste geht und benachbarte Elemente vertauscht. Gut für kleinere Listen.")
            print("2. Selection Sortierung: Sucht schrittweise das kleinste Element aus dem unsortierten Teil der Liste und fügt es an der richtigen Stelle im sortierten Teil ein. Effizient bei kleinen bis mittelgroßen Listen.")
            print("3. Insertion Sortierung: Fügt jedes Element der Liste nacheinander in den bereits sortierten Teil ein. Besonders effizient, wenn die Liste fast sortiert ist.")

            choice = input("Ihre Wahl (1, 2 oder 3): ")
            if choice not in ['1', '2', '3']:
                beenden_check()
                continue

            sorted_arr = copy.deepcopy(sort_num)
            if choice == '1':
                bubble_sort(sorted_arr)
            elif choice == '2':
                selection_sort(sorted_arr)
            elif choice == '3':
                insertion_sort(sorted_arr)

            print(f"Sortierte Liste: {sorted_arr}\n")
            break

if __name__ == "__main__":
    main()