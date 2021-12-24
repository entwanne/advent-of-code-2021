w, x, y, z = 0, 0, 0, 0
s = [0] * 14

w = s.pop(0)
x = 1
y = z = w + 8

w = s.pop(0)
x = 1
y = w + 13
z = z*26 + y

w = s.pop(0)
x = 1
y = w + 2
z = z * 26 + y

w = s.pop(0)
x = z % 26
z = z // 26
if x != w:
    x = 1
    y = w + 7
    z = z * 26 + y

w = s.pop(0)
x = z % 26 + 12
if x != w:
    x = 1
    y = w + 11
    z = z * 26 + y

w = s.pop(0)
x = z % 26 + 12
x = int(x == w)
x = int(x == 0)
if x != w:
    x = 1
    y = w + 4
    z = z * 26 + y

w = s.pop(0)
x = z % 26 + 12
if x != w:
    x = 1
    y = w + 13
    z = z * 26 + y

w = s.pop(0)
x = int(x * 0)
x = int(x + z)
x = int(x % 26)
z = int(z // 26)
x = int(x + -8)
x = int(x == w)
x = int(x == 0)
y = int(y * 0)
y = int(y + 25)
y = int(y * x)
y = int(y + 1)
z = int(z * y)
y = int(y * 0)
y = int(y + w)
y = int(y + 13)
y = int(y * x)
z = int(z + y)

w = s.pop(0)
x = int(x * 0)
x = int(x + z)
x = int(x % 26)
z = int(z // 26)
x = int(x + -9)
x = int(x == w)
x = int(x == 0)
y = int(y * 0)
y = int(y + 25)
y = int(y * x)
y = int(y + 1)
z = int(z * y)
y = int(y * 0)
y = int(y + w)
y = int(y + 10)
y = int(y * x)
z = int(z + y)

w = s.pop(0)
x = int(x * 0)
x = int(x + z)
x = int(x % 26)
z = int(z // 1)
x = int(x + 11)
x = int(x == w)
x = int(x == 0)
y = int(y * 0)
y = int(y + 25)
y = int(y * x)
y = int(y + 1)
z = int(z * y)
y = int(y * 0)
y = int(y + w)
y = int(y + 1)
y = int(y * x)
z = int(z + y)

w = s.pop(0)
x = int(x * 0)
x = int(x + z)
x = int(x % 26)
z = int(z // 26)
x = int(x + 0)
x = int(x == w)
x = int(x == 0)
y = int(y * 0)
y = int(y + 25)
y = int(y * x)
y = int(y + 1)
z = int(z * y)
y = int(y * 0)
y = int(y + w)
y = int(y + 2)
y = int(y * x)
z = int(z + y)

w = s.pop(0)
x = int(x * 0)
x = int(x + z)
x = int(x % 26)
z = int(z // 26)
x = int(x + -5)
x = int(x == w)
x = int(x == 0)
y = int(y * 0)
y = int(y + 25)
y = int(y * x)
y = int(y + 1)
z = int(z * y)
y = int(y * 0)
y = int(y + w)
y = int(y + 14)
y = int(y * x)
z = int(z + y)

w = s.pop(0)
x = int(x * 0)
x = int(x + z)
x = int(x % 26)
z = int(z // 26)
x = int(x + -6)
x = int(x == w)
x = int(x == 0)
y = int(y * 0)
y = int(y + 25)
y = int(y * x)
y = int(y + 1)
z = int(z * y)
y = int(y * 0)
y = int(y + w)
y = int(y + 6)
y = int(y * x)
z = int(z + y)

w = s.pop(0)
x = int(x * 0)
x = int(x + z)
x = int(x % 26)
z = int(z // 26)
x = int(x + -12)
x = int(x == w)
x = int(x == 0)
y = int(y * 0)
y = int(y + 25)
y = int(y * x)
y = int(y + 1)
z = int(z * y)
y = int(y * 0)
y = int(y + w)
y = int(y + 14)
y = int(y * x)
z = int(z + y)

print(z)
