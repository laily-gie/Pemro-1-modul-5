def titik (nilai1 , nilai2):
    hasil = nilai1 - nilai2
    return abs(hasil)
    
a, b, c, d = map(int , input().split())

hasil = titik(a, c) + titik(b, d)
print(abs(hasil)); 