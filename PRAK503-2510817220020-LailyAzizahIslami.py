def maksimal(a, b):
    if a > b:
        return a
    else:
        return b

def minimal(a, b):
    if a < b:
        return a
    else:
        return b

batas = 0
maks = -1000000
minim = 1000000
bilangan = int(input())
nilai = map(int, input().split())

for n in nilai:
    maks = maksimal(maks, n)
    minim = minimal(minim, n)

print(maks, minim)