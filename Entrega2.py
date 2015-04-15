import random 
import turtle                           # Usa a biblioteca de turtle graphics
window = turtle.Screen()                # cria uma janela
window.bgcolor("red")                   # Muda a cor do fundo
window.title("Jogo da Forca")           # Título da janela
window.setup(width=1240,height=800,startx=-0,starty=000) #Define o tamanho da janela 
tartaruga = turtle.Turtle()  # Cria um objeto "desenhador" e atribui um nome
tartaruga.penup() # Levanta a caneta
tartaruga.setpos(-250,250) # Define a posição inicial
tartaruga.pendown() # Abaixa a caneta
tartaruga.color("black") # Muda a cor que vai ser escrita
tartaruga.write("Jogo da Forca", align = "left", font = ("arial", 40, "normal")) #Define a fonte 
tartaruga.speed(5) # Define a velocidade
tartaruga.penup() # Remova e veja o que acontece
tartaruga.setpos(-600,0) # Base da forca
tartaruga.pendown()
tartaruga.color("white") # Define a cor da tartaruga
tartaruga.pensize(6) # Espessura da linha desenhada
tartaruga.left(90) # Virar para esquerda
tartaruga.forward(250) # Ir para frente
tartaruga.right(90) # Virar para direita
tartaruga.forward(100) 
tartaruga.right(90)
tartaruga.forward(50)

print(tartaruga.pos()) # Mostra a posição que a tartaruga parou

def cabeca(): # Desenha a cabeça
        tartaruga.penup()        
        tartaruga.setpos(-500,100)
        tartaruga.pendown()
        tartaruga.circle(-50)

def corpo(): # Desenha o corpo
        tartaruga.penup()        
        tartaruga.setpos(-500,100)
        tartaruga.left(90)        
        tartaruga.pendown()
        tartaruga.bk(-50)

def braco1(): # Desenha o braço 1
        tartaruga.penup()        
        tartaruga.setpos(-500,75)
        tartaruga.pendown()
        tartaruga.right(45)
        tartaruga.bk(-25)

def braco2(): # Desenha o braço 2
        tartaruga.penup()        
        tartaruga.setpos(-500,75)
        tartaruga.pendown()
        tartaruga.left(90)
        tartaruga.bk(-25)

def perna1(): # Desenha a perna 1
        tartaruga.penup()        
        tartaruga.setpos(-500,50)
        tartaruga.pendown()
        tartaruga.left(5)
        tartaruga.bk(-25)

def perna2(): # Desenha a perna 2
        tartaruga.penup()        
        tartaruga.setpos(-500,50)
        tartaruga.pendown()
        tartaruga.right(-90)
        tartaruga.bk(25)

f = open("entrada.txt","r", encoding="utf-8") # Abre o arquivo com as palavras da forca
palavra = f.readlines() # Lê todas as linhas do arquivo
palavra_escolhida1 = random.choice(palavra) # Escolhe alguma palavra do arquivo
palavra_escolhida = palavra_escolhida1.upper() # Deixa todas as letras da palavra em maiscúla
print(palavra_escolhida) # Printa na tela a palavra escolhida

def linha(): # Linha que deve substituir cada letra
    tartaruga.pendown()
    tartaruga.left(0)
    tartaruga.bk(50) # Ir para trás
    
def espaco(): # Espaço entre as letras
    tartaruga.penup()        
    tartaruga.left(0)
    tartaruga.bk(25)

def espaco2(): # Caso a palavra seja composta
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
window.exitonclick() # Fecha a janela ao clicar sobre ela