from tkinter import *

root = Tk()
root.title("Calculadora Simples")

# Área de funções:


def botao_click(num):

	# evitar os numeros entrarem ao contrário na tela.
	x = e.get()
	e.delete(0, END)
	e.insert(0,str(x) + str(num))
	
	return

def botao_limpar():

	e.delete(0, END)

def botao_somar():
	primeiro_numero = e.get() 
	global p_num
	global operador
	operador = "adicao"
	p_num = float(primeiro_numero)
	e.delete(0, END)

def botao_sub():
	primeiro_numero = e.get() 
	global p_num
	global operador
	operador = "subtracao"
	p_num = float(primeiro_numero)
	e.delete(0, END)

def botao_multi():
	primeiro_numero = e.get() 
	global p_num
	global operador
	operador = "multiplicacao"
	p_num = float(primeiro_numero)
	e.delete(0, END)

def botao_div():
	primeiro_numero = e.get() 
	global p_num
	global operador
	operador = "divisao"
	p_num = float(primeiro_numero)
	e.delete(0, END)

def botao_igual():

	segundo_numero = e.get()
	e.delete(0, END)
	if operador == "adicao":
		e.insert(0, p_num + float(segundo_numero))
	elif operador == "subtracao":
		e.insert(0, p_num - float(segundo_numero))
	elif operador == "multiplicacao":
		e.insert(0, p_num * float(segundo_numero))
	elif operador == "divisao":
		e.insert(0, p_num / float(segundo_numero))

#----------------------------------------------------------------------------------

	#Definir botões
botao_1 = Button(root, text="1", padx=40, pady=20, command=lambda: botao_click(1))
botao_2 = Button(root, text="2", padx=40, pady=20, command=lambda: botao_click(2))
botao_3 = Button(root, text="3", padx=40, pady=20, command=lambda: botao_click(3))
botao_4 = Button(root, text="4", padx=40, pady=20, command=lambda: botao_click(4))
botao_5 = Button(root, text="5", padx=40, pady=20, command=lambda: botao_click(5))
botao_6 = Button(root, text="6", padx=40, pady=20, command=lambda: botao_click(6))
botao_7 = Button(root, text="7", padx=40, pady=20, command=lambda: botao_click(7))
botao_8 = Button(root, text="8", padx=40, pady=20, command=lambda: botao_click(8))
botao_9 = Button(root, text="9", padx=40, pady=20, command=lambda: botao_click(9))
botao_0 = Button(root, text="0", padx=40, pady=20, command=lambda: botao_click(0))
botao_ponto = Button(root, text=".", padx=40, pady=20, command=lambda: botao_click("."))
botao_add = Button(root, text="+", padx=40, pady=20, command=botao_somar)
botao_igual = Button(root, text="=", padx=80, pady=20, command=botao_igual)
botao_limpar = Button(root, text="Limpar", padx=80, pady=20, command=botao_limpar)
botao_sub = Button(root, text="-", padx=40, pady=20, command=botao_sub)
botao_multi = Button(root, text="x", padx=40, pady=20, command=botao_multi)
botao_div = Button(root, text="/", padx=40, pady=20, command=botao_div)

# Colocar os botões na tela

botao_1.grid(row=3, column=0)
botao_2.grid(row=3, column=1)
botao_3.grid(row=3, column=2)

botao_4.grid(row=2, column=0)
botao_5.grid(row=2, column=1)
botao_6.grid(row=2, column=2)

botao_7.grid(row=1, column=0)
botao_8.grid(row=1, column=1)
botao_9.grid(row=1, column=2)

botao_0.grid(row=4, column=0)

botao_add.grid(row=2, column=4)
botao_ponto.grid(row=4, column=1)
botao_igual.grid(row=4, column=3, columnspan=2)
botao_limpar.grid(row=1, column=3, columnspan=2)
botao_sub.grid(row=3, column=4)
botao_multi.grid(row=2, column=3)
botao_div.grid(row=3, column=3)


# Criando o input para entrada de dados
#e = Entry(root, bg="black", fg="white" width=50)
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0,column=1, columnspan=3, padx=10, pady=10)





root.mainloop()