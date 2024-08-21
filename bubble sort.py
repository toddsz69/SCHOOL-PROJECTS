def bubble_sort(arr, reverse=False):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if (arr[j] > arr[j+1] and not reverse) or (arr[j] < arr[j+1] and reverse):
                arr[j], arr[j+1] = arr[j+1], arr[j]

def main():
    input_str = input("Masukkan angka: ")
    angka = list(map(int, input_str.split()))

    bubble_sorted_ascending = angka[:]
    bubble_sort(bubble_sorted_ascending)
    print(f"Urutan dari kecil ke besar: {bubble_sorted_ascending}")

    bubble_sorted_descending = angka[:]
    bubble_sort(bubble_sorted_descending, reverse=True)
    print(f"Urutan dari besar ke kecil: {bubble_sorted_descending}")

if __name__ == "__main__":
    main()
