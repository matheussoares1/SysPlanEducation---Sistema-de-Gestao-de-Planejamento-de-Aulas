from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd


# importando pillow
from PIL import ImageTk, Image


# Importando VIew

from view import *


# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # Cinza
co3 = "#20a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # Azul
co7 = "#ef5350"   # Vermelho
co6 = "#038c73"   # verde água
co8 = "#263238"   # Azul Ciano 
co9 = "#f5df4d"   # Amarelo
co10 = "#848484"
co11 = "#ff6600"
co12 = "#84bd91"


# Criando janela
janela = Tk()
janela.title("SysPlanEducation")
janela.geometry('1366x768')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)



style = Style(janela)
style.theme_use("clam")

# Criando Frames
frame_logo = Frame(janela, width=1366, height=52, bg=co2)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_dados = Frame(janela, width=1366, height=65, bg=co2)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_detalhes = Frame(janela, width=1366, height=260, bg=co1)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=1366, height=200, bg=co1)
frame_tabela.grid(row=9, column=0, pady=0, padx=10, sticky=NSEW)



#FRAME LOGO
app_lg = Image.open('logosemmarca.png')
app_lg = app_lg.resize((70,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="  SysPlanEducation", width=1366, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=co10, fg=co1)
app_logo.place(x=0, y=0)


def cadastrar():

	l_tema = Label(frame_detalhes, text="Tema: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_tema.place(x=7, y=30)
	enome_tema = Entry(frame_detalhes, width=35, justify='left', relief='solid')
	enome_tema.place(x=7, y=50)

	l_objetivos = Label(frame_detalhes, text="Objetivos: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_objetivos.place(x=300, y=30)
	enome_objetivos = Entry(frame_detalhes, width=35, justify='left', relief='solid')
	enome_objetivos.place(x=300, y=50)

	l_areaconhecimento = Label(frame_detalhes, text="Área de conhecimento: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_areaconhecimento.place(x=593, y=30)
	enome_areaconehcimento = Entry(frame_detalhes, width=35, justify='left', relief='solid')
	enome_areaconehcimento.place(x=593, y=50)


	l_disciplina = Label(frame_detalhes, text="Disciplina: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_disciplina.place(x=885, y=30)
	enome_disciplina = Entry(frame_detalhes, width=25, justify='left', relief='solid')
	enome_disciplina.place(x=885, y=50)

	l_competencias = Label(frame_detalhes, text="Competências da BNCC: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_competencias.place(x=130, y=85)
	enome_competencias = Entry(frame_detalhes, width=35, justify='left', relief='solid')
	enome_competencias.place(x=130, y=105)

	l_habilidades = Label(frame_detalhes, text="Habilidades da BNCC: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_habilidades.place(x=422, y=85)
	enome_habilidades = Entry(frame_detalhes, width=32, justify='left', relief='solid')
	enome_habilidades.place(x=422, y=105)

	l_objetos = Label(frame_detalhes, text="Objetos de conhecimento: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_objetos.place(x=690, y=85)
	enome_objetos = Entry(frame_detalhes, width=35, justify='left', relief='solid')
	enome_objetos.place(x=690, y=105)


	l_descricao = Label(frame_detalhes, text="Descrição da Aula (metodologia): ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_descricao.place(x=7, y=145)
	enome_descricao = Entry(frame_detalhes, width=45, justify='left', relief='solid')
	enome_descricao.place(x=7, y=165)


	l_recursos = Label(frame_detalhes, text="Recursos: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_recursos.place(x=382, y=145)
	enome_recursos = Entry(frame_detalhes, width=41, justify='left', relief='solid')
	enome_recursos.place(x=382, y=165)


	l_avaliacao = Label(frame_detalhes, text="Avaliação: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_avaliacao.place(x=725, y=145)
	enome_avaliacao = Entry(frame_detalhes, width=45, justify='left', relief='solid')
	enome_avaliacao.place(x=725, y=165)




	# Linha Divisória
	l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=70, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
	l_linha.place(x=1100, y=10)

	l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=70, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
	l_linha.place(x=1099, y=10)

		# Linha Divisória
	l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1325, height=1, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
	l_linha.place(x=7, y=240)

	l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1325, height=1, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
	l_linha.place(x=7, y=240)

	def novo_planejamento():
		tema = enome_tema.get()
		objetivos = enome_objetivos.get()
		area_conhecimento = enome_areaconehcimento.get()
		disciplina = enome_disciplina.get()
		competencias = enome_competencias.get()
		habilidades = enome_habilidades.get()
		objetos = enome_objetos.get()
		descricao = enome_descricao.get()
		recursos = enome_recursos.get()
		avaliacao = enome_avaliacao.get()

		lista_planejamento = [tema, objetivos, area_conhecimento, disciplina, competencias, habilidades, objetos, descricao, recursos, avaliacao]

		# Caso esteja vazio haverá uma tela de insereçao de ddos obrigatórios
		for i in lista_planejamento:
			if i=="":
				messagebox.showerror('Erro', 'Preencha todos os campos.')
				return

		#Inserindo dados no banco de dados 
		inserir_planejamento(lista_planejamento)

		# Mostrando mensagem de sucesso
		messagebox.showinfo('Sucesso', 'Dados inseridos com sucesso!')

		enome_tema.delete(0,END)
		enome_objetivos.delete(0,END)
		enome_areaconehcimento.delete(0,END)
		enome_disciplina.delete(0,END)
		enome_competencias.delete(0,END)
		enome_habilidades.delete(0,END)
		enome_objetos.delete(0,END)
		enome_descricao.delete(0,END)
		enome_recursos.delete(0,END)
		enome_avaliacao.delete(0,END)

		# Mostrando os valores na tabela
		mostrar_planejamento()



	#Atualizar Personal
	def update_planejamenento():
		try:
			tree_itens = tree_personais.focus()
			tree_dicionario = tree_personais.item(tree_itens)
			tree_lista = tree_dicionario['values']

			valor_id = tree_lista[0]


			# Inserindo os valores nas entries
			enome_tema.insert(0, tree_lista[1])
			enome_objetivos.insert(0, tree_lista[2])
			enome_areaconehcimento.insert(0, tree_lista[3])
			enome_disciplina.insert(0, tree_lista[4])
			enome_competencias.insert(0, tree_lista[5])
			enome_habilidades.insert(0, tree_lista[6])
			enome_objetos.insert(0, tree_lista[7])
			enome_descricao.insert(0, tree_lista[8])
			enome_recursos.insert(0, tree_lista[9])
			enome_avaliacao.insert(0, tree_lista[10])


			#função atualizar
			def update():
				tema = enome_tema.get()
				objetivos = enome_objetivos.get()
				area_conhecimento = enome_areaconehcimento.get()
				disciplina = enome_disciplina.get()
				competencias = enome_competencias.get()
				habilidades = enome_habilidades.get()
				objetos = enome_objetos.get()
				descricao = enome_descricao.get()
				recursos = enome_recursos.get()
				avalicao = enome_avaliacao.get()

				lista_planejamento = [tema, objetivos, area_conhecimento, disciplina, competencias, habilidades, objetos, descricao, recursos, avalicao, valor_id]

				# Caso esteja vazio haverá uma tela de insereçao de ddos obrigatórios
				for i in lista_planejamento:
					if i=="":
						messagebox.showerror('Erro', 'Preencha todos os campos.')
						return

				#Inserindo dados no banco de dados 
				atualizar_planejamento(lista_planejamento)

				# Mostrando mensagem de sucesso
				messagebox.showinfo('Sucesso', 'Dados inseridos com sucesso!')

				enome_tema.delete(0,END)
				enome_objetivos.delete(0,END)
				enome_areaconehcimento.delete(0,END)
				enome_disciplina.delete(0,END)
				enome_competencias.delete(0,END)
				enome_habilidades.delete(0,END)
				enome_objetos.delete(0,END)
				enome_descricao.delete(0,END)
				enome_recursos.delete(0,END)
				enome_avaliacao.delete(0,END)


				# Mostrando os valores na tabela
				mostrar_planejamento()

				#Destruindo o Botão Salvar após Salvar os dados
				botao_salvaredit.destroy()


			botao_salvaredit = Button(frame_detalhes,command=update, anchor=CENTER, text="Salvar Atualização".upper(), overrelief=RIDGE, font=('Ivy 7 bold'), bg=co12, fg=co1)
			botao_salvaredit.place(x=1150, y=180)		

		except IndexError:
			messagebox.showerror('Erro', 'Selecione um dos planejamentos na tabela')



	#Deletar Personal
	def delete_planejamento():
		try:
			tree_itens = tree_personais.focus()
			tree_dicionario = tree_personais.item(tree_itens)
			tree_lista = tree_dicionario['values']

			valor_id = tree_lista[0]

			#Deletando dados do banco de dados
			deletar_planejamento([valor_id])

			# Mostrando mensagem de sucesso
			messagebox.showinfo('Sucesso', 'Dados deletados com sucesso!')

			#mostrando os valores na tabela
			mostrar_planejamento()

		except IndexError:
			messagebox.showerror('Erro', 'Selecione um dos planejamentos para deletar')


	def limpar_campos():
	
		enome_tema.delete(0,END)
		enome_objetivos.delete(0,END)
		enome_areaconehcimento.delete(0,END)
		enome_disciplina.delete(0,END)
		enome_competencias.delete(0,END)
		enome_habilidades.delete(0,END)
		enome_objetos.delete(0,END)
		enome_descricao.delete(0,END)
		enome_recursos.delete(0,END)
		enome_avaliacao.delete(0,END)





	# Botões de Salvar, Editar e Deletar
	botao_salvar = Button(frame_detalhes, command=novo_planejamento, anchor=CENTER, text="Salvar".upper(), width=20, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
	botao_salvar.place(x=1150, y=60)


	botao_atualizar = Button(frame_detalhes,command=update_planejamenento, anchor=CENTER, text="Editar".upper(), width=20, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co9, fg=co1)
	botao_atualizar.place(x=1150, y=90)


	botao_deletar = Button(frame_detalhes,command=delete_planejamento, anchor=CENTER, text="Deletar".upper(), width=20, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
	botao_deletar.place(x=1150, y=120)

	botao_limpar = Button(frame_detalhes,command=limpar_campos, anchor=CENTER, text="Limpar".upper(), width=20, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co11, fg=co1)
	botao_limpar.place(x=1150, y=150)


		# Tabela Alunos
	def mostrar_planejamento():
		app_nome = Label(frame_tabela, text="Apresentação de Planejamento", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
		app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

		# creating a treeview with dual scrollbars
		list_header = ['id','Tema', 'Ojetivos','Área de Conhecimento','Disciplina','Competências','Habilidades','Objetos', 'Descrição', 'Recursos', 'Avaliação']

		df_list = ver_planejamento()

		global tree_personais

		tree_personais = ttk.Treeview(frame_tabela, selectmode="extended",columns=list_header, show="headings")

		# vertical scrollbar
		vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_personais.yview)
		# horizontal scrollbar
		hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_personais.xview)

		tree_personais.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
		tree_personais.grid(column=0, row=1, sticky='nsew')
		vsb.grid(column=1, row=1, sticky='ns')
		hsb.grid(column=0, row=2, sticky='ew')
		frame_tabela.grid_rowconfigure(0, weight=12)
		
		hd=["nw","nw","nw","nw","nw","nw","nw","nw","nw","nw","nw"]
		h=[30,130,130,130,130,130,130,130,130,130,130]
		n=0
		
		for col in list_header:
   			tree_personais.heading(col, text=col.title(), anchor=NW)
   			tree_personais.column(col, width=h[n],anchor=hd[n])
   			n+=1

		for item in df_list:
			tree_personais.insert('', 'end', values=item)
	
	mostrar_planejamento()

def salvar():
	print('Hello World')

	# Botões de Salvar, Editar e Deletar
	botao_salvar = Button(frame_detalhes, anchor=CENTER, text="Salvar".upper(), width=20, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
	botao_salvar.place(x=630, y=60)


	botao_atualizar = Button(frame_detalhes, anchor=CENTER, text="Editar".upper(), width=20, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co9, fg=co1)
	botao_atualizar.place(x=630, y=90)


	botao_deletar = Button(frame_detalhes, anchor=CENTER, text="Deletar".upper(), width=20, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
	botao_deletar.place(x=630, y=120)


def control(i):
	#CADASTRO DE CLIENTE
	if i == 'cadastro':

		for widget in frame_detalhes.winfo_children():
			widget.destroy()

		for widget in frame_tabela.winfo_children():
			widget.destroy()

		#Chamando Função Clientes
		cadastrar()

	if i == 'salvar':

		for widget in frame_detalhes.winfo_children():
			widget.destroy()

		for widget in frame_tabela.winfo_children():
			widget.destroy()

		#Chamando Função Clientes
		salvar()


#Criando Botoes ------------------------------------------------------------------------
#Cadastro
app_img_cadastro = Image.open('add.png')
app_img_cadastro = app_img_cadastro.resize((18,18))
app_img_cadastro = ImageTk.PhotoImage(app_img_cadastro)
app_cadastro = Button(frame_dados, command=lambda:control('cadastro'), image=app_img_cadastro, text=" Cadastro", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_cadastro.place(x=10, y=15)

#Salvar
app_img_salvar = Image.open('save.png')
app_img_salvar = app_img_salvar.resize((18,18))
app_img_salvar = ImageTk.PhotoImage(app_img_salvar)
app_salvar = Button(frame_dados, command=lambda:control('salvar'), image=app_img_salvar, text=" Salvar", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_salvar.place(x=150, y=15)


cadastrar()
#Executando Janela
janela.mainloop()
