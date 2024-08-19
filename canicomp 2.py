angka = [5, 1, 9, 3, 7]
min, max = angka[0], angka[0]

for num in angka:
    if num < min:
        min = num
    if num > max:
        max = num

print(f"Nilai minimum: {min}, Nilai maksimum: {max}")
