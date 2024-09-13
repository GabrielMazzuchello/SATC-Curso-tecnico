""". Escreva um programa que receba uma lista de temperaturas em Celsius e, utilizando a função
map() com uma expressão lambda, retorne uma nova lista com as temperaturas convertidas para
Fahrenheit. A fórmula para converter Celsius para Fahrenheit é: (C * 1.8) + 32."""

listaNumeros = []

for c in range(5):
    num = float(input('Informe a temperatura em °C: '))
    listaNumeros.append(num)

listaFahrenheit = list(map(lambda x : (x * 1.8) + 32,  listaNumeros))
print(listaFahrenheit)