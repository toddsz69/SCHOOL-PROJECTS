from statistics import mean, mode, median
def x(data):
    rata2 = mean(data)
    
    mediand= median(data)

    try:
        modusd = mode(data)
    except:
        modusd = "Modus hanya 1"
    
    return rata2, mediand, modusd

data = [1, 1, 1,  2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6]

rata2, mediand, modusd = x(data)

print(f"Data: {data}")
print(f"Rata-rata: {rata2}")
print(f"Median: {mediand}")
print(f"Modus: {modusd}")