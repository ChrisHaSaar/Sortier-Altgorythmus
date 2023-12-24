Python Sortieralgorithmen
Dieses Python-Programm demonstriert die Implementierung und Anwendung von drei grundlegenden Sortieralgorithmen: Bubble Sort, Selection Sort und Insertion Sort. Es bietet eine interaktive Benutzeroberfläche, um eine Liste von Zufallszahlen zu generieren und diese mit einem der ausgewählten Algorithmen zu sortieren.

Sortieralgorithmen
1. Bubble Sort
Funktionsweise:
Bubble Sort ist ein einfacher Sortieralgorithmus, der wiederholt durch die Liste geht und benachbarte Elemente vertauscht, wenn sie in der falschen Reihenfolge sind. Der Prozess wird wiederholt, bis keine Vertauschungen mehr erforderlich sind, was bedeutet, dass die Liste sortiert ist.

Beispiel:
Gegeben sei die Liste [5, 3, 8, 4, 2]. Bubble Sort vergleicht zuerst 5 und 3 und vertauscht sie, da 5 > 3. Dann vergleicht es 5 mit 8, macht keine Änderung, und so weiter. Nach dem ersten Durchgang sieht die Liste so aus: [3, 5, 4, 2, 8]. Der Vorgang wird wiederholt, bis die Liste vollständig sortiert ist.

2. Selection Sort
Funktionsweise:
Selection Sort ist ein Algorithmus, der die Liste in zwei Teile teilt: einen sortierten und einen unsortierten. In jedem Durchgang wählt er das kleinste Element aus dem unsortierten Teil und verschiebt es ans Ende des sortierten Teils.

Beispiel:
Betrachten Sie die Liste [29, 10, 14, 37, 13]. Im ersten Durchgang findet Selection Sort das kleinste Element (10) und vertauscht es mit dem ersten Element (29). Die Liste sieht nun so aus: [10, 29, 14, 37, 13]. Der Prozess wird wiederholt, bis die gesamte Liste sortiert ist.

3. Insertion Sort
Funktionsweise:
Insertion Sort baut die sortierte Liste schrittweise auf, indem jedes neue Element an der korrekten Position in den bereits sortierten Teil eingefügt wird.

Beispiel:
Für die Liste [22, 27, 16, 2, 18, 6] beginnt Insertion Sort mit dem zweiten Element (27) und vergleicht es rückwärts mit den vorherigen Elementen. In jedem Schritt wird das Element in den bereits sortierten Teil eingefügt, bis die gesamte Liste sortiert ist.

Hauptprogramm
Das Hauptprogramm ermöglicht es dem Benutzer, eine Anzahl von Elementen und einen Bereich für Zufallszahlen anzugeben. Diese Zahlen werden dann in einer Liste generiert. Der Benutzer kann anschließend einen der drei Sortieralgorithmen auswählen, um die Liste zu sortieren. Nach der Auswahl des Algorithmus zeigt das Programm die sortierte Liste an.

Nutzung
Führen Sie das Programm aus und geben Sie die gewünschte Anzahl von Elementen und den Zahlenbereich ein.
Wählen Sie einen der Sortieralgorithmen aus dem Menü aus.
Betrachten Sie die sortierte Liste.

Anforderungen
Das Programm benötigt Python 3.x. Es werden keine externen Bibliotheken verwendet, abgesehen von random und copy, die in der Standardbibliothek von Python enthalten sind.