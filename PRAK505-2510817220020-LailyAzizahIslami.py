def biodata(tahunlahir, A, B):
    tahunsekarang  = 2020
    umur = tahunsekarang - tahunlahir
    angkatan = tahunlahir + 18

    print("\nPerkenalkan Nama Saya       :" , A)
    print("Umur Saya                   :", umur)
    print("Saya Adalah Angkatan        :", angkatan)
    print("Asal Saya dari              :", B)

tahunlahir = int(input())
A = input()
B = input()

biodata(tahunlahir, A, B)