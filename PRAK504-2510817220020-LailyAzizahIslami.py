def reverse(n):
    hasil = 0

    while (n != 0):
        hasil = hasil * 10 + (n % 10)
        n //= 10
    return hasil

a, b, = map(int , input().split())

a = reverse(a)
b = reverse(b)
c = a + b
d = reverse(c)
print(d)