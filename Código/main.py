from tkinter import *

class Calc:
    def __init__(self):
        # Cria a janela principal
        self.window = Tk()
        self.window.title("Calculadora")
        self.window.resizable(0,0)

        # Cria a entrada de texto para os números
        self.num = Entry(self.window, font="arial 20 bold", bg="#1f2b30", fg="white", width=16)
        self.num.pack()

        # Cria um frame para os botões
        self.frame = Frame(self.window)
        self.frame.pack()

        # Cria os botões numéricos e os botões de operações
        # Cada botão chama a função 'touch' com um número ou operação específica
        # Os botões são adicionados ao frame
        # O comando 'lambda' é usado para passar argumentos para a função 'touch'
        self.button_1 = Button(self.frame, bg="orange", text="1", font="arial 20 bold", width="3", height=1, command=lambda: self.touch('1'), fg="white")

        self.button_2 = Button(self.frame, bg="orange", text="2", font="arial 20 bold", width="3", height=1, command=lambda: self.touch('2'), fg="white")

        self.button_3 = Button(self.frame, bg="orange", text="3", font="arial 20 bold", width="3", height=1, command=lambda: self.touch('3'), fg="white")

        self.button_4 = Button(self.frame, bg="orange", text="4", font="arial 20 bold", width="3", height=1, command=lambda: self.touch('4'), fg="white")

        self.button_5 = Button(self.frame, bg="orange", text="5", font="arial 20 bold", width="3", height=1, command=lambda: self.touch('5'), fg="white")

        self.button_6 = Button(self.frame, bg="orange", text="6", font="arial 20 bold", width="3", height=1, command=lambda: self.touch('6'), fg="white")

        self.button_7 = Button(self.frame, bg="orange", text="7", font="arial 20 bold", width="3", height=1, command=lambda: self.touch('7'), fg="white")

        self.button_8 = Button(self.frame, bg="orange", text="8", font="arial 20 bold", width="3", height=1, command=lambda: self.touch('8'), fg="white")

        self.button_9 = Button(self.frame, bg="orange", text="9", font="arial 20 bold", width="3", height=1, command=lambda: self.touch('9'), fg="white")

        self.button_0 = Button(self.frame, bg="orange", text="0", font="arial 20 bold", width="3", height=1, command=lambda: self.touch('0'), fg="white")

        self.button_soma = Button(self.frame, bg="orange", text="+", font="arial 20 bold", width="3", height=1, command= lambda: self.touch('+'), fg="white")

        self.button_sub = Button(self.frame, bg="orange", text="-", font="arial 20 bold", width="3", height=1, command= lambda: self.touch('-'), fg="white")

        self.button_div = Button(self.frame, bg="orange", text="/", font="arial 20 bold", width="3", height=1, command=lambda: self.touch('/'), fg="white")

        self.button_mult = Button(self.frame, bg="orange", text="*", font="arial 20 bold", width="3", height=1, command=lambda: self.touch('*'), fg="white")

        self.button_igual = Button(self.frame, bg="orange", text="=", font="arial 20 bold", width="3", height=1, command= self.total, fg="white")

        self.button_clean = Button(self.frame, bg="orange", text="C", font="arial 20 bold", width="3", height=1, command=self.Clean, fg="white")

        # Posiciona os botões no grid
        self.button_1.grid(row=0, column=0)
        self.button_2.grid(row=0, column=1)
        self.button_3.grid(row=0, column=2)
        self.button_div.grid(row=0, column=3)
        self.button_4.grid(row=1, column=0)
        self.button_5.grid(row=1, column=1)
        self.button_6.grid(row=1, column=2)
        self.button_mult.grid(row=1, column=3)
        self.button_7.grid(row=2, column=0)
        self.button_8.grid(row=2, column=1)
        self.button_9.grid(row=2, column=2)
        self.button_0.grid(row=3, column=0)
        self.button_sub.grid(row=2, column=3)
        self.button_soma.grid(row=3, column=3)
        self.button_clean.grid(row=3, column=2)
        self.button_igual.grid(row=3, column=1)
        
        self.window.mainloop()

    # Função chamada quando um botão é pressionado
    # Insere o número ou operação na entrada de texto
    def touch(self, n):
        self.num.insert(END,n)

    # Função para limpar a entrada de texto
    def Clean(self):
        self.num.delete(0, END)

    # Função para calcular o total da expressão na entrada de texto
    # Usa a função 'eval' para avaliar a expressão
    def total(self):
        t = eval(self.num.get())
        self.num.delete(0, END)
        self.num.insert(0, str(t))

Calc()