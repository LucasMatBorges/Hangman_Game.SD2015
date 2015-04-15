import random 
import turtle               # Usa a biblioteca de turtle graphics
window = turtle.Screen()    # cria uma janela
window.bgcolor("red")       # Muda a cor do fundo
window.title("Poligonos")
window.setup(width=1240,height=800,startx=-0,starty=000)
tartaruga   = turtle.Turtle()  # Cria um objeto "desenhador"
tartaruga.penup()
tartaruga.setpos(-250,250)
tartaruga.pendown()
tartaruga.color("black")
tartaruga.write("Jogo da Forca", align = "left", font = ("arial", 40, "normal"))
tartaruga.speed(5)  # define a velocidade
tartaruga.penup()       # Remova e veja o que acontece
tartaruga.setpos(-600,0) #Base da forca
tartaruga.pendown()
tartaruga.color("white") #Define a cor da tartaruga
#dist = 250
#angulo = 90

#for i in range(3):
  #  tartaruga.right(angulo)  # Vira o angulo pedido
    #tartaruga.forward(dist) # Avança a distancia pedida
tartaruga.pensize(6)
tartaruga.left(90)
tartaruga.forward(250)
tartaruga.right(90)
tartaruga.forward(100)
tartaruga.right(90)
tartaruga.forward(50)

a=tartaruga.pos() #mostra a posição que a tartaruga parou
print(a) 


def cabeca():
        tartaruga.penup()        
        tartaruga.setpos(-500,100)
        tartaruga.pendown()
        tartaruga.circle(-50)
#==============================================================================
# cabeca()
#==============================================================================

def corpo():
        tartaruga.penup()        
        tartaruga.setpos(-500,100)
        tartaruga.left(90)        
        tartaruga.pendown()
        tartaruga.bk(-50)
#==============================================================================
# corpo()
#==============================================================================

def braco1():
        tartaruga.penup()        
        tartaruga.setpos(-500,75)
        tartaruga.pendown()
        tartaruga.right(45)
        tartaruga.bk(-25)
#==============================================================================
# braco1()
#==============================================================================

def braco2():
        tartaruga.penup()        
        tartaruga.setpos(-500,75)
        tartaruga.pendown()
        tartaruga.left(90)
        tartaruga.bk(-25)
#==============================================================================
# braco2()
#==============================================================================

def perna1():
        tartaruga.penup()        
        tartaruga.setpos(-500,50)
        tartaruga.pendown()
        tartaruga.left(5)
        tartaruga.bk(-25)
#==============================================================================
# perna1()
#==============================================================================

def perna2():
        tartaruga.penup()        
        tartaruga.setpos(-500,50)
        tartaruga.pendown()
        tartaruga.right(-90)
        tartaruga.bk(25)
#==============================================================================
# perna2()
#==============================================================================

a1=tartaruga.pos() #mostra a posição que a tartaruga parou
print(a1) 
#a = window.textinput("Texto", "Digite a letra")
f = open("entrada.txt","r", encoding="utf-8")
palavra = f.readlines()
palavra_escolhida1 = random.choice(palavra)
palavra_escolhida = palavra_escolhida1.upper()
print(palavra_escolhida)

def linha():
    tartaruga.pendown()
    tartaruga.left(0)
    tartaruga.bk(50)
   # tartaruga.write(l)
    
def espaco():
    tartaruga.penup()        
    tartaruga.left(0)
    tartaruga.bk(25)

def espaco2():
    tartaruga.penup()        
    tartaruga.left(0)
    tartaruga.bk(50)

x=0
L=list(palavra_escolhida)
print(L)
tartaruga.penup() 
tartaruga.pensize(5)
tartaruga.right(90)
tartaruga.setpos(-400,0)
while x <len(palavra_escolhida)-1:
    l = L[x]
    if l == " ":
        espaco2()
        espaco()
    else:
     linha()
     espaco()
    x+=1

resposta=1    
tartaruga.pensize(2)
erros = 0
while erros<6:
 chute1 = window.textinput("Chute", "Escolha uma letra")
 chute = chute1.upper()
 
 if chute in L:    
    print("Legal")
    
 else: 
    erros = erros + 1 
    tartaruga.penup()
    tartaruga.setpos(-300+(erros*50),225)
    tartaruga.pendown()
    tartaruga.color("black")
    tartaruga.write(chute, align = "left", font = ("arial", 20, "normal"))
    tartaruga.color("white")    
    if erros == 1:
       cabeca()
    elif erros == 2:
        corpo()
    elif erros == 3:
        braco1()
    elif erros == 4:
        braco2()
    elif erros == 5:
        perna1()
    elif erros == 6:
        perna2()
        tartaruga.penup()
        tartaruga.setpos(-250,100)
        tartaruga.pendown()
        tartaruga.color("black")
        tartaruga.write("GAME OVER", align = "left", font = ("arial", 60, "normal"))
 for indice,tentativa in enumerate(L):
     if tentativa in L and tentativa==chute:
        tartaruga.penup()
        tartaruga.setpos(-400+(75*indice),0)
        tartaruga.pendown()
        tartaruga.write(chute, font = ("Arial" , 32)) # Escreve a letra na forca com a fonte escolhida
        resposta = resposta + 1
     
 if resposta==len(palavra_escolhida):
     break       
tartaruga.hideturtle
print(resposta)
print(erros)       
window.exitonclick()