from turtle import *
print('Quantos lados você quer que o casco da tartaruga tenha?')
try:
    lados_antes = int(input())
    if lados_antes <= 0:
        print("O número de lados deve ser positivo.")

    lados = lados_antes * 2
    perimetro = 400
    passo = perimetro / lados
    angulo = 360 / lados

    color("brown")

    lados_desenho = int(lados/2)
    

    for i in range(lados_desenho):
        forward(passo)
        right(angulo)

    right(90 - angulo)
    tamanho_raio = perimetro / (2 * 3.14)
    print("Raio aproximado:", tamanho_raio)

    forward(tamanho_raio)
    forward(tamanho_raio)

    done()
except ValueError as e:
    print(f"Entrada inválida: {e}")
