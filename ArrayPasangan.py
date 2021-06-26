daftar = [102, 32, 99, 32, 45, 102, 45, 67, 67, 100, 100]

for i in daftar:
    if daftar.count(i) == 1:
        print("daftar yang tidak berpasangan adalah ",i,"terdapat pada indeks ke :",daftar.index(i)+1)