# Ahmad ingin mengurutkan daftar angka secara descending menggunakan Bubble Sort. Berikut
# adalah daftar angka yang ingin diurutkan: [42,19,33,8,55]. Bantulah Ahmad untuk mengurutkan
# daftar angka tersebut secara descending menggunakan Bubble Sort.

def bSort(daftarAngka):
    n = len(daftarAngka)
    for i in range(n-1):
        for j in range(n-i-1):
            if daftarAngka[j] < daftarAngka[j+1]:
                daftarAngka[j], daftarAngka[j+1] = daftarAngka[j+1], daftarAngka[j]
                
daftarAngka = [42,19,33,8,55]
bSort(daftarAngka)
print("Hasil pengurutan : ",daftarAngka)