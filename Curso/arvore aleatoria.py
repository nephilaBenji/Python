from turtle import*
import random
#recursão

def arvore(altura):
    if(altura == 0):
        color("green")
        forward(30)
        backward(30)
        color("brown")
        return
    tamanho = random.randint(25,30)
    forward(tamanho)
    goright = random.randint(10,30)
    right(goright)
    arvore(altura-1)
    left(goright)
    goleft = random.randint(10,30)
    left(goleft)
    arvore(altura-1)
    right(goleft)
    backward(tamanho)

left(90)
arvore(15)