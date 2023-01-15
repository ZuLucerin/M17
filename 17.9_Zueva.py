sp = input("Введите последовательность чисел через пробел: ")
sp_list = [int(a) for a in sp.split()]

num = int(input("Введите число: "))
if num % 1 == 0:
    sp_list.append(num)
    print("Список до сортировки: ", sp_list)

def my_sort(sp_list):
    for i in range(len(sp_list)):  # проходим по всему массиву
        idx_min = i  # сохраняем индекс предположительно минимального элемента
        for j in range(i, len(sp_list)):
            if sp_list[j] < sp_list[idx_min]:
                idx_min = j
        if i != idx_min:  # если индекс не совпадает с минимальным, меняем
            sp_list[i], sp_list[idx_min] = sp_list[idx_min], sp_list[i]
    return sp_list

print("Список после сортировки:", my_sort(sp_list))