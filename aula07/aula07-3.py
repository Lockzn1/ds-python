import statistics
lista=[1,2,3,4,5]
media = statistics.mean(lista)
print("A média é igul a", media)

def soma(n1, n2):
    resultado = n1 + n2
    return resultado

num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))

s = soma(num1, num2)
print("A soma é igual a: ",s)

dic = {'colher': 10, 'garfo': 9.5, 'faca': 12.7}
print(dic['garfo'])
