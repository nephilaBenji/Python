print("você quer saber o tamanho do seu sapato pelo tamanho por quantos centimetros ele possui escreva 1, se quiser saber a quantidade de centímentors do deu pé pelo tamanho do sapato escreva 2")
x = input()
if (x == "1"):

    print("Digite a quantos centimetros que tem seu pé")
    x = float(input())
    y = (5 * x + 28) / 4
    print("O tamanho do seu pé é: ", y)
else:
    print("Digite o tamanho do seu sapato")
    x = float(input())
    y = (4 * x - 28) / 5
    print("O tamanho do seu sapato é: ", y, " centímetros")