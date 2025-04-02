from turtle import*

speed(1)

perimetro = 800

lados = 100
passo = perimetro/lados
angulo = 360/lados
color("red")
for i in range(lados*3):
    forward(passo)
    left(angulo)
    perimetro = perimetro * 0.99
    passo = perimetro/lados




