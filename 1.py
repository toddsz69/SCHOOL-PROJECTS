def palindromcheck(x):
    i = ''.join(x.split()).lower()
    l = i[::-1]
    
    if i == i[::-1]:
        print(f"{x} Kalimat Palindrom")
        print(f"Dibalik dengan case sensitive: {l}")
    else:
        print(f"{x} Bukan Kalimat Palindrom")

palindromcheck("Radar")
