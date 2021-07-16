# No Python 3:
from tkinter import *
from tkinter import messagebox
# No Python 2:
#from Tkinter import *
#import tkMessageBox as messagebox
import random

class myError(Exception):
    pass


class BatalhaNaval():
    def __init__(self,master):
        self.master = master
        self.frameCentro = Frame(master)
        self.frameCentro.pack(side=LEFT)

        self.framemomentaneo1=Frame(self.frameCentro)
        self.framemomentaneo1.pack()
        self.framemomentaneo2=Frame(self.frameCentro)
        self.framemomentaneo2.pack()
        self.framemomentaneo3=Frame(self.frameCentro)
        self.framemomentaneo3.pack()
        
        #Criando o botao iniciar
        self.iniciar = Button(self.framemomentaneo1,text='Iniciar',command=self.iniciarJogo,bg='black',fg='white',font=('Arial',12),width=87,height=2)#width=73,height=2
        self.iniciar.pack(side=LEFT)        

        #Criando as imagens
        self.variavel1=PhotoImage(file='esquerda2.gif')
        self.labelv1=Label(self.framemomentaneo3,image=self.variavel1,width=390,height=700)#width=400,height=700
        self.labelv1.pack(side=LEFT)
        self.variavel2=PhotoImage(file='direita2.gif')
        self.labelv2=Label(self.framemomentaneo3,image=self.variavel2,width=390,height=700)#width=400,height=700
        self.labelv2.pack(side=LEFT)

        #Criando a parte das chances
        self.labelf1=Label(self.framemomentaneo2,bg='yellow',text='Clique em iniciar, para começar o jogo.',fg='black',font=('Arial',12),width=87,height=2)#width=73,height=2
        self.labelf1.pack()
        self.navios = []
                                  
    def iniciarJogo(self):
        self.framemomentaneo1.destroy()
        self.framemomentaneo2.destroy()
        self.framemomentaneo3.destroy()       
        #-------------------------
        #Criando os 13 frames do centro
        self.frame1= Frame(self.frameCentro)#Frame onde fica as chances
        self.frame1.pack()
        self.frame2= Frame(self.frameCentro)#Frame para as letras
        self.frame2.pack()
        self.frame3= Frame(self.frameCentro,bg='grey')#A partir daqui começa as peças do tabuleiro 10x10
        self.frame3.pack()
        self.frame4= Frame(self.frameCentro,bg='grey')#Coloquei as cores
        self.frame4.pack()
        self.frame5= Frame(self.frameCentro,bg='grey')
        self.frame5.pack()
        self.frame6= Frame(self.frameCentro,bg='grey')
        self.frame6.pack()
        self.frame7= Frame(self.frameCentro,bg='grey')
        self.frame7.pack()
        self.frame8= Frame(self.frameCentro,bg='grey')
        self.frame8.pack()
        self.frame9= Frame(self.frameCentro,bg='grey')
        self.frame9.pack()
        self.frame10= Frame(self.frameCentro,bg='grey')
        self.frame10.pack()
        self.frame11= Frame(self.frameCentro,bg='grey')
        self.frame11.pack()
        self.frame12= Frame(self.frameCentro,bg='grey')#Aqui termina as peças do tabuleiro 10x10
        self.frame12.pack()
        self.frame13= Frame(self.frameCentro)#Frame para as letras
        self.frame13.pack()
        #----------------------ATENÇÃO AQUI FOI CRIADO UMA NOVA LABEL PARA AS CHANCES
        self.labelf1n=Label(self.frame1,bg='yellow',text='Você possui 20 tiros de canhão, acerte um dos navios e ganhe mais dois tiros.',fg='black',font=('Arial',12),width=100,height=2)#width=93,height=2
        self.labelf1n.pack()
        #----------------------
        #Criando as letras do tabuleiro
        self.labelf2= Label(self.frame2,bg='grey',text='A                B                C                D                E                F                G                H                I                J',fg='black',font=('Arial',12),width=100,height=2)#width=93,height=2
        self.labelf2.pack(side=LEFT)#'A            B            C          D          E            F            G            H            I            J'
        self.labelf14= Label(self.frame13,bg='grey',text='A                B                C                D                E                F                G                H                I                J',fg='black',font=('Arial',12),width=100,height=2)#width=93,height=2
        self.labelf14.pack(side=LEFT)
        #---------------------
        #Criando os numeros do tabuleiro lado esquerdo
        self.label3E = Label(self.frame3,bg='grey',fg='black',font=('Arial',12),text='1',width=9,height=3)
        self.label3E.pack(side=LEFT)
        self.label4E = Label(self.frame4,bg='grey',fg='black',font=('Arial',12),text='2',width=9,height=3)
        self.label4E.pack(side=LEFT)
        self.label5E = Label(self.frame5,bg='grey',fg='black',font=('Arial',12),text='3',width=9,height=3)
        self.label5E.pack(side=LEFT)
        self.label6E = Label(self.frame6,bg='grey',fg='black',font=('Arial',12),text='4',width=9,height=3)
        self.label6E.pack(side=LEFT)
        self.label7E = Label(self.frame7,bg='grey',fg='black',font=('Arial',12),text='5',width=9,height=3)
        self.label7E.pack(side=LEFT)
        self.label8E = Label(self.frame8,bg='grey',fg='black',font=('Arial',12),text='6',width=9,height=3)
        self.label8E.pack(side=LEFT)
        self.label9E = Label(self.frame9,bg='grey',fg='black',font=('Arial',12),text='7',width=9,height=3)
        self.label9E.pack(side=LEFT)
        self.label10E = Label(self.frame10,bg='grey',fg='black',font=('Arial',12),text='8',width=9,height=3)
        self.label10E.pack(side=LEFT)
        self.label11E = Label(self.frame11,bg='grey',fg='black',font=('Arial',12),text='9',width=9,height=3)
        self.label11E.pack(side=LEFT)
        self.label12E = Label(self.frame12,bg='grey',fg='black',font=('Arial',12),text='10',width=9,height=3)
        self.label12E.pack(side=LEFT)
        #Criando os numeros do tabuleiro lado direito
        self.label3D = Label(self.frame3,bg='grey',fg='black',font=('Arial',12),text='1',width=9,height=3)
        self.label3D.pack(side=RIGHT)
        self.label4D = Label(self.frame4,bg='grey',fg='black',font=('Arial',12),text='2',width=9,height=3)
        self.label4D.pack(side=RIGHT)
        self.label5D = Label(self.frame5,bg='grey',fg='black',font=('Arial',12),text='3',width=9,height=3)
        self.label5D.pack(side=RIGHT)
        self.label6D = Label(self.frame6,bg='grey',fg='black',font=('Arial',12),text='4',width=9,height=3)
        self.label6D.pack(side=RIGHT)
        self.label7D = Label(self.frame7,bg='grey',fg='black',font=('Arial',12),text='5',width=9,height=3)
        self.label7D.pack(side=RIGHT)
        self.label8D = Label(self.frame8,bg='grey',fg='black',font=('Arial',12),text='6',width=9,height=3)
        self.label8D.pack(side=RIGHT)
        self.label9D = Label(self.frame9,bg='grey',fg='black',font=('Arial',12),text='7',width=9,height=3)
        self.label9D.pack(side=RIGHT)
        self.label10D = Label(self.frame10,bg='grey',fg='black',font=('Arial',12),text='8',width=9,height=3)
        self.label10D.pack(side=RIGHT)
        self.label11D = Label(self.frame11,bg='grey',fg='black',font=('Arial',12),text='9',width=9,height=3)
        self.label11D.pack(side=RIGHT)
        self.label12D = Label(self.frame12,bg='grey',fg='black',font=('Arial',12),text='10',width=9,height=3)
        self.label12D.pack(side=RIGHT)
        #---------------------------
        #Frames Linha 1
        self.frameA1 = Frame(self.frame3,bg='#add8e6')
        self.frameA1.pack(side=LEFT)
        self.frameB1 = Frame(self.frame3,bg='#add8e6')
        self.frameB1.pack(side=LEFT)
        self.frameC1 = Frame(self.frame3,bg='#add8e6')
        self.frameC1.pack(side=LEFT)
        self.frameD1 = Frame(self.frame3,bg='#add8e6')
        self.frameD1.pack(side=LEFT)
        self.frameE1 = Frame(self.frame3,bg='#add8e6')
        self.frameE1.pack(side=LEFT)
        self.frameF1 = Frame(self.frame3,bg='#add8e6')
        self.frameF1.pack(side=LEFT)
        self.frameG1 = Frame(self.frame3,bg='#add8e6')
        self.frameG1.pack(side=LEFT)
        self.frameH1 = Frame(self.frame3,bg='#add8e6')
        self.frameH1.pack(side=LEFT)
        self.frameI1 = Frame(self.frame3,bg='#add8e6')
        self.frameI1.pack(side=LEFT)
        self.frameJ1 = Frame(self.frame3,bg='#add8e6')
        self.frameJ1.pack(side=LEFT)
        #Frames Linha 2
        self.frameA2 = Frame(self.frame4,bg='#add8e6')
        self.frameA2.pack(side=LEFT)
        self.frameB2 = Frame(self.frame4,bg='#add8e6')
        self.frameB2.pack(side=LEFT)
        self.frameC2 = Frame(self.frame4,bg='#add8e6')
        self.frameC2.pack(side=LEFT)
        self.frameD2 = Frame(self.frame4,bg='#add8e6')
        self.frameD2.pack(side=LEFT)
        self.frameE2 = Frame(self.frame4,bg='#add8e6')
        self.frameE2.pack(side=LEFT)
        self.frameF2 = Frame(self.frame4,bg='#add8e6')
        self.frameF2.pack(side=LEFT)
        self.frameG2 = Frame(self.frame4,bg='#add8e6')
        self.frameG2.pack(side=LEFT)
        self.frameH2 = Frame(self.frame4,bg='#add8e6')
        self.frameH2.pack(side=LEFT)
        self.frameI2 = Frame(self.frame4,bg='#add8e6')
        self.frameI2.pack(side=LEFT)
        self.frameJ2 = Frame(self.frame4,bg='#add8e6')
        self.frameJ2.pack(side=LEFT)
        #Frames Linha 3
        self.frameA3 = Frame(self.frame5,bg='#add8e6')
        self.frameA3.pack(side=LEFT)
        self.frameB3 = Frame(self.frame5,bg='#add8e6')
        self.frameB3.pack(side=LEFT)
        self.frameC3 = Frame(self.frame5,bg='#add8e6')
        self.frameC3.pack(side=LEFT)
        self.frameD3 = Frame(self.frame5,bg='#add8e6')
        self.frameD3.pack(side=LEFT)
        self.frameE3 = Frame(self.frame5,bg='#add8e6')
        self.frameE3.pack(side=LEFT)
        self.frameF3 = Frame(self.frame5,bg='#add8e6')
        self.frameF3.pack(side=LEFT)
        self.frameG3 = Frame(self.frame5,bg='#add8e6')
        self.frameG3.pack(side=LEFT)
        self.frameH3 = Frame(self.frame5,bg='#add8e6')
        self.frameH3.pack(side=LEFT)
        self.frameI3 = Frame(self.frame5,bg='#add8e6')
        self.frameI3.pack(side=LEFT)
        self.frameJ3 = Frame(self.frame5,bg='#add8e6')
        self.frameJ3.pack(side=LEFT)
        #Frames Linha 4
        self.frameA4 = Frame(self.frame6,bg='#add8e6')
        self.frameA4.pack(side=LEFT)
        self.frameB4 = Frame(self.frame6,bg='#add8e6')
        self.frameB4.pack(side=LEFT)
        self.frameC4 = Frame(self.frame6,bg='#add8e6')
        self.frameC4.pack(side=LEFT)
        self.frameD4 = Frame(self.frame6,bg='#add8e6')
        self.frameD4.pack(side=LEFT)
        self.frameE4 = Frame(self.frame6,bg='#add8e6')
        self.frameE4.pack(side=LEFT)
        self.frameF4 = Frame(self.frame6,bg='#add8e6')
        self.frameF4.pack(side=LEFT)
        self.frameG4 = Frame(self.frame6,bg='#add8e6')
        self.frameG4.pack(side=LEFT)
        self.frameH4 = Frame(self.frame6,bg='#add8e6')
        self.frameH4.pack(side=LEFT)
        self.frameI4 = Frame(self.frame6,bg='#add8e6')
        self.frameI4.pack(side=LEFT)
        self.frameJ4 = Frame(self.frame6,bg='#add8e6')
        self.frameJ4.pack(side=LEFT)
        #Frames Linha 5
        self.frameA5 = Frame(self.frame7,bg='#add8e6')
        self.frameA5.pack(side=LEFT)
        self.frameB5 = Frame(self.frame7,bg='#add8e6')
        self.frameB5.pack(side=LEFT)
        self.frameC5 = Frame(self.frame7,bg='#add8e6')
        self.frameC5.pack(side=LEFT)
        self.frameD5 = Frame(self.frame7,bg='#add8e6')
        self.frameD5.pack(side=LEFT)
        self.frameE5 = Frame(self.frame7,bg='#add8e6')
        self.frameE5.pack(side=LEFT)
        self.frameF5 = Frame(self.frame7,bg='#add8e6')
        self.frameF5.pack(side=LEFT)
        self.frameG5 = Frame(self.frame7,bg='#add8e6')
        self.frameG5.pack(side=LEFT)
        self.frameH5 = Frame(self.frame7,bg='#add8e6')
        self.frameH5.pack(side=LEFT)
        self.frameI5 = Frame(self.frame7,bg='#add8e6')
        self.frameI5.pack(side=LEFT)
        self.frameJ5 = Frame(self.frame7,bg='#add8e6')
        self.frameJ5.pack(side=LEFT)
        #Frames Linha 6
        self.frameA6 = Frame(self.frame8,bg='#add8e6')
        self.frameA6.pack(side=LEFT)
        self.frameB6 = Frame(self.frame8,bg='#add8e6')
        self.frameB6.pack(side=LEFT)
        self.frameC6 = Frame(self.frame8,bg='#add8e6')
        self.frameC6.pack(side=LEFT)
        self.frameD6 = Frame(self.frame8,bg='#add8e6')
        self.frameD6.pack(side=LEFT)
        self.frameE6 = Frame(self.frame8,bg='#add8e6')
        self.frameE6.pack(side=LEFT)
        self.frameF6 = Frame(self.frame8,bg='#add8e6')
        self.frameF6.pack(side=LEFT)
        self.frameG6 = Frame(self.frame8,bg='#add8e6')
        self.frameG6.pack(side=LEFT)
        self.frameH6 = Frame(self.frame8,bg='#add8e6')
        self.frameH6.pack(side=LEFT)
        self.frameI6 = Frame(self.frame8,bg='#add8e6')
        self.frameI6.pack(side=LEFT)
        self.frameJ6 = Frame(self.frame8,bg='#add8e6')
        self.frameJ6.pack(side=LEFT)
        #Frames Linha 7
        self.frameA7 = Frame(self.frame9,bg='#add8e6')
        self.frameA7.pack(side=LEFT)
        self.frameB7 = Frame(self.frame9,bg='#add8e6')
        self.frameB7.pack(side=LEFT)
        self.frameC7 = Frame(self.frame9,bg='#add8e6')
        self.frameC7.pack(side=LEFT)
        self.frameD7 = Frame(self.frame9,bg='#add8e6')
        self.frameD7.pack(side=LEFT)
        self.frameE7 = Frame(self.frame9,bg='#add8e6')
        self.frameE7.pack(side=LEFT)
        self.frameF7 = Frame(self.frame9,bg='#add8e6')
        self.frameF7.pack(side=LEFT)
        self.frameG7 = Frame(self.frame9,bg='#add8e6')
        self.frameG7.pack(side=LEFT)
        self.frameH7 = Frame(self.frame9,bg='#add8e6')
        self.frameH7.pack(side=LEFT)
        self.frameI7 = Frame(self.frame9,bg='#add8e6')
        self.frameI7.pack(side=LEFT)
        self.frameJ7 = Frame(self.frame9,bg='#add8e6')
        self.frameJ7.pack(side=LEFT)
        #Frames Linha 8
        self.frameA8 = Frame(self.frame10,bg='#add8e6')
        self.frameA8.pack(side=LEFT)
        self.frameB8 = Frame(self.frame10,bg='#add8e6')
        self.frameB8.pack(side=LEFT)
        self.frameC8 = Frame(self.frame10,bg='#add8e6')
        self.frameC8.pack(side=LEFT)
        self.frameD8 = Frame(self.frame10,bg='#add8e6')
        self.frameD8.pack(side=LEFT)
        self.frameE8 = Frame(self.frame10,bg='#add8e6')
        self.frameE8.pack(side=LEFT)
        self.frameF8 = Frame(self.frame10,bg='#add8e6')
        self.frameF8.pack(side=LEFT)
        self.frameG8 = Frame(self.frame10,bg='#add8e6')
        self.frameG8.pack(side=LEFT)
        self.frameH8 = Frame(self.frame10,bg='#add8e6')
        self.frameH8.pack(side=LEFT)
        self.frameI8 = Frame(self.frame10,bg='#add8e6')
        self.frameI8.pack(side=LEFT)
        self.frameJ8 = Frame(self.frame10,bg='#add8e6')
        self.frameJ8.pack(side=LEFT)
        #Frames Linha 9
        self.frameA9 = Frame(self.frame11,bg='#add8e6')
        self.frameA9.pack(side=LEFT)
        self.frameB9 = Frame(self.frame11,bg='#add8e6')
        self.frameB9.pack(side=LEFT)
        self.frameC9 = Frame(self.frame11,bg='#add8e6')
        self.frameC9.pack(side=LEFT)
        self.frameD9 = Frame(self.frame11,bg='#add8e6')
        self.frameD9.pack(side=LEFT)
        self.frameE9 = Frame(self.frame11,bg='#add8e6')
        self.frameE9.pack(side=LEFT)
        self.frameF9 = Frame(self.frame11,bg='#add8e6')
        self.frameF9.pack(side=LEFT)
        self.frameG9 = Frame(self.frame11,bg='#add8e6')
        self.frameG9.pack(side=LEFT)
        self.frameH9 = Frame(self.frame11,bg='#add8e6')
        self.frameH9.pack(side=LEFT)
        self.frameI9 = Frame(self.frame11,bg='#add8e6')
        self.frameI9.pack(side=LEFT)
        self.frameJ9 = Frame(self.frame11,bg='#add8e6')
        self.frameJ9.pack(side=LEFT)
        #Frames Linha 10
        self.frameA10 = Frame(self.frame12,bg='#add8e6')
        self.frameA10.pack(side=LEFT)
        self.frameB10 = Frame(self.frame12,bg='#add8e6')
        self.frameB10.pack(side=LEFT)
        self.frameC10 = Frame(self.frame12,bg='#add8e6')
        self.frameC10.pack(side=LEFT)
        self.frameD10 = Frame(self.frame12,bg='#add8e6')
        self.frameD10.pack(side=LEFT)
        self.frameE10 = Frame(self.frame12,bg='#add8e6')
        self.frameE10.pack(side=LEFT)
        self.frameF10 = Frame(self.frame12,bg='#add8e6')
        self.frameF10.pack(side=LEFT)
        self.frameG10 = Frame(self.frame12,bg='#add8e6')
        self.frameG10.pack(side=LEFT)
        self.frameH10 = Frame(self.frame12,bg='#add8e6')
        self.frameH10.pack(side=LEFT)
        self.frameI10 = Frame(self.frame12,bg='#add8e6')
        self.frameI10.pack(side=LEFT)
        self.frameJ10 = Frame(self.frame12,bg='#add8e6')
        self.frameJ10.pack(side=LEFT)
        #-------------------------------------------------------------------------------------------------
        #Botoes Linha 1
        self.A1 = Button(self.frameA1,bg='black',command=lambda: self.destruir(self.A1,self.frameA1),width=9,height=3)
        self.A1.pack(side=LEFT)
        self.B1 = Button(self.frameB1,bg='black',command=lambda: self.destruir(self.B1,self.frameB1),width=9,height=3)
        self.B1.pack(side=LEFT)
        self.C1 = Button(self.frameC1,bg='black',command=lambda: self.destruir(self.C1,self.frameC1),width=9,height=3)
        self.C1.pack(side=LEFT)
        self.D1 = Button(self.frameD1,bg='black',command=lambda: self.destruir(self.D1,self.frameD1),width=9,height=3)
        self.D1.pack(side=LEFT)
        self.E1 = Button(self.frameE1,bg='black',command=lambda: self.destruir(self.E1,self.frameE1),width=9,height=3)
        self.E1.pack(side=LEFT)
        self.F1 = Button(self.frameF1,bg='black',command=lambda: self.destruir(self.F1,self.frameF1),width=9,height=3)
        self.F1.pack(side=LEFT)
        self.G1 = Button(self.frameG1,bg='black',command=lambda: self.destruir(self.G1,self.frameG1),width=9,height=3)
        self.G1.pack(side=LEFT)
        self.H1 = Button(self.frameH1,bg='black',command=lambda: self.destruir(self.H1,self.frameH1),width=9,height=3)
        self.H1.pack(side=LEFT)
        self.I1 = Button(self.frameI1,bg='black',command=lambda: self.destruir(self.I1,self.frameI1),width=9,height=3)
        self.I1.pack(side=LEFT)
        self.J1 = Button(self.frameJ1,bg='black',command=lambda: self.destruir(self.J1,self.frameJ1),width=9,height=3)
        self.J1.pack(side=LEFT)
        #Botoes Linha 2
        self.A2 = Button(self.frameA2,bg='black',command=lambda: self.destruir(self.A2,self.frameA2),width=9,height=3)
        self.A2.pack(side=LEFT)
        self.B2 = Button(self.frameB2,bg='black',command=lambda: self.destruir(self.B2,self.frameB2),width=9,height=3)
        self.B2.pack(side=LEFT)
        self.C2 = Button(self.frameC2,bg='black',command=lambda: self.destruir(self.C2,self.frameC2),width=9,height=3)
        self.C2.pack(side=LEFT)
        self.D2 = Button(self.frameD2,bg='black',command=lambda: self.destruir(self.D2,self.frameD2),width=9,height=3)
        self.D2.pack(side=LEFT)
        self.E2 = Button(self.frameE2,bg='black',command=lambda: self.destruir(self.E2,self.frameE2),width=9,height=3)
        self.E2.pack(side=LEFT)
        self.F2 = Button(self.frameF2,bg='black',command=lambda: self.destruir(self.F2,self.frameF2),width=9,height=3)
        self.F2.pack(side=LEFT)
        self.G2 = Button(self.frameG2,bg='black',command=lambda: self.destruir(self.G2,self.frameG2),width=9,height=3)
        self.G2.pack(side=LEFT)
        self.H2 = Button(self.frameH2,bg='black',command=lambda: self.destruir(self.H2,self.frameH2),width=9,height=3)
        self.H2.pack(side=LEFT)
        self.I2 = Button(self.frameI2,bg='black',command=lambda: self.destruir(self.I2,self.frameI2),width=9,height=3)
        self.I2.pack(side=LEFT)
        self.J2 = Button(self.frameJ2,bg='black',command=lambda: self.destruir(self.J2,self.frameJ2),width=9,height=3)
        self.J2.pack(side=LEFT)
        #Botoes Linha 3
        self.A3 = Button(self.frameA3,bg='black',command=lambda: self.destruir(self.A3,self.frameA3),width=9,height=3)
        self.A3.pack(side=LEFT)
        self.B3 = Button(self.frameB3,bg='black',command=lambda: self.destruir(self.B3,self.frameB3),width=9,height=3)
        self.B3.pack(side=LEFT)
        self.C3 = Button(self.frameC3,bg='black',command=lambda: self.destruir(self.C3,self.frameC3),width=9,height=3)
        self.C3.pack(side=LEFT)
        self.D3 = Button(self.frameD3,bg='black',command=lambda: self.destruir(self.D3,self.frameD3),width=9,height=3)
        self.D3.pack(side=LEFT)
        self.E3 = Button(self.frameE3,bg='black',command=lambda: self.destruir(self.E3,self.frameE3),width=9,height=3)
        self.E3.pack(side=LEFT)
        self.F3 = Button(self.frameF3,bg='black',command=lambda: self.destruir(self.F3,self.frameF3),width=9,height=3)
        self.F3.pack(side=LEFT)
        self.G3 = Button(self.frameG3,bg='black',command=lambda: self.destruir(self.G3,self.frameG3),width=9,height=3)
        self.G3.pack(side=LEFT)
        self.H3 = Button(self.frameH3,bg='black',command=lambda: self.destruir(self.H3,self.frameH3),width=9,height=3)
        self.H3.pack(side=LEFT)
        self.I3 = Button(self.frameI3,bg='black',command=lambda: self.destruir(self.I3,self.frameI3),width=9,height=3)
        self.I3.pack(side=LEFT)
        self.J3 = Button(self.frameJ3,bg='black',command=lambda: self.destruir(self.J3,self.frameJ3),width=9,height=3)
        self.J3.pack(side=LEFT)
        #Botoes Linha 4
        self.A4 = Button(self.frameA4,bg='black',command=lambda: self.destruir(self.A4,self.frameA4),width=9,height=3)
        self.A4.pack(side=LEFT)
        self.B4 = Button(self.frameB4,bg='black',command=lambda: self.destruir(self.B4,self.frameB4),width=9,height=3)
        self.B4.pack(side=LEFT)
        self.C4 = Button(self.frameC4,bg='black',command=lambda: self.destruir(self.C4,self.frameC4),width=9,height=3)
        self.C4.pack(side=LEFT)
        self.D4 = Button(self.frameD4,bg='black',command=lambda: self.destruir(self.D4,self.frameD4),width=9,height=3)
        self.D4.pack(side=LEFT)
        self.E4 = Button(self.frameE4,bg='black',command=lambda: self.destruir(self.E4,self.frameE4),width=9,height=3)
        self.E4.pack(side=LEFT)
        self.F4 = Button(self.frameF4,bg='black',command=lambda: self.destruir(self.F4,self.frameF4),width=9,height=3)
        self.F4.pack(side=LEFT)
        self.G4 = Button(self.frameG4,bg='black',command=lambda: self.destruir(self.G4,self.frameG4),width=9,height=3)
        self.G4.pack(side=LEFT)
        self.H4 = Button(self.frameH4,bg='black',command=lambda: self.destruir(self.H4,self.frameH4),width=9,height=3)
        self.H4.pack(side=LEFT)
        self.I4 = Button(self.frameI4,bg='black',command=lambda: self.destruir(self.I4,self.frameI4),width=9,height=3)
        self.I4.pack(side=LEFT)
        self.J4 = Button(self.frameJ4,bg='black',command=lambda: self.destruir(self.J4,self.frameJ4),width=9,height=3)
        self.J4.pack(side=LEFT)
        #Botoes Linha 5
        self.A5 = Button(self.frameA5,bg='black',command=lambda: self.destruir(self.A5,self.frameA5),width=9,height=3)
        self.A5.pack(side=LEFT)
        self.B5 = Button(self.frameB5,bg='black',command=lambda: self.destruir(self.B5,self.frameB5),width=9,height=3)
        self.B5.pack(side=LEFT)
        self.C5 = Button(self.frameC5,bg='black',command=lambda: self.destruir(self.C5,self.frameC5),width=9,height=3)
        self.C5.pack(side=LEFT)
        self.D5 = Button(self.frameD5,bg='black',command=lambda: self.destruir(self.D5,self.frameD5),width=9,height=3)
        self.D5.pack(side=LEFT)
        self.E5 = Button(self.frameE5,bg='black',command=lambda: self.destruir(self.E5,self.frameE5),width=9,height=3)
        self.E5.pack(side=LEFT)
        self.F5 = Button(self.frameF5,bg='black',command=lambda: self.destruir(self.F5,self.frameF5),width=9,height=3)
        self.F5.pack(side=LEFT)
        self.G5 = Button(self.frameG5,bg='black',command=lambda: self.destruir(self.G5,self.frameG5),width=9,height=3)
        self.G5.pack(side=LEFT)
        self.H5 = Button(self.frameH5,bg='black',command=lambda: self.destruir(self.H5,self.frameH5),width=9,height=3)
        self.H5.pack(side=LEFT)
        self.I5 = Button(self.frameI5,bg='black',command=lambda: self.destruir(self.I5,self.frameI5),width=9,height=3)
        self.I5.pack(side=LEFT)
        self.J5 = Button(self.frameJ5,bg='black',command=lambda: self.destruir(self.J5,self.frameJ5),width=9,height=3)
        self.J5.pack(side=LEFT)
        #Botoes Linha 6
        self.A6 = Button(self.frameA6,bg='black',command=lambda: self.destruir(self.A6,self.frameA6),width=9,height=3)
        self.A6.pack(side=LEFT)
        self.B6 = Button(self.frameB6,bg='black',command=lambda: self.destruir(self.B6,self.frameB6),width=9,height=3)
        self.B6.pack(side=LEFT)
        self.C6 = Button(self.frameC6,bg='black',command=lambda: self.destruir(self.C6,self.frameC6),width=9,height=3)
        self.C6.pack(side=LEFT)
        self.D6 = Button(self.frameD6,bg='black',command=lambda: self.destruir(self.D6,self.frameD6),width=9,height=3)
        self.D6.pack(side=LEFT)
        self.E6 = Button(self.frameE6,bg='black',command=lambda: self.destruir(self.E6,self.frameE6),width=9,height=3)
        self.E6.pack(side=LEFT)
        self.F6 = Button(self.frameF6,bg='black',command=lambda: self.destruir(self.F6,self.frameF6),width=9,height=3)
        self.F6.pack(side=LEFT)
        self.G6 = Button(self.frameG6,bg='black',command=lambda: self.destruir(self.G6,self.frameG6),width=9,height=3)
        self.G6.pack(side=LEFT)
        self.H6 = Button(self.frameH6,bg='black',command=lambda: self.destruir(self.H6,self.frameH6),width=9,height=3)
        self.H6.pack(side=LEFT)
        self.I6 = Button(self.frameI6,bg='black',command=lambda: self.destruir(self.I6,self.frameI6),width=9,height=3)
        self.I6.pack(side=LEFT)
        self.J6 = Button(self.frameJ6,bg='black',command=lambda: self.destruir(self.J6,self.frameJ6),width=9,height=3)
        self.J6.pack(side=LEFT)
        #Botoes Linha 7
        self.A7 = Button(self.frameA7,bg='black',command=lambda: self.destruir(self.A7,self.frameA7),width=9,height=3)
        self.A7.pack(side=LEFT)
        self.B7 = Button(self.frameB7,bg='black',command=lambda: self.destruir(self.B7,self.frameB7),width=9,height=3)
        self.B7.pack(side=LEFT)
        self.C7 = Button(self.frameC7,bg='black',command=lambda: self.destruir(self.C7,self.frameC7),width=9,height=3)
        self.C7.pack(side=LEFT)
        self.D7 = Button(self.frameD7,bg='black',command=lambda: self.destruir(self.D7,self.frameD7),width=9,height=3)
        self.D7.pack(side=LEFT)
        self.E7 = Button(self.frameE7,bg='black',command=lambda: self.destruir(self.E7,self.frameE7),width=9,height=3)
        self.E7.pack(side=LEFT)
        self.F7 = Button(self.frameF7,bg='black',command=lambda: self.destruir(self.F7,self.frameF7),width=9,height=3)
        self.F7.pack(side=LEFT)
        self.G7 = Button(self.frameG7,bg='black',command=lambda: self.destruir(self.G7,self.frameG7),width=9,height=3)
        self.G7.pack(side=LEFT)
        self.H7 = Button(self.frameH7,bg='black',command=lambda: self.destruir(self.H7,self.frameH7),width=9,height=3)
        self.H7.pack(side=LEFT)
        self.I7 = Button(self.frameI7,bg='black',command=lambda: self.destruir(self.I7,self.frameI7),width=9,height=3)
        self.I7.pack(side=LEFT)
        self.J7 = Button(self.frameJ7,bg='black',command=lambda: self.destruir(self.J7,self.frameJ7),width=9,height=3)
        self.J7.pack(side=LEFT)
        #Botoes Linha 8
        self.A8 = Button(self.frameA8,bg='black',command=lambda: self.destruir(self.A8,self.frameA8),width=9,height=3)
        self.A8.pack(side=LEFT)
        self.B8 = Button(self.frameB8,bg='black',command=lambda: self.destruir(self.B8,self.frameB8),width=9,height=3)
        self.B8.pack(side=LEFT)
        self.C8 = Button(self.frameC8,bg='black',command=lambda: self.destruir(self.C8,self.frameC8),width=9,height=3)
        self.C8.pack(side=LEFT)
        self.D8 = Button(self.frameD8,bg='black',command=lambda: self.destruir(self.D8,self.frameD8),width=9,height=3)
        self.D8.pack(side=LEFT)
        self.E8 = Button(self.frameE8,bg='black',command=lambda: self.destruir(self.E8,self.frameE8),width=9,height=3)
        self.E8.pack(side=LEFT)
        self.F8 = Button(self.frameF8,bg='black',command=lambda: self.destruir(self.F8,self.frameF8),width=9,height=3)
        self.F8.pack(side=LEFT)
        self.G8 = Button(self.frameG8,bg='black',command=lambda: self.destruir(self.G8,self.frameG8),width=9,height=3)
        self.G8.pack(side=LEFT)
        self.H8 = Button(self.frameH8,bg='black',command=lambda: self.destruir(self.H8,self.frameH8),width=9,height=3)
        self.H8.pack(side=LEFT)
        self.I8 = Button(self.frameI8,bg='black',command=lambda: self.destruir(self.I8,self.frameI8),width=9,height=3)
        self.I8.pack(side=LEFT)
        self.J8 = Button(self.frameJ8,bg='black',command=lambda: self.destruir(self.J8,self.frameJ8),width=9,height=3)
        self.J8.pack(side=LEFT)
        #Botoes Linha 9
        self.A9 = Button(self.frameA9,bg='black',command=lambda: self.destruir(self.A9,self.frameA9),width=9,height=3)
        self.A9.pack(side=LEFT)
        self.B9 = Button(self.frameB9,bg='black',command=lambda: self.destruir(self.B9,self.frameB9),width=9,height=3)
        self.B9.pack(side=LEFT)
        self.C9 = Button(self.frameC9,bg='black',command=lambda: self.destruir(self.C9,self.frameC9),width=9,height=3)
        self.C9.pack(side=LEFT)
        self.D9 = Button(self.frameD9,bg='black',command=lambda: self.destruir(self.D9,self.frameD9),width=9,height=3)
        self.D9.pack(side=LEFT)
        self.E9 = Button(self.frameE9,bg='black',command=lambda: self.destruir(self.E9,self.frameE9),width=9,height=3)
        self.E9.pack(side=LEFT)
        self.F9 = Button(self.frameF9,bg='black',command=lambda: self.destruir(self.F9,self.frameF9),width=9,height=3)
        self.F9.pack(side=LEFT)
        self.G9 = Button(self.frameG9,bg='black',command=lambda: self.destruir(self.G9,self.frameG9),width=9,height=3)
        self.G9.pack(side=LEFT)
        self.H9 = Button(self.frameH9,bg='black',command=lambda: self.destruir(self.H9,self.frameH9),width=9,height=3)
        self.H9.pack(side=LEFT)
        self.I9 = Button(self.frameI9,bg='black',command=lambda: self.destruir(self.I9,self.frameI9),width=9,height=3)
        self.I9.pack(side=LEFT)
        self.J9 = Button(self.frameJ9,bg='black',command=lambda: self.destruir(self.J9,self.frameJ9),width=9,height=3)
        self.J9.pack(side=LEFT)
        #Botoes Linha 10
        self.A10 = Button(self.frameA10,bg='black',command=lambda: self.destruir(self.A10,self.frameA10),width=9,height=3)
        self.A10.pack(side=LEFT)
        self.B10 = Button(self.frameB10,bg='black',command=lambda: self.destruir(self.B10,self.frameB10),width=9,height=3)
        self.B10.pack(side=LEFT)
        self.C10 = Button(self.frameC10,bg='black',command=lambda: self.destruir(self.C10,self.frameC10),width=9,height=3)
        self.C10.pack(side=LEFT)
        self.D10 = Button(self.frameD10,bg='black',command=lambda: self.destruir(self.D10,self.frameD10),width=9,height=3)
        self.D10.pack(side=LEFT)
        self.E10 = Button(self.frameE10,bg='black',command=lambda: self.destruir(self.E10,self.frameE10),width=9,height=3)
        self.E10.pack(side=LEFT)
        self.F10 = Button(self.frameF10,bg='black',command=lambda: self.destruir(self.F10,self.frameF10),width=9,height=3)
        self.F10.pack(side=LEFT)
        self.G10 = Button(self.frameG10,bg='black',command=lambda: self.destruir(self.G10,self.frameG10),width=9,height=3)
        self.G10.pack(side=LEFT)
        self.H10 = Button(self.frameH10,bg='black',command=lambda: self.destruir(self.H10,self.frameH10),width=9,height=3)
        self.H10.pack(side=LEFT)
        self.I10 = Button(self.frameI10,bg='black',command=lambda: self.destruir(self.I10,self.frameI10),width=9,height=3)
        self.I10.pack(side=LEFT)
        self.J10 = Button(self.frameJ10,bg='black',command=lambda: self.destruir(self.J10,self.frameJ10),width=9,height=3)
        self.J10.pack(side=LEFT)
        #-----------------------------------
        self.posicao=[self.frameA1,self.frameB1,self.frameC1,self.frameD1,self.frameE1,self.frameF1,self.frameG1,\
            self.frameH1,self.frameI1,self.frameJ1,self.frameA2,self.frameB2,self.frameC2,self.frameD2,\
            self.frameE2,self.frameF2,self.frameG2,self.frameH2,self.frameI2,self.frameJ2,self.frameA3,\
            self.frameB3,self.frameC3,self.frameD3,self.frameE3,self.frameF3,self.frameG3,self.frameH3,\
            self.frameI3,self.frameJ3,self.frameA4,self.frameB4,self.frameC4,self.frameD4,self.frameE4,\
            self.frameF4,self.frameG4,self.frameH4,self.frameI4,self.frameJ4,self.frameA5,self.frameB5,\
            self.frameC5,self.frameD5,self.frameE5,self.frameF5,self.frameG5,self.frameH5,self.frameI5,\
            self.frameJ5,self.frameA6,self.frameB6,self.frameC6,self.frameD6,self.frameE6,self.frameF6,\
            self.frameG6,self.frameH6,self.frameI6,self.frameJ6,self.frameA7,self.frameB7,self.frameC7,\
            self.frameD7,self.frameE7,self.frameF7,self.frameG7,self.frameH7,self.frameI7,self.frameJ7,\
            self.frameA8,self.frameB8,self.frameC8,self.frameD8,self.frameE8,self.frameF8,self.frameG8,\
            self.frameH8,self.frameI8,self.frameJ8,self.frameA9,self.frameB9,self.frameC9,self.frameD9,\
            self.frameE9,self.frameF9,self.frameG9,self.frameH9,self.frameI9,self.frameJ9,self.frameA10,\
            self.frameB10,self.frameC10,self.frameD10,self.frameE10,self.frameF10,self.frameG10,self.frameH10,\
            self.frameI10,self.frameJ10]
        #---------------
        self.As=[self.frameA1,self.frameA2,self.frameA3,self.frameA4,self.frameA5,self.frameA6,self.frameA7,self.frameA8,self.frameA9,self.A10]
        self.Bs=[self.frameB1,self.frameB2,self.frameB3,self.frameB4,self.frameB5,self.frameB6,self.frameB7,self.frameB8,self.frameB9,self.B10]
        self.Cs=[self.frameC1,self.frameC2,self.frameC3,self.frameC4,self.frameC5,self.frameC6,self.frameC7,self.frameC8,self.frameC9,self.C10]
        self.Ds=[self.frameD1,self.frameD2,self.frameD3,self.frameD4,self.frameD5,self.frameD6,self.frameD7,self.frameD8,self.frameD9,self.D10]
        self.Es=[self.frameE1,self.frameE2,self.frameE3,self.frameE4,self.frameE5,self.frameE6,self.frameE7,self.frameE8,self.frameE9,self.E10]
        self.Fs=[self.frameF1,self.frameF2,self.frameF3,self.frameF4,self.frameF5,self.frameF6,self.frameF7,self.frameF8,self.frameF9,self.F10]
        self.Gs=[self.frameG1,self.frameG2,self.frameG3,self.frameG4,self.frameG5,self.frameG6,self.frameG7,self.frameG8,self.frameG9,self.G10]
        self.Hs=[self.frameH1,self.frameH2,self.frameH3,self.frameH4,self.frameH5,self.frameH6,self.frameH7,self.frameH8,self.frameH9,self.H10]
        self.Is=[self.frameI1,self.frameI2,self.frameI3,self.frameI4,self.frameI5,self.frameI6,self.frameI7,self.frameI8,self.frameI9,self.I10]
        self.Js=[self.frameJ1,self.frameJ2,self.frameJ3,self.frameJ4,self.frameJ5,self.frameJ6,self.frameJ7,self.frameJ8,self.frameJ9,self.J10]
        self.L1s=[self.frameA1,self.frameB1,self.frameC1,self.frameD1,self.frameE1,self.frameF1,self.frameG1,self.frameH1,self.frameI1,self.frameJ1]
        self.L2s=[self.frameA2,self.frameB2,self.frameC2,self.frameD2,self.frameE2,self.frameF2,self.frameG2,self.frameH2,self.frameI2,self.frameJ2]
        self.L3s=[self.frameA3,self.frameB3,self.frameC3,self.frameD3,self.frameE3,self.frameF3,self.frameG3,self.frameH3,self.frameI3,self.frameJ3]
        self.L4s=[self.frameA4,self.frameB4,self.frameC4,self.frameD4,self.frameE4,self.frameF4,self.frameG4,self.frameH4,self.frameI4,self.frameJ4]
        self.L5s=[self.frameA5,self.frameB5,self.frameC5,self.frameD5,self.frameE5,self.frameF5,self.frameG5,self.frameH5,self.frameI5,self.frameJ5]
        self.L6s=[self.frameA6,self.frameB6,self.frameC6,self.frameD6,self.frameE6,self.frameF6,self.frameG6,self.frameH6,self.frameI6,self.frameJ6]
        self.L7s=[self.frameA7,self.frameB7,self.frameC7,self.frameD7,self.frameE7,self.frameF7,self.frameG7,self.frameH7,self.frameI7,self.frameJ7]
        self.L8s=[self.frameA8,self.frameB8,self.frameC8,self.frameD8,self.frameE8,self.frameF8,self.frameG8,self.frameH8,self.frameI8,self.frameJ8]
        self.L9s=[self.frameA9,self.frameB9,self.frameC9,self.frameD9,self.frameE9,self.frameF9,self.frameG9,self.frameH9,self.frameI9,self.frameJ9]
        self.L10s=[self.frameA10,self.frameB10,self.frameC10,self.frameD10,self.frameE10,self.frameF10,self.frameG10,self.frameH10,self.frameI10,self.frameJ10]
        #-------------
        self.n=20
        #--------
        self.gerarPA()
        self.gerar4c()
        self.gerar3c()
        self.gerar2c()
        self.gerar1c()
        
    def gerarPA(self):
        posicao=['Cima','Baixo','Direita','Esquerda']
        choose=random.choice(posicao)
        if choose=='Cima':
            while True:
                navio1=random.choice(self.posicao)
                try:
                    if navio1 in self.L10s or navio1  in self.L9s:
                        raise myError
                    elif navio1 in self.As or navio1 in self.Js:
                        raise myError
                except myError:
                    navio1=random.choice(self.posicao)
                else:
                    break
            navio1['bg']='#3CB371'
            self.navios.append(navio1)
            momentaneo2=self.posicao.index(navio1)+10
            navio2=self.posicao[momentaneo2]
            navio2['bg']='#3CB371'
            self.navios.append(navio2)
            momentaneo3=self.posicao.index(navio1)+20
            navio3=self.posicao[momentaneo3]
            navio3['bg']='#3CB371'
            self.navios.append(navio3)
            momentaneo4=self.posicao.index(navio1)+1
            navio4=self.posicao[momentaneo4]
            navio4['bg']='#3CB371'
            self.navios.append(navio4)
            momentaneo5=self.posicao.index(navio1)-1
            navio5=self.posicao[momentaneo5]
            navio5['bg']='#3CB371'
            self.navios.append(navio5)
        elif choose=='Baixo':
            while True:
                navio1=random.choice(self.posicao)
                try:
                    if navio1 in self.L1s or navio1  in self.L2s:
                        raise myError
                    elif navio1 in self.As or navio1 in self.Js:
                        raise myError
                except myError:
                    navio1=random.choice(self.posicao)
                else:
                    break
            navio1['bg']='#3CB371'
            self.navios.append(navio1)
            momentaneo2=self.posicao.index(navio1)-10
            navio2=self.posicao[momentaneo2]
            navio2['bg']='#3CB371'
            self.navios.append(navio2)
            momentaneo3=self.posicao.index(navio1)-20
            navio3=self.posicao[momentaneo3]
            navio3['bg']='#3CB371'
            self.navios.append(navio3)
            momentaneo4=self.posicao.index(navio1)+1
            navio4=self.posicao[momentaneo4]
            navio4['bg']='#3CB371'
            self.navios.append(navio4)
            momentaneo5=self.posicao.index(navio1)-1
            navio5=self.posicao[momentaneo5]
            navio5['bg']='#3CB371'
            self.navios.append(navio5)
        elif choose=='Direita':
            while True:
                navio1=random.choice(self.posicao)
                try:
                    if navio1 in self.L1s or navio1  in self.L10s:
                        raise myError
                    elif navio1 in self.As or navio1 in self.Bs:
                        raise myError
                except myError:
                    navio1=random.choice(self.posicao)
                else:
                    break
            navio1['bg']='#3CB371'
            self.navios.append(navio1)
            momentaneo2=self.posicao.index(navio1)-10
            navio2=self.posicao[momentaneo2]
            navio2['bg']='#3CB371'
            self.navios.append(navio2)
            momentaneo3=self.posicao.index(navio1)+10
            navio3=self.posicao[momentaneo3]
            navio3['bg']='#3CB371'
            self.navios.append(navio3)
            momentaneo4=self.posicao.index(navio1)-2
            navio4=self.posicao[momentaneo4]
            navio4['bg']='#3CB371'
            self.navios.append(navio4)
            momentaneo5=self.posicao.index(navio1)-1
            navio5=self.posicao[momentaneo5]
            navio5['bg']='#3CB371'
            self.navios.append(navio5)
        elif choose=='Esquerda':
            while True:
                navio1=random.choice(self.posicao)
                try:
                    if navio1 in self.L1s or navio1  in self.L10s:
                        raise myError
                    elif navio1 in self.Is or navio1 in self.Js:
                        raise myError
                except myError:
                    navio1=random.choice(self.posicao)
                else:
                    break
            navio1['bg']='#3CB371'
            self.navios.append(navio1)
            momentaneo2=self.posicao.index(navio1)-10
            navio2=self.posicao[momentaneo2]
            navio2['bg']='#3CB371'
            self.navios.append(navio2)
            momentaneo3=self.posicao.index(navio1)+10
            navio3=self.posicao[momentaneo3]
            navio3['bg']='#3CB371'
            self.navios.append(navio3)
            momentaneo4=self.posicao.index(navio1)+2
            navio4=self.posicao[momentaneo4]
            navio4['bg']='#3CB371'
            self.navios.append(navio4)
            momentaneo5=self.posicao.index(navio1)+1
            navio5=self.posicao[momentaneo5]
            navio5['bg']='#3CB371'
            self.navios.append(navio5)
    def gerar4c(self):
        posicao=['Pe','Deitado']
        choose=random.choice(posicao)
        if choose=='Pe':
            while True:
                navio6=random.choice(self.posicao)
                try:
                    if navio6 in self.navios:
                        raise myError
                    elif navio6 in self.L8s or navio6 in self.L9s or navio6 in self.L10s:
                        raise myError
                except myError:
                    navio6=random.choice(self.posicao)
                else:
                    momentaneo7=self.posicao.index(navio6)+10
                    momentaneo8=self.posicao.index(navio6)+20
                    momentaneo9=self.posicao.index(navio6)+30
                    while True:
                        try:
                            navio7=self.posicao[momentaneo7]
                            navio8=self.posicao[momentaneo8]
                            navio9=self.posicao[momentaneo9]
                            if navio7 in self.navios or navio8 in self.navios or navio9 in self.navios:
                                raise myError
                            elif navio6 in self.navios:
                                raise myError
                            elif navio6 in self.L8s or navio6 in self.L9s or navio6 in self.L10s:
                                raise myError
                        except myError:
                            navio6=random.choice(self.posicao)
                            momentaneo7=self.posicao.index(navio6)+10
                            momentaneo8=self.posicao.index(navio6)+20
                            momentaneo9=self.posicao.index(navio6)+30
                        except IndexError:
                            navio6=random.choice(self.posicao)
                            momentaneo7=self.posicao.index(navio6)+10
                            momentaneo8=self.posicao.index(navio6)+20
                            momentaneo9=self.posicao.index(navio6)+30                            
                        else:
                            break
                    break
            navio6['bg']='#7FFF00'
            self.navios.append(navio6)
            navio7['bg']='#7FFF00'
            self.navios.append(navio7)
            self.navios.append(navio8)
            navio8['bg']='#7FFF00'
            navio9['bg']='#7FFF00'
            self.navios.append(navio9)
        elif choose=='Deitado':
            while True:
                navio6=random.choice(self.posicao)
                try:
                    if navio6 in self.navios:
                        raise myError
                    elif navio6 in self.Hs or navio6 in self.Js or navio6 in self.Is:
                        raise myError
                except myError:
                    navio6=random.choice(self.posicao)
                else:
                    momentaneo7=self.posicao.index(navio6)+1
                    momentaneo8=self.posicao.index(navio6)+2
                    momentaneo9=self.posicao.index(navio6)+3
                    while True:
                        try:
                            navio7=self.posicao[momentaneo7]
                            navio8=self.posicao[momentaneo8]
                            navio9=self.posicao[momentaneo9]
                            if navio7 in self.navios or navio8 in self.navios or navio9 in self.navios:
                                raise myError
                            elif navio6 in self.navios:
                                raise myError
                            elif navio6 in self.Hs or navio6 in self.Js or navio6 in self.Is:
                                raise myError
                        except myError:
                            navio6=random.choice(self.posicao)
                            momentaneo7=self.posicao.index(navio6)+1
                            momentaneo8=self.posicao.index(navio6)+2
                            momentaneo9=self.posicao.index(navio6)+3
                        except IndexError:
                            navio6=random.choice(self.posicao)
                            momentaneo7=self.posicao.index(navio6)+1
                            momentaneo8=self.posicao.index(navio6)+2
                            momentaneo9=self.posicao.index(navio6)+3
                        else:
                            break
                    break
            navio6['bg']='#7FFF00'
            self.navios.append(navio6)
            navio7['bg']='#7FFF00'
            self.navios.append(navio7)
            self.navios.append(navio8)
            navio8['bg']='#7FFF00'
            navio9['bg']='#7FFF00'
            self.navios.append(navio9)
    def gerar3c(self):
        posicao=['Pe','Deitado']
        #1 navio de 3 canos
        choose=random.choice(posicao)
        if choose=='Pe':
            while True:
                navio10=random.choice(self.posicao)
                try:
                    if navio10 in self.navios:
                        raise myError
                    elif navio10 in self.L1s or navio10 in self.L10s:
                        raise myError
                except myError:
                    navio10=random.choice(self.posicao)
                else:
                    momentaneo11=self.posicao.index(navio10)-10
                    momentaneo12=self.posicao.index(navio10)+10
                    while True:
                        try:
                            navio11=self.posicao[momentaneo11]
                            navio12=self.posicao[momentaneo12]
                            if navio11 in self.navios or navio12 in self.navios:
                                raise myError
                            elif navio10 in self.navios:
                                raise myError
                            elif navio10 in self.L1s or navio10 in self.L10s:
                                raise myError
                        except myError:
                            navio10=random.choice(self.posicao)
                            momentaneo11=self.posicao.index(navio10)-10
                            momentaneo12=self.posicao.index(navio10)+10
                        except IndexError:
                            navio10=random.choice(self.posicao)
                            momentaneo11=self.posicao.index(navio10)-10
                            momentaneo12=self.posicao.index(navio10)+10
                        else:
                            break
                    break
            navio10['bg']='#008000'
            self.navios.append(navio10)
            navio11['bg']='#008000'
            self.navios.append(navio11)
            navio12['bg']='#008000'
            self.navios.append(navio12)
        if choose=='Deitado':
            while True:
                navio10=random.choice(self.posicao)
                try:
                    if navio10 in self.navios:
                        raise myError
                    elif navio10 in self.As or navio10 in self.Js:
                        raise myError
                except myError:
                    navio10=random.choice(self.posicao)
                else:
                    momentaneo11=self.posicao.index(navio10)-1
                    momentaneo12=self.posicao.index(navio10)+1
                    while True:
                        try:
                            navio11=self.posicao[momentaneo11]
                            navio12=self.posicao[momentaneo12]
                            if navio11 in self.navios or navio12 in self.navios:
                                raise myError
                            elif navio10 in self.navios:
                                raise myError
                            elif navio10 in self.As or navio10 in self.Js:
                                raise myError
                        except myError:
                            navio10=random.choice(self.posicao)
                            momentaneo11=self.posicao.index(navio10)-1
                            momentaneo12=self.posicao.index(navio10)+1
                        except IndexError:
                            navio10=random.choice(self.posicao)
                            momentaneo11=self.posicao.index(navio10)-1
                            momentaneo12=self.posicao.index(navio10)+1
                        else:
                            break
                    break
            navio10['bg']='#008000'
            self.navios.append(navio10)
            navio11['bg']='#008000'
            self.navios.append(navio11)
            navio12['bg']='#008000'
            self.navios.append(navio12)
        #2 navio de 3 canos
        choose1=random.choice(posicao)
        if choose1=='Pe':
            while True:
                navio13=random.choice(self.posicao)
                try:
                    if navio13 in self.navios:
                        raise myError
                    elif navio13 in self.L1s or navio13 in self.L10s:
                        raise myError
                except myError:
                    navio13=random.choice(self.posicao)
                else:
                    momentaneo14=self.posicao.index(navio13)-10
                    momentaneo15=self.posicao.index(navio13)+10
                    while True:
                        try:
                            navio14=self.posicao[momentaneo14]
                            navio15=self.posicao[momentaneo15]
                            if navio14 in self.navios or navio15 in self.navios:
                                raise myError
                            if navio13 in self.navios:
                                raise myError
                            elif navio13 in self.L1s or navio13 in self.L10s:
                                raise myError
                        except myError:
                            navio13=random.choice(self.posicao)
                            momentaneo14=self.posicao.index(navio13)-10
                            momentaneo15=self.posicao.index(navio13)+10
                        except IndexError:
                            navio13=random.choice(self.posicao)
                            momentaneo14=self.posicao.index(navio13)-10
                            momentaneo15=self.posicao.index(navio13)+10
                        else:
                            break
                    break
            navio13['bg']='#008000'
            self.navios.append(navio13)
            navio14['bg']='#008000'
            self.navios.append(navio14)
            navio15['bg']='#008000'
            self.navios.append(navio15)
        if choose1=='Deitado':
            while True:
                navio13=random.choice(self.posicao)
                try:
                    if navio13 in self.navios:
                        raise myError
                    elif navio13 in self.As or navio13 in self.Js:
                        raise myError
                except myError:
                    navio13=random.choice(self.posicao)
                else:
                    momentaneo14=self.posicao.index(navio13)-1
                    momentaneo15=self.posicao.index(navio13)+1
                    while True:
                        try:
                            navio14=self.posicao[momentaneo14]
                            navio15=self.posicao[momentaneo15]
                            if navio14 in self.navios or navio15 in self.navios:
                                raise myError
                            elif navio13 in self.navios:
                                raise myError
                            elif navio13 in self.As or navio13 in self.Js:
                                raise myError
                        except myError:
                            navio13=random.choice(self.posicao)
                            momentaneo14=self.posicao.index(navio13)-1
                            momentaneo15=self.posicao.index(navio13)+1
                        except IndexError:
                            navio13=random.choice(self.posicao)
                            momentaneo14=self.posicao.index(navio13)-1
                            momentaneo15=self.posicao.index(navio13)+1                            
                        else:
                            break
                    break
            navio13['bg']='#008000'
            self.navios.append(navio13)
            navio14['bg']='#008000'
            self.navios.append(navio14)
            navio15['bg']='#008000'
            self.navios.append(navio15)
    def gerar2c(self):
        posicao=['Pe','Deitado']
        #1 navio de 2 canos
        choose=random.choice(posicao)
        if choose=='Pe':
            while True:
                navio16=random.choice(self.posicao)
                try:
                    if navio16 in self.navios:
                        raise myError
                    elif navio16 in self.L10s:
                        raise myError
                except:
                    navio16=random.choice(self.posicao)
                else:
                    momentaneo17=self.posicao.index(navio16)+10
                    while True:
                        try:
                            navio17=self.posicao[momentaneo17]
                            if navio17 in self.navios:
                                raise myError
                            elif navio16 in self.navios:
                                raise myError
                            elif navio16 in self.L10s:
                                raise myError
                        except myError:
                            navio16=random.choice(self.posicao)
                            momentaneo17=self.posicao.index(navio16)+10
                        except IndexError:
                            navio16=random.choice(self.posicao)
                            momentaneo17=self.posicao.index(navio16)+10                            
                        else:
                            break
                    break
            navio16['bg']='#98FB98'
            self.navios.append(navio16)
            navio17['bg']='#98FB98'
            self.navios.append(navio17)
        if choose=='Deitado':
            while True:
                navio16=random.choice(self.posicao)
                try:
                    if navio16 in self.navios:
                        raise myError
                    elif navio16 in self.Js:
                        raise myError
                except:
                    navio16=random.choice(self.posicao)
                else:
                    momentaneo17=self.posicao.index(navio16)+1
                    while True:
                        try:
                            navio17=self.posicao[momentaneo17]
                            if navio17 in self.navios:
                                raise myError
                            elif navio16 in self.navios:
                                raise myError
                            elif navio16 in self.Js:
                                raise myError
                        except myError:
                            navio16=random.choice(self.posicao)
                            momentaneo17=self.posicao.index(navio16)+1
                        except IndexError:
                            navio16=random.choice(self.posicao)
                            momentaneo17=self.posicao.index(navio16)+1                            
                        else:
                            break
                    break
            navio16['bg']='#98FB98'
            self.navios.append(navio16)
            navio17['bg']='#98FB98'
            self.navios.append(navio17)
        #2 navio de 2 canos
        choose1=random.choice(posicao)
        if choose1=='Pe':
            while True:
                navio18=random.choice(self.posicao)
                try:
                    if navio18 in self.navios:
                        raise myError
                    elif navio18 in self.L10s:
                        raise myError
                except:
                    navio18=random.choice(self.posicao)
                else:
                    momentaneo19=self.posicao.index(navio18)+10
                    while True:
                        try:
                            navio19=self.posicao[momentaneo19]
                            if navio19 in self.navios:
                                raise myError
                            elif navio18 in self.navios:
                                raise myError
                            elif navio18 in self.L10s:
                                raise myError
                        except myError:
                            navio18=random.choice(self.posicao)
                            momentaneo19=self.posicao.index(navio18)+10
                        except IndexError:
                            navio18=random.choice(self.posicao)
                            momentaneo19=self.posicao.index(navio18)+10
                        else:
                            break
                    break
            navio18['bg']='#98FB98'
            self.navios.append(navio18)
            navio19['bg']='#98FB98'
            self.navios.append(navio19)
        if choose1=='Deitado':
            while True:
                navio18=random.choice(self.posicao)
                try:
                    if navio18 in self.navios:
                        raise myError
                    elif navio18 in self.Js:
                        raise myError
                except:
                    navio18=random.choice(self.posicao)
                else:
                    momentaneo19=self.posicao.index(navio18)+1
                    while True:
                        try:
                            navio19=self.posicao[momentaneo19]
                            if navio19 in self.navios:
                                raise myError
                            elif navio18 in self.navios:
                                raise myError
                            elif navio18 in self.Js:
                                raise myError
                        except myError:
                            navio18=random.choice(self.posicao)
                            momentaneo19=self.posicao.index(navio18)+1
                        except IndexError:
                            navio18=random.choice(self.posicao)
                            momentaneo19=self.posicao.index(navio18)+1
                        else:
                            break
                    break
            navio18['bg']='#98FB98'
            self.navios.append(navio18)
            navio19['bg']='#98FB98'
            self.navios.append(navio19)
        #3 navio de 2 canos
        choose2=random.choice(posicao)
        if choose1=='Pe':
            while True:
                navio20=random.choice(self.posicao)
                try:
                    if navio20 in self.navios:
                        raise myError
                    elif navio20 in self.L10s:
                        raise myError
                except:
                    navio20=random.choice(self.posicao)
                else:
                    momentaneo21=self.posicao.index(navio20)+10
                    while True:
                        try:
                            navio21=self.posicao[momentaneo21]
                            if navio21 in self.navios:
                                raise myError
                            elif navio20 in self.navios:
                                raise myError
                            elif navio20 in self.L10s:
                                raise myError
                        except myError:
                            navio20=random.choice(self.posicao)
                            momentaneo21=self.posicao.index(navio20)+10
                        except IndexError:
                            navio20=random.choice(self.posicao)
                            momentaneo21=self.posicao.index(navio20)+10
                        else:
                            break
                    break
            navio20['bg']='#98FB98'
            self.navios.append(navio20)
            navio21['bg']='#98FB98'
            self.navios.append(navio21)
        if choose1=='Deitado':
            while True:
                navio20=random.choice(self.posicao)
                try:
                    if navio20 in self.navios:
                        raise myError
                    elif navio20 in self.Js:
                        raise myError
                except:
                    navio20=random.choice(self.posicao)
                else:
                    momentaneo21=self.posicao.index(navio20)+1
                    while True:
                        try:
                            navio21=self.posicao[momentaneo21]
                            if navio21 in self.navios:
                                raise myError
                            elif navio20 in self.navios:
                                raise myError
                            elif navio20 in self.Js:
                                raise myError
                        except myError:
                            navio20=random.choice(self.posicao)
                            momentaneo21=self.posicao.index(navio20)+1
                        except IndexError:
                            navio20=random.choice(self.posicao)
                            momentaneo21=self.posicao.index(navio20)+1                            
                        else:
                            break
                    break
            navio20['bg']='#98FB98'
            self.navios.append(navio20)
            navio21['bg']='#98FB98'
            self.navios.append(navio21)
    def gerar1c(self):
        #1 navio de 1 cano
        while True:
            navio22=random.choice(self.posicao)
            try:
                if navio22 in self.navios:
                    raise myError
            except myError:
                navio22=random.choice(self.posicao)
            else:
                break
        navio22['bg']='#6B8E23'
        self.navios.append(navio22)
        #2 navio de 1 cano
        while True:
            navio23=random.choice(self.posicao)
            try:
                if navio23 in self.navios:
                    raise myError
            except myError:
                navio23=random.choice(self.posicao)
            else:
                break
        navio23['bg']='#6B8E23'
        self.navios.append(navio23)
        #3 navio de 1 cano
        while True:
            navio24=random.choice(self.posicao)
            try:
                if navio24 in self.navios:
                    raise myError
            except myError:
                navio24=random.choice(self.posicao)
            else:
                break
        navio24['bg']='#6B8E23'
        self.navios.append(navio24)
        #4 navio de 1 cano
        while True:
            navio25=random.choice(self.posicao)
            try:
                if navio25 in self.navios:
                    raise myError
            except myError:
                navio25=random.choice(self.posicao)
            else:
                break
        navio25['bg']='#6B8E23'
        self.navios.append(navio25)
    def destruir(self,botao,frame):
        botao.destroy()
        if len(self.navios)==1 and frame in self.navios:##Coloquei a mais
            messagebox.showinfo('Jogar novamente?','Você ganhou, parabéns.')
            self.master.destroy()
        elif self.navios!=[]:##Coloquei a mais
            if self.n>=1:
                if frame in self.navios:
                    #print 'Uhul!'
                    self.n+=1
                    self.labelf1n['text']='Uma parte de um navio foi destruída, agora você possui '+str(self.n)+' tiros de canhão.'
                    #print self.n
                    self.navios.remove(frame)###Coloquei a mais
                else:
                    #print 'Agua'
                    self.n-=1
                    if self.n>0:
                        self.labelf1n['text']='Tiro ao mar, agora você possui '+str(self.n)+' tiros de canhão.'
                        #print self.n
                    elif self.n==0:
                        self.labelf1n['text']='Seus tiros de canhões acabaram, fim de jogo.'
                        messagebox.showinfo('Tente Novamente','Você perdeu.')
                        self.master.destroy()
        

    #CORES    
    #3CB371
    #7FFF00
    #008000
    #6B8E23
    #98FB98
root = Tk()
root.title('Batalha Naval')
jogo = BatalhaNaval(root)
root.mainloop()
