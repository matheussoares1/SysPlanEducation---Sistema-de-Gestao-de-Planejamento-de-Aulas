from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date


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


# Criando janela
janela = Tk()
janela.title("")
janela.geometry('850x620')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# Criando Frames
frame_logo = Frame(janela, width=850, height=52, bg=co2)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_dados = Frame(janela, width=850, height=65, bg=co2)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_detalhes = Frame(janela, width=850, height=200, bg=co1)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=850, height=200, bg=co1)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)

#FRAME LOGO
app_lg = Image.open('logosemmarca.png')
app_lg = app_lg.resize((70,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="  SysPlanEducation", width=850, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=co10, fg=co1)
app_logo.place(x=0, y=0)


def cadastrar():

	l_professor = Label(frame_detalhes, text="Nome do Professor: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_professor.place(x=7, y=10)
	enome_professor = Entry(frame_detalhes, width=35, justify='left', relief='solid')
	enome_professor.place(x=7, y=30)

	l_disciplina = Label(frame_detalhes, text="Disciplina: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_disciplina.place(x=300, y=10)
	enome_disciplina = Entry(frame_detalhes, width=20, justify='left', relief='solid')
	enome_disciplina.place(x=300, y=30)

	l_turmas = Label(frame_detalhes, text="Turma: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_turmas.place(x=475, y=10)
	enome_turmas = Entry(frame_detalhes, width=10, justify='left', relief='solid')
	enome_turmas.place(x=475, y=30)

	l_meta = Label(frame_detalhes, text="Meta: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_meta.place(x=7, y=55)
	enome_meta = Entry(frame_detalhes, width=35, justify='left', relief='solid')
	enome_meta.place(x=7, y=75)

	l_descricao = Label(frame_detalhes, text="Descrição da Aula: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_descricao.place(x=300, y=55)
	enome_descricao = Entry(frame_detalhes, width=32, justify='left', relief='solid')
	enome_descricao.place(x=300, y=75)

	l_material = Label(frame_detalhes, text="Material: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_material.place(x=7, y=100)
	enome_material = Entry(frame_detalhes, width=35, justify='left', relief='solid')
	enome_material.place(x=7, y=120)

	# Linha Divisória
	l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=57, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
	l_linha.place(x=570, y=10)

	l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=57, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
	l_linha.place(x=569, y=10)

		# Linha Divisória
	l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=550, height=1, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
	l_linha.place(x=7, y=190)

	l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=550, height=1, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
	l_linha.place(x=7, y=189)

	def novo_planejamento():
		professor = enome_professor.get()
		disciplina = enome_disciplina.get()
		turma = enome_turmas.get()
		meta = enome_meta.get()
		descricao = enome_descricao.get()
		material = enome_material.get()

		lista_planejamento = [professor, disciplina, turma, meta, descricao, material]

		# Caso esteja vazio haverá uma tela de insereçao de ddos obrigatórios
		for i in lista_planejamento:
			if i=="":
				messagebox.showerror('Erro', 'Preencha todos os campos.')
				return

		#Inserindo dados no banco de dados 
		inserir_planejamento(lista_planejamento)

		# Mostrando mensagem de sucesso
		messagebox.showinfo('Sucesso', 'Dados inseridos com sucesso!')

		enome_professor.delete(0,END)
		enome_disciplina.delete(0,END)
		enome_turmas.delete(0,END)
		enome_meta.delete(0,END)
		enome_descricao.delete(0,END)
		enome_material.delete(0,END)

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
			enome_professor.insert(0, tree_lista[1])
			enome_disciplina.insert(0, tree_lista[2])
			enome_turmas.insert(0, tree_lista[3])
			enome_meta.insert(0, tree_lista[4])
			enome_descricao.insert(0, tree_lista[5])
			enome_material.insert(0, tree_lista[6])


			#função atualizar
			def update():
				professor = enome_professor.get()
				disciplina = enome_disciplina.get()
				turma = enome_turmas.get()
				meta = enome_meta.get()
				descricao = enome_descricao.get()
				material = enome_material.get()

				lista_planejamento = [professor, disciplina, turma, meta, descricao, material, valor_id]

				# Caso esteja vazio haverá uma tela de insereçao de ddos obrigatórios
				for i in lista_planejamento:
					if i=="":
						messagebox.showerror('Erro', 'Preencha todos os campos.')
						return

				#Inserindo dados no banco de dados 
				atualizar_planejamento(lista_planejamento)

				# Mostrando mensagem de sucesso
				messagebox.showinfo('Sucesso', 'Dados inseridos com sucesso!')

				enome_professor.delete(0,END)
				enome_disciplina.delete(0,END)
				enome_turmas.delete(0,END)
				enome_meta.delete(0,END)
				enome_descricao.delete(0,END)
				enome_material.delete(0,END)


				# Mostrando os valores na tabela
				mostrar_planejamento()

				#Destruindo o Botão Salvar após Salvar os dados
				botao_salvar.destroy()


			botao_salvar = Button(frame_detalhes,command=update, anchor=CENTER, text="Salvar Atualização".upper(), overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
			botao_salvar.place(x=190, y=170)		

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




	# Botões de Salvar, Editar e Deletar
	botao_salvar = Button(frame_detalhes, command=novo_planejamento, anchor=CENTER, text="Salvar".upper(), width=20, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
	botao_salvar.place(x=630, y=60)


	botao_atualizar = Button(frame_detalhes,command=update_planejamenento, anchor=CENTER, text="Editar".upper(), width=20, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co9, fg=co1)
	botao_atualizar.place(x=630, y=90)


	botao_deletar = Button(frame_detalhes,command=delete_planejamento, anchor=CENTER, text="Deletar".upper(), width=20, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
	botao_deletar.place(x=630, y=120)

		# Tabela Alunos
	def mostrar_planejamento():
		app_nome = Label(frame_tabela, text="Apresentação de Planejamento", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
		app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

		# creating a treeview with dual scrollbars
		list_header = ['id','Professor','Disciplina','Turmas','Meta','Descrição','Material']

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
		
		hd=["nw","nw","nw","center","center","center","center"]
		h=[40,100,100,100,180,180,110]
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
