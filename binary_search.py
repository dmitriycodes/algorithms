lst_in = list(range(1, 11))


def find_el(lst, find_el):
    index = -1
    count_operation = 0
    for el, idx in enumerate(lst):
        count_operation += 1
        if el == find_el:
            index = idx
            break
    return index, count_operation




def binary_search(lst, find_el):
    low = 0
    hight = len(lst) - 1
    counter = 0

    while low <= hight:
        mid = (low + hight) // 2
        guess = lst[mid]
        counter += 1
        if guess == find_el:
            return mid, counter
        elif guess < find_el:
            low = mid + 1
        else:
            hight = mid - 1

    return None, counter


# print("usuall searhc", find_el(lst_in, 50))
print("binary", binary_search(lst_in, -5))

