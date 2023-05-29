def selection_sort(arr):
    n = len(arr)
    for i in range (n-1):
        min_index = i
        for j in range (i+1, n):
            if arr[j][2] > arr[min_index][2]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

footballs = [
    ["Kylian Mbappe", "Paris Saint Germain", 40],
    ["Victor Osimhen", "Napoli", 28],
    ["Robert Lewandowski", "Barcelona", 33],
    ["Erling Haaland", "Manchester City", 52],
    ["Christopher Nkunku", "RB Leipzig", 22]
]
selection_sort(footballs)
print("Daftar Pemain (diurutkan berdasarkan jumlah gol):" )
print("No.  Nama Pemain                                 Klub                          Jumlah Gol")
print("------------------------------------------------------------------------------------------")
for i, football in enumerate(footballs, start=1):
    player, club, goal = football
    print(f"{i:2}.  {player:40}  {club:25} {goal:15}")