from turtle import*
import random
speed(0)
color("green")
pensize(3)
def arvore(altura):
    if(altura == 0):
        return
    forward(30)
    right(30)
    arvore(altura-1)
    left(30)
    left(30)
    arvore(altura-1)
    right(30)
    backward(30)

count_espacamento = 0
def espacamento():
    global count_espacamento
    count_espacamento += 1
    color("green")
    left(90)
    forward(170)
    left(270)

def voltar():
    global count_espacamento
    total = count_espacamento*170
    right(90)
    color("green")
    forward(total)

def casa():
    for i in range (4):
        color("yellow")
        left(90)
        forward(100)
    backward(100)
    color("red")
    right(240)
    forward(60)
    right(60)
    forward(60)


        



altura = random.randint(4,6)

left(90)
arvore(altura)
espacamento()
color("brown")
altura = random.randint(4,6)
arvore(altura)
espacamento()
color("lime")
altura = random.randint(4,6)
arvore(altura)
voltar()
right(90)
espacamento()
casa()
right(60)
color("yellow")
forward(100)
right(180)
voltar()
left(90)
arvore(altura)
espacamento()
color("brown")
altura = random.randint(4,6)
arvore(altura)
espacamento()
color("lime")
altura = random.randint(4,6)
arvore(altura)



mainloop()