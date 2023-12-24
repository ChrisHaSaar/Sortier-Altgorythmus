import random
import copy

# Abschnitt 1: Bubble Sort
def bubble_sort(sort_n):
    n = len(sort_n)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if sort_n[j] > sort_n[j + 1]:
                sort_n[j], sort_n[j + 1] = sort_n[j + 1], sort_n[j]

# Abschnitt 2: Selection Sort
def selection_sort(sort_n):
    for i in range(len(sort_n)):
        min_idx = i
        for j in range(i+1, len(sort_n)):
            if sort_n[min_idx] > sort_n[j]:
                min_idx = j
        sort_n[i], sort_n[min_idx] = sort_n[min_idx], sort_n[i]

# Abschnitt 3: Insertion Sort
def insertion_sort(sort_n):
    for i in range(1, len(sort_n)):
        key = sort_n[i]
        j = i-1
        while j >=0 and key < sort_n[j]:
            sort_n[j + 1] = sort_n[j]
            j -= 1
        sort_n[j + 1] = key

# Abschnitt 4: Hauptprogramm
def main():
    while True:
        try:
            range_num = int(input("Enter Range 1 to: "))
            item_range = int(input("How many Items: "))
            if range_num < item_range or item_range <= 0:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter positive integers with range greater than item count.")
            continue

        sort_num = random.sample(range(1, range_num + 1), item_range)
        print(f"Original Array: {sort_num}")

        algorithms = {'1': bubble_sort, '2': selection_sort, '3': insertion_sort}
        while True:
            print('''\nChoose Sorting Algorithm:
1. Bubble Sort
2. Selection Sort
3. Insertion Sort
Enter any other key to exit''')

            choice = input("Your choice: ")
            if choice in algorithms:
                sorted_arr = copy.deepcopy(sort_num)
                algorithms[choice](sorted_arr)
                print(f"Sorted Array: {sorted_arr}\n")
            else:
                break

if __name__ == "__main__":
    main()
