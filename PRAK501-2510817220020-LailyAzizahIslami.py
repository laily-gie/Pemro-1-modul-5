def maxBilangan (a, b, c, d):

    maxBilangan = a

    if b > maxBilangan:
        maxBilangan = b
    if c > maxBilangan:
        maxBilangan = c
    if d > maxBilangan:
        maxBilangan = d
    return maxBilangan

a, b, c, d = map(int , input().split())
hasil = maxBilangan (a, b, c, d)

print("" , hasil)