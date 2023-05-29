# Hannah adalah seorang siswa yang ingin mengurutkan daftar nilai ujian siswa di kelasnya
# secara ascending menggunakan Bubble Sort. Berikut adalah daftar nilai ujian siswa di
# kelas Hannad: [78,65,90,82,70]. Bantulah Hannad untuk mengurutkan daftar nilai tersebut
# menggunakan Bubble Sort.

def bSort(NUS):
    n = len(NUS)
    for i in range(n-1):
        for j in range(n-i-1):
            if NUS[j] > NUS[j+1]:
                NUS[j], NUS[j+1] = NUS[j+1], NUS[j]
                
NUS = [78,65,90,82,70]
bSort(NUS)
print("Urutan nilai siswa : ",NUS)