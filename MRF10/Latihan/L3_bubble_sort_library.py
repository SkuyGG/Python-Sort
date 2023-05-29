# Di suatu perpustakaan, terdapat daftar buku yang perlu diurutkan berdasarkan jumlah
# halaman secara ascending menggunakan Bubble Sort. Setiap buku memiliki informasi berikut:
# Judul buku, Penulis, dan Jumlah halaman. Berikut adalah daftar buku yang perlu diurutkan:

# NO        Judul Buku                                  Penulis                 Jumlah Halaman
# 1.        Harry Potter and the Sorcerer's Stone       J.K Rowing              320
# 2.        To Kill a Mockingbird                       Harper Lee              281
# 3.        The Great Gatsby                            F. Scott Fitzgerald     180
# 4.        Pride and Prejudice                         Jane Austen             432
# 5.        1984                                        George Orwell           328

def bSort(perpus):
    n = len(perpus)
    for i in range(n-1):
        for j in range(n-i-1):
            if perpus[j][2] > perpus[j+1][2]:
                perpus[j], perpus[j+1] = perpus[j+1], perpus[j]
                
perpus = [["Harry Potter and the Sorcerer's Stone","J.K Rowing",320],["To Kill a Mockingbird","Harper Lee",281],["The Great Gatsby","F. Scott Fitzgerald",180],["Pride and Prejudice","Jane Austen",432],["1984","George Orwell",328]]
bSort(perpus)
print("Urutan daftar buku diperpustakaan : ",perpus)