cisla = [5, 2, 4, 1]

def selection_sort(cisla):
    n = len(cisla)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if cisla[j] < cisla[min_index]:
                min_index = j
        min_value = cisla.pop(min_index)
        cisla.insert(i, min_value)
        
    return print(cisla)

selection_sort(cisla)