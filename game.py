#Program yebak bilangan/angka
#Dari 1 sampai 10
#Pemograman Kent
#Kelas 10.4/24

import random

pencacah_utama = [] #ada list dengan nama pencacah_utama
pencacah = [] #ada list dengan nama pencacah
print("Tebak Bilangan")

def GameMultiPemain(pemain):
    global pencacah
    pencacah = 0
    n = random.randint(1,10)
    print(f"\n{pemain} giliranmu")
    while True:
        usr = int(input("Masukkan bilangan tebakanmu:"))
        pencacah += 1
        if n ==usr:
            print("Selamat "
                  f"{pemain}, tebakanmu benar"
                  f"tebakan tepat")
            print(f"{pemain}"
                  f"skor: {pencacah}")
            break
        elif n>usr:
            print("tebaklah bilangan yang lebih besar")
        elif n<usr:
            print("tebaklah bilangan yang lebih kecil")
        else:
            print("terjadi kesalahan")
        pencacah_utama.append(pencacah)

if __name__=='__main__':
    pemain1 = input("Masukkan nama Pemain1: ")
    pemain2 = input("Masukkan nama pemain2: ")

    GameMultiPemain(pemain1)
    GameMultiPemain(pemain2)

    if pencacah_utama[0] == pencacah_utama[1]:
        print("Seri/Draw")
    elif pencacah_utama[0] > pencacah_utama[1]:
        print(f"{pemain2} menang")
    else: 
        print(f"{pemain1} menang")
