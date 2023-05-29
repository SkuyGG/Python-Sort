# Berdasakan statistik sepak bola musim 2022/2023, terdapat daftar pemain yang perlu
# diurutkan berdasarkan jumlah gol yang dicetak secara descending menggunakan Selection Sort.
# Setiap pemain memiliki informasi berikut: nama pemain, klub pemain, dan jumlah gol yang
# dicetak. Berikut adalah daftar pemain yang perlu diurutkan:

# NO        Nama Pemain             Klub                            Jumlah Gol
# 1.        Kylian Mbappe           Paris Saint Germain             40
# 2.        Victor Osimhen          Napoli                          28
# 3.        Robert Lewandowski      Barcelona                       33
# 4.        Erling Haaland          Manchester City                 52
# 5.        Christopher Nkunku      RB Leipzig                      22



def sSort(daftarPemain):
    n = len(daftarPemain)
    for i in range(n-1):
        
        max_index = i
        for j in range(i+1, n):
            if daftarPemain[j]["Jumlah Gol"] > daftarPemain[max_index]["Jumlah Gol"]:
                max_index = j

        
        daftarPemain[i], daftarPemain[max_index] = daftarPemain[max_index], daftarPemain[i]

    return daftarPemain
        
daftarPemain = [
    {"No.": 1, "Nama Pemain": "Kylian Mbappe", "Klub": "Paris Saint Germain", "Jumlah Gol": 40},
    {"No.": 2, "Nama Pemain": "Victor Osimhen", "Klub": "Napoli", "Jumlah Gol": 28},
    {"No.": 3, "Nama Pemain": "Robert Lewandowski", "Klub": "Barcelona", "Jumlah Gol": 33},
    {"No.": 4, "Nama Pemain": "Erling Haaland", "Klub": " ", "Jumlah Gol": 52},
    {"No.": 5, "Nama Pemain": "Christopher Nkunku", "Klub": "RB Leipzig", "Jumlah Gol": 22},
]

print("Daftar pemain terurut berdasarkan jumlah gol:")
for pemain in daftarPemain:
    print("No.:", pemain["No."])
    print("Nama Pemain:", pemain["Nama Pemain"])
    print("Klub:", pemain["Klub"])
    print("Jumlah Gol:", pemain["Jumlah Gol"])
    print()