import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
#from kivy.image import Image
#from kivy.uix.floatlayout import FloatLayout


# Set the app size
Window.size = (500,700)


Builder.load_file('calc.kv')


class MyLayout(Widget):
	
	def clear(self):
		self.ids.calc_input.text = '0'
	#Função que cria a resposta para o pressionamento dos botões
	
	def button_press(self, button):
		#criar a varável do TextBox primeira.
		prior = self.ids.calc_input.text
		if "Erro" in prior:
			prior = ' '
		#código para digitar vários algarismos na tela.
		
		if prior == "0":
			self.ids.calc_input.text = ''
			self.ids.calc_input.text = f'{button}'
		else:
			self.ids.calc_input.text = f'{prior}{button}'
	
	
	#Função para desligar
	def off(self):
		exit()
	
	
	#Funão para +/- 
	def pos_negative(self):
		prior = self.ids.calc_input.text
		
		if "-" in prior:
			self.ids.calc_input.text = f'{prior.replace("-","")}'
		else:
			self.ids.calc_input.text = f'-{prior}'
		
	
	#Função para remover dígito a dígito
	def remove(self):
		
		prior = self.ids.calc_input.text
		prior = prior[:-1]
		#esse codigo é sempre para devolver para o TexBox o valor processado
		self.ids.calc_input.text = prior
		
		if prior == '':
			
			self.ids.calc_input.text = "0"
		
	
	
	
	#Funçao para adicionar números decimais à calculadora
	def ponto(self):
				
		prior = self.ids.calc_input.text
		num_list = prior.split("+")
		#dispositivo para só poder colocar um ponto.
		
		if "+" in prior and "." not in num_list[-1]:
			prior = f'{prior}.'
			self.ids.calc_input.text = prior
		
		elif "." in prior:
			pass
		else:
			prior = f'{prior}.'
			self.ids.calc_input.text = prior	
	
	def math_sign(self, sign):
		
		prior = self.ids.calc_input.text
		self.ids.calc_input.text = f'{prior}{sign}'
			
	def igual(self):
		prior = self.ids.calc_input.text
		
	
		try:
			# A funçao 'eval' avaliará a matemática do texto
			answer = eval(prior)
		
			#output
			self.ids.calc_input.text = str(answer)
		except:
			
			self.ids.calc_input.text = "Erro"
		
	
	
#Esta parte do código abaixo é para o app ir à tela.
class CalculadoraApp(App):
	def build(self):
		#cor do main layout
		#Window.clearcolor = (1,1,1,1)
		return MyLayout()


if __name__ == '__main__':
	CalculadoraApp().run()
