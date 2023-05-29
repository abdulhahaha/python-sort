def bubble_sort(books):
    n = len(books)
    for i in range(n-1):
        for j in range (n-i-1):
            if books[j][2] > books[j+1][2]:
                books[j], books[j+1] = books[j+1], books[j]

books = [
    ["Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 320],
    ["To a Mockingbird", "Harper Lee", 281],
    ["The Great Gatsby", "F. Scott Fitzgerald", 432],
    ["Pride and Prejudice", "Jane Austen", 180],
    ["1984", "George Orwell", 328]
]
bubble_sort(books)
print("Daftar Buku (diurutkan berdasarkan jumlah halaman):" )
print("No.  Judul Buku                                 Penulis                          Jumlah Halaman")
print("-----------------------------------------------------------------------------------------------")
for i, book in enumerate(books, start=1):
    title, author, pages = book
    print(f"{i:2}.  {title:40}  {author:25} {pages:15}")