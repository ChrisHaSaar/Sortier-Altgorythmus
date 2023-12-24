import random
import copy

def bubble_sort(count, sort_n):
    bubble = True
    for i in range(len(sort_n) - 1):
        if sort_n[i] > sort_n[i + 1]:
            sort_n[i + 1], sort_n[i] = sort_n[i], sort_n[i + 1]
            bubble = False
            print(f"Sort{count}: {sort_n} \'{sort_n[i + 1]} swap {sort_n[i]}\'")
            count += 1
    if bubble == False:
        bubble_sort(count, sort_n)
            
def selection_sort(count, sort_n):
    for i in range(len(sort_n) - 1):
        compare_num = sort_n[i]
        num = 1
        n_sort = 0
        while (i + num) < len(sort_n):
            if compare_num > sort_n[i + num]:
                compare_num = sort_n[i + num]
                n_sort = (i + num)
            num += 1
        if n_sort != 0:
            sort_n[n_sort], sort_n[i] = sort_n[i], sort_n[n_sort]
            print(f"Sort{count}: {sort_n} \'{sort_n[n_sort]} swap {sort_n[i]}\'")
            count += 1
        
        
def insertion_sort(count, sort_n):
    i = 1
    n_loop = 0
    while i < len(sort_n):
        j = 0
        point = 0
        while j <= n_loop:
            if point > 0:
                if sort_n[i] > sort_n[i - (j + 1)]:
                    name_insert = sort_n[i]
                    del sort_n[i]
                    sort_n.insert((i - j), name_insert)
                    print(f"Sort{count}: {sort_n} \'Insert {name_insert} after {sort_n[i - (j - 1)]}\'")
                    count += 1
                    break
            if sort_n[i] < sort_n[i - (j + 1)]:
                if j == point and j == n_loop:
                    name_insert = sort_n[i]
                    del sort_n[i]
                    sort_n.insert(0, name_insert)
                    print(f"Sort{count}: {sort_n} \'Insert {name_insert} to 1st\'")
                    count += 1
                    break
                point += 1
            j += 1                          
        n_loop += 1
        i += 1


while True:
    sort_num = []
    try:
        range_num = int(input("Enter Range 1 to "))
        item_range = int(input("How many Item: "))
    except Exception as e:
        continue
    
    print()
    if range_num < item_range:
        print("Item must less than Range.\n")
        continue
        #exit()  
    num_one = 1
    while num_one <= item_range:
        num_one += 1
        pick_num = random.randint(1, range_num)
        if pick_num in sort_num:
            num_one -= 1
            continue     
        sort_num.append(pick_num)
     
    print(f"Array: {sort_num}")
       
    while True:
        c_sort = copy.deepcopy(sort_num)
        print('''\n=================================
||  Sorting Algorithms:        ||
||      1. Bubble Sort         ||
||      2. Selection Sort      ||
||      3. Insertion Sort      ||
=================================''')
                
        input_sort = input("Choose Sort: ")
     
        if input_sort == "1":
            print()
            print("\t\"BUBBLE SORT\"\n")
            print(f" Orig: {sort_num}")
            bubble_sort(1, c_sort)
            print("\nDone")
        elif input_sort == "2":
            print()
            print("\t\"SELECTION SORT\"\n")
            print(f" Orig: {sort_num}")
            selection_sort(1, c_sort)
            print("\nDone")
        elif input_sort == "3":
            print()
            print("\t\"INSERTION SORT\"\n")
            print(f" Orig: {sort_num}")
            insertion_sort(1, c_sort)
            print("\nDone")
        else:
            print()
            break
            
        print()
        #sort_num.clear()
       
    
    