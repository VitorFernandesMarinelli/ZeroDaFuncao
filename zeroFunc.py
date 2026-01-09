import tkinter as tk
from tkinter import messagebox
import re
import math



#region UI
class MyWindow:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Calculadora zero da função")
        self.criar_interface()
    def criar_interface(self):
        # Configuração da fonte para o título
        fonte_titulo = ("Helvetica", 18, "bold")

        # Criação do título centralizado
        titulo = tk.Label(self.janela, text="Calculadora zero da fução", font=fonte_titulo)
        titulo.grid(row=0, column=0, columnspan=4)

        # Criação dos textos acima de cada campo
        texto_label1 = tk.Label(self.janela, text="Função:")
        texto_label1.grid(row=1, column=0)
        texto_label2 = tk.Label(self.janela, text="A:")
        texto_label2.grid(row=1, column=1)
        texto_label3 = tk.Label(self.janela, text="B:")
        texto_label3.grid(row=1, column=2)
        texto_label4 = tk.Label(self.janela, text="Erro:")
        texto_label4.grid(row=1, column=3)

        # Criação dos campos de texto
        self.campo1 = tk.Entry(self.janela)
        self.campo1.grid(row=2, column=0)
        self.campo2 = tk.Entry(self.janela)
        self.campo2.grid(row=2, column=1)
        self.campo3 = tk.Entry(self.janela)
        self.campo3.grid(row=2, column=2)
        self.campo4 = tk.Entry(self.janela)
        self.campo4.grid(row=2, column=3)

        # Botão 
        botao = tk.Button(self.janela, text="Calcular", command=self.calcular)
        botao.grid(row=3, column=0, columnspan=4)

    #ação do botão
    def calcular(self):
        
        try: 
            func = criarFunc(self.campo1.get())
            a = float(self.campo2.get())
            b = float(self.campo3.get())
            erro = float(self.campo4.get())
            mensagem = IniciarCalculo(a,b,func,erro)
        except Exception as e:
            mensagem = "Os valores digitados estão incorretos!\nPor favor digite os valores corretos"

        
        messagebox.showinfo("Interações", mensagem)

    def iniciar(self):
        self.janela.mainloop()

#endregion

#region tratamento da função
def criarFunc(tf):
    f = arrumar_func(tf)
    return lambda x: eval(f)


def arrumar_func(f):
  a = f
  a = a.replace('^', '**')
  a = a.replace('sen','math.sin')
  a = a.replace('cos','math.cos')
  a = a.replace('tg','math.tan')
  a = a.replace('π', 'math.pi')
  a = a.replace('e', 'math.e')
  a = a.replace('!', 'math.factorial')
  a = a.replace('log', 'math.log10')
  a = raizes(a)
  return a

def raizes(f):
   regex = r'\[(\d+)\]√\((.+?)\)'
   a = lambda match: f'math.pow(({match.group(2)}), 1/{match.group(1)})'
   resultado = re.sub(regex,a,f)
   return resultado
#endregion

#region calculo do zero da função
def IniciarCalculo(a,b,f,erro):
    x = (a+b)/2
    er = abs(a-b)
    if(Bolzano(f,a,x) == 1):
        return calcular(a,x,f,erro,1,x,er,f"\n{0}º [{a},{b}]    x = {x}    e{er}")
    else:
        return calcular(x,b,f,erro,1,x,er,f"\n{0}º [{a},{b}]    x = {x}    e{er}")


def calcular(a,b,f,erroM,i,anterior,erro,mensagem):
    #divisão do intervalo
    x = (a+b)/2 
    intervaloRaiz = Bolzano(f,a,x)
    erro = abs(x-anterior)
    if((b-a<=erroM)): 
        mensagem = mensagem + f"\n Resulador final = {x}  e = {erro}\n\n"
        return mensagem
    else:

        mensagem = mensagem + f"\n{i}º [{a}, {b}]   x = {x}   e = {erro}"
        i = i+1
        
        if(intervaloRaiz == 1):
            return calcular(a,x,f,erroM,i,x,erro,mensagem)
        else:
            return calcular(x,b,f,erroM,i,x,erro,mensagem)
        


def Bolzano(f,a,x):
    #aplicação das funções
    yA = f(a)
    yX = f(x)
    intervalo1 = yA*yX 
    #verificação do intervalo
    if(intervalo1 < 0):
        intervalo = 1
    else:
        intervalo = 2

    return intervalo

#endregion

# Iniciar o loop principal da janela
janela = MyWindow()
janela.iniciar()
