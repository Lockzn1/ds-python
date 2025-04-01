# Ex 1

count = 0
while count <= 10:
    print(count)
    count += 1


# Ex 2

for n1 in [8,7,17,25,38]:
    print(n1)

seq = [3,57,67,22,8]
for n2 in seq:
    print(n2)


# Ex 3

for num in range(1000):
    print(num)
    if num == 100:
        break
        continue
    print("Finalizado")


# Ex 4

for x in [1, 10, 20, 30, 40, 50, 60]:
    if x == 30:

        continue
    print(x)


# Ex 5 -> Range Inicio | Fim | Salto

for numero in range (20, 30, 2):
    print(numero)


# Ex 6 -> Lista

lista = [1, 3, 5, 7, 9, 10]
print(lista[4])


# Ex 7 -> Lista

lista = [1, 3, 5], [7, 9, 10]
print(lista[0][1])


# Ex 8 -> Adicionar um item ao final da linha

x = [1, 3, 5, 'victor']

x.append('Luiz')
print(x)