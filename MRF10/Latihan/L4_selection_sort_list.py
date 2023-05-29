# Andi memiliki sebuah daftar angka yang ingin diurutkan secara ascending menggunakan
# Selection Sort. Berikut adalah daftar angka yang dimiliki Andi: [9,5,3,8,2]. Bantulah
# Andi untuk mengurutkan daftar angka tersebut menggunakan Selection Sort

def sSort(daftarAngka):
    n = len(daftarAngka)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if daftarAngka[j] < daftarAngka[min_index]:
                min_index = j
        daftarAngka[i], daftarAngka[min_index] = daftarAngka[min_index], daftarAngka[i]
                
daftarAngka = [9,5,3,8,2]
sSort(daftarAngka)
print("Hasil daftar angka berurutan : ",daftarAngka)