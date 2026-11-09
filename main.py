cisla = [5, 2, 4, 1]  # Vytvoříme seznam čísel, která chceme seřadit

def selection_sort(cisla):  # Vytvoříme funkci pro řazení čísel
    n = len(cisla)  # Zjistíme počet čísel v seznamu

    for i in range(n-1):  # Vnější cyklus určuje pozici, kam vložíme nejmenší číslo
        min_index = i  # Předpokládáme, že číslo na aktuální pozici je nejmenší

        for j in range(i+1, n):  # Vnitřní cyklus prochází zbytek seznamu
            if cisla[j] < cisla[min_index]:  # Zjišťujeme, jestli jsme našli menší číslo
                min_index = j  # Uložíme pozici nového nejmenšího čísla

        min_value = cisla.pop(min_index)  # Odstraníme nejmenší číslo a uložíme si ho
        cisla.insert(i, min_value)  # Vložíme nejmenší číslo na správnou pozici

    return print(cisla)  # Vypíšeme seřazený seznam

selection_sort(cisla)  # Zavoláme funkci, aby se řazení spustilo