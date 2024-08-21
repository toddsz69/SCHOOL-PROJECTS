def main():
    input_str = input("Masukkan angka: ")
    angka = list(map(int, input_str.split()))

    sorted_kecilbesar = sorted(angka)
    print(f"Urutan dari kecil ke besar: {sorted_kecilbesar}")

    sorted_besarkecil = sorted(angka, reverse=True)
    print(f"Urutan dari besar ke kecil: {sorted_besarkecil}")

if __name__ == "__main__":
    main()
