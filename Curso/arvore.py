from turtle import*

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

left(90)
arvore(3)