from random import randint

data = [randint(1, 20) for _ in xrange(20)]
print(data)
m = max(data)

hhisto = [('o' * i).rjust(m) for i in data]
for line in hhisto:
    print(line)

for line in zip(*hhisto):
    print(''.join(line))

print('hey, hey')
