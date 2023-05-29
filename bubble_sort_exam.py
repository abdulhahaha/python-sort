def bubble_sort(nilai_siswa):
    n = len(nilai_siswa)
    for i in range(n-1):
        for j in range (n-i-1):
            if nilai_siswa[j] > nilai_siswa[j+1]:
                nilai_siswa[j], nilai_siswa[j+1] = nilai_siswa[j+1], nilai_siswa[j]
    return nilai_siswa

nilai_siswa = [78, 65, 90, 82, 70]
hasil = bubble_sort(nilai_siswa)
print("Daftar nilai setelah diurutkan secara ascending:", hasil)