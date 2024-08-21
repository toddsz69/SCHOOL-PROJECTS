def selection_sort(arr, reverse=False):
    n = len(arr)
    for i in range(n):
        index_extreme = i
        for j in range(i+1, n):
            if (arr[j] < arr[index_extreme] and not reverse) or (arr[j] > arr[index_extreme] and reverse):
                index_extreme = j
        arr[i], arr[index_extreme] = arr[index_extreme], arr[i]

def main():
    input_str = input("Masukkan angka: ")
    angka = list(map(int, input_str.split()))

    selection_sorted_ascending = angka[:]
    selection_sort(selection_sorted_ascending)
    print(f"Urutan dari kecil ke besar: {selection_sorted_ascending}")

    selection_sorted_descending = angka[:]
    selection_sort(selection_sorted_descending, reverse=True)
    print(f"Urutan dari besar ke kecil: {selection_sorted_descending}")

if __name__ == "__main__":
    main()
