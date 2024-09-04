numbersList = []

for c in range(5):
    numbers = float(input('Informe um numero: '))
    numbersList.append(numbers)

print(list(map(lambda x : x ** 2, numbersList)))