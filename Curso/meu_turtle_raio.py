from turtle import*

pensize(10)
speed(1)

perimetro = 200
lados = 6
passo = perimetro/lados
angulo = 360/lados
color("red")
for i in range(lados):
    forward(passo)
    left(angulo)
left(angulo)
tamanho_raio = perimetro/(2*3.14)
print(tamanho_raio)
forward(tamanho_raio)




