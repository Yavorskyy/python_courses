__author__ = 'andriy'
# triples
n =100
count = 0

number = int(raw_input("Enter number of triples:"))

list = []
for i in xrange(1,n):
    for j in xrange(1,n):
        for y in xrange(1,n):
            if ((i**2)+(j**2) == (y**2)) and count < number:
                list.append((i,j,y))
                print list
                count += 1

m = len(list)
print type(m)
while b < m:
...     print b
...     a, b = list[i], a+b
