from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd


# importando pillow
from PIL import Image, ImageTk



# Importando VIew

from view import *
from conversor import *


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

	#/////////////////////////////////////////////////////////////////////////////

	l_competencias = Label(frame_detalhes, text="Competências Gerais: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_competencias.place(x=5, y=85)

	compgs = ver_comp_gerais()
	compgl = []

	for i in compgs:
		compgl.append(i[1])

	ecompgs_nome = ttk.Combobox(frame_detalhes, width=30, font=('Ivy 8 bold'))
	ecompgs_nome['values'] = (compgl)
	ecompgs_nome.place(x=5,y=105)




	l_competencias = Label(frame_detalhes, text="Competências Específicas: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_competencias.place(x=250, y=85)

	compes = ver_comp_especificas()
	compesl = []

	for i in compes:
		compesl.append(i[1])

	ecompes_nome = ttk.Combobox(frame_detalhes, width=35, font=('Ivy 8 bold'))
	ecompes_nome['values'] = (compesl)
	ecompes_nome.place(x=250,y=105)






	l_competencias = Label(frame_detalhes, text="Habilidades: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_competencias.place(x=550, y=85)

	hab = ver_habilidades()
	habl = []

	for i in hab:
		habl.append(i[1])

	ehab_nome = ttk.Combobox(frame_detalhes, width=35, font=('Ivy 8 bold'))
	ehab_nome['values'] = (habl)
	ehab_nome.place(x=530,y=105)



	l_objetos = Label(frame_detalhes, text="Objetos de conhecimento: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_objetos.place(x=800, y=85)
	enome_objetos = Entry(frame_detalhes, width=35, justify='left', relief='solid')
	enome_objetos.place(x=800, y=103)


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

def inserir():
	frame_tabela_personais = Frame(frame_tabela, width=500, height=300, bg=co1)
	frame_tabela_personais.grid(row=0, column=0, pady=0, padx=20, sticky=NSEW)

	frame_tabela_turmas = Frame(frame_tabela, width=320, height=200, bg=co1)
	frame_tabela_turmas.grid(row=0, column=2, pady=0, padx=10, sticky=NSEW)

	frame_tabela_divisao = Frame(frame_tabela, width=5, height=200, bg=co1)
	frame_tabela_divisao.grid(row=0, column=1, pady=0, padx=10, sticky=NSEW)




	#Linha Divisória
	label_cg = Label(frame_detalhes, relief=GROOVE, text='Competências Gerais', anchor=NW, font=('Ivy 12 bold'))
	label_cg.place(x=0, y=10)

	label_cg = Label(frame_detalhes, relief=GROOVE, text='Competências Específicas', anchor=NW, font=('Ivy 12 bold'))
	label_cg.place(x=660, y=10)


	#//////////////COMPETENCIAS GERAIS//////////////
	l_compg = Label(frame_detalhes, text=' Inserir Competências Específicas', height=1, anchor=NW, font=('Ivy 12'), bg=co1)
	l_compg.place(x=660, y=45)
	enome_compg = Entry(frame_detalhes, width=74, justify='left', relief='solid')
	enome_compg.place(x=20, y=70)

	#//////////////COMPETENCIAS GERAIS//////////////
	l_compe = Label(frame_detalhes, text=' Inserir Competências Gerais', height=1, anchor=NW, font=('Ivy 12'), bg=co1)
	l_compe.place(x=10, y=45)
	enome_compe = Entry(frame_detalhes, width=74, justify='left', relief='solid')
	enome_compe.place(x=670, y=70)

	def inserindo_compe_especifica():

		texto_comp = enome_compe.get()

		lista_comes = [texto_comp]

		for i in lista_comes:

			if i=="":
				messagebox.showerror('Erro', "Preencha o Campo de Texto.")
				return

		criar_comp_especificas(lista_comes)

		messagebox.showinfo('Sucesso', 'Dados inseridos com sucesso!')

		enome_compe.delete(0, END)

		mostrar_turmass()

	def update_comp_especificas():
		try:
			tree_itens = tree_turmas.focus()
			tree_dicionario = tree_turmas.item(tree_itens)
			tree_lista = tree_dicionario['values']

			valor_id = tree_lista[0]

			enome_compe.insert(0, tree_lista[1])

			def update_comes():

				texto_comp = enome_compe.get()

				lista_comes = [texto_comp, valor_id]

				for i in lista_comes:
					if i=="":
						messagebox.showerror('Erro', "Preencha o Campo de Texto.")
						return

				atualizar_comp_especificas(lista_comes)
	
				messagebox.showinfo('Sucesso', 'Dados inseridos com sucesso!')
	
				enome_compe.delete(0, END)

				mostrar_turmass()

				botao_salvar_comp_especificas.destroy()

			botao_salvar_comp_especificas = Button(frame_detalhes, command=update_comes, width=20, text="Salvar Alterações".upper(), overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
			botao_salvar_comp_especificas.place(x=660, y=195)

		except IndexError:
			messagebox.showerror('Erro', 'Selecione um dos campos na tabela')

	def deletar_comp_es():
		try:
			tree_itens = tree_turmas.focus()
			tree_dicionario = tree_turmas.item(tree_itens)
			tree_lista = tree_dicionario['values']

			valor_id = tree_lista[0]

			deletar_comp_especificas([valor_id])

			messagebox.showerror('Sucesso', 'Dados deletados com sucesso!')

			mostrar_turmass()

		except IndexError:
			messagebox.showerror('Erro', 'Selecione um campo na tabela para ser deletado.')



	def inserindo_compe_geral():
		texto = enome_compg.get()

		lista_comger = [texto]

		for i in lista_comger:
			if i=="":
				messagebox.showerror('Erro', "Preencha o Campo de Texto.")
				return
		criar_comp_gerais(lista_comger)

		messagebox.showinfo('Sucesso', 'Dados inseridos com sucesso!')

		enome_compg.delete(0, END)

		mostrar_personais()

	def update_comp_geral():
		try:
			tree_itens = tree_personais.focus()
			tree_dicionario = tree_personais.item(tree_itens)
			tree_lista = tree_dicionario['values']

			valor_id = tree_lista[0]

			enome_compg.insert(0, tree_lista[1])

			def update_comg():

				texto = enome_compg.get()

				lista_comger = [texto, valor_id]

				for i in lista_comger:
					if i=="":
						messagebox.showerror('Erro', "Preencha o Campo de Texto.")
						return

				atualizar_comp_gerais(lista_comger)
	
				messagebox.showinfo('Sucesso', 'Dados inseridos com sucesso!')
	
				enome_compg.delete(0, END)

				mostrar_personais()

				botao_salvar_comp_gerais.destroy()

			botao_salvar_comp_gerais = Button(frame_detalhes, command=update_comg, width=20, text="Salvar Alterações".upper(), overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
			botao_salvar_comp_gerais.place(x=20, y=195)

		except IndexError:
			messagebox.showerror('Erro', 'Selecione um dos campos na tabela')

	def deletar_comp_ge():
		try:
			tree_itens = tree_personais.focus()
			tree_dicionario = tree_personais.item(tree_itens)
			tree_lista = tree_dicionario['values']

			valor_id = tree_lista[0]

			deletar_comp_gerais([valor_id])

			messagebox.showinfo('Sucesso', 'Dados Deletados com Sucesso!')

			mostrar_personais()
		except IndexError:
			messagebox.showerror('Erro', 'Selecione um campo na tabela para ser deletado!')

	botao_salvar_cg = Button(frame_detalhes,command=inserindo_compe_geral, anchor=CENTER, text="Salvar".upper(), width=20, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
	botao_salvar_cg.place(x=20, y=100)

	botao_atualizar_cg = Button(frame_detalhes,command=update_comp_geral, anchor=CENTER, text="Editar".upper(), width=20, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co9, fg=co1)
	botao_atualizar_cg.place(x=20, y=133)

	botao_deletar_cg = Button(frame_detalhes,command=deletar_comp_ge, anchor=CENTER, text="Deletar".upper(), width=20, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
	botao_deletar_cg.place(x=20, y=165)






		#Linha Divisória
	l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
	l_linha.place(x=650, y=10)

	l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
	l_linha.place(x=651, y=10)

	l_linha = Label(frame_tabela, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
	l_linha.place(x=649, y=10)

	#Competencias Especificas

	botao_salvar_ce = Button(frame_detalhes,command=inserindo_compe_especifica, anchor=CENTER, text="Salvar".upper(), width=20, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
	botao_salvar_ce.place(x=670, y=100)

	botao_atualizar_ce = Button(frame_detalhes,command=update_comp_especificas, anchor=CENTER, text="Editar".upper(), width=20, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co9, fg=co1)
	botao_atualizar_ce.place(x=670, y=135)

	botao_deletar_ce = Button(frame_detalhes,command=deletar_comp_es, anchor=CENTER, text="Deletar".upper(), width=20, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
	botao_deletar_ce.place(x=670, y=165)



	
	def mostrar_personais():


		app_nome = Label(frame_tabela_personais, text="Tabela de Personais", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
		app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)
		
		# creating a treeview with dual scrollbars
		list_header = ['ID','Nome']

		df_list = ver_comp_gerais()

		global tree_personais

		tree_personais = ttk.Treeview(frame_tabela_personais, selectmode="extended", columns=list_header, show="headings")

 		# vertical scrollbar
		vsb = ttk.Scrollbar(frame_tabela_personais, orient="vertical", command=tree_personais.yview)
		# horizontal scrollbar
		hsb = ttk.Scrollbar(frame_tabela_personais, orient="horizontal", command=tree_personais.xview)

		tree_personais.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
		tree_personais.grid(column=0, row=1, sticky='nsew')
		vsb.grid(column=1, row=1, sticky='ns')
		hsb.grid(column=0, row=2, sticky='ew')
		frame_tabela_personais.grid_rowconfigure(0, weight=12)

		hd = ["nw","nw","e","e"]
		h = [30,550]
		n = 0
 
		for col in list_header:
			tree_personais.heading(col, text=col.title(), anchor=NW)
			# adjust the column's width to the header string
			tree_personais.column(col, width=h[n], anchor=hd[n])
			n+=1

		for item in df_list:
			tree_personais.insert('', 'end', values=item)
			
	mostrar_personais()

	l_linha = Label(frame_tabela_divisao, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
	l_linha.place(x=0, y=10)
	


	#l_linha = Label(frame_tabela_divisaoo, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
	#l_linha.place(x=0, y=10)
	


	def mostrar_turmass():
		app_nome = Label(frame_tabela_turmas, text="Tabela de Turmas", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
		app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)
		
		# creating a treeview with dual scrollbars
		list_header = ['ID','Nome']

		df_list = ver_comp_especificas()

		global tree_turmas

		tree_turmas = ttk.Treeview(frame_tabela_turmas, selectmode="extended", columns=list_header, show="headings")

 		# vertical scrollbar
		vsb = ttk.Scrollbar(frame_tabela_turmas, orient="vertical", command=tree_turmas.yview)
		# horizontal scrollbar
		hsb = ttk.Scrollbar(frame_tabela_turmas, orient="horizontal", command=tree_turmas.xview)

		tree_turmas.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
		tree_turmas.grid(column=0, row=1, sticky='nsew')
		vsb.grid(column=1, row=1, sticky='ns')
		hsb.grid(column=0, row=2, sticky='ew')
		frame_tabela_turmas.grid_rowconfigure(0, weight=12)

		hd = ["nw","nw","e","e"]
		h = [30,550]
		n = 0
 
		for col in list_header:
			tree_turmas.heading(col, text=col.title(), anchor=NW)
			# adjust the column's width to the header string
			tree_turmas.column(col, width=h[n], anchor=hd[n])
			n+=1

		for item in df_list:
			tree_turmas.insert('', 'end', values=item)
			
	mostrar_turmass()


def cadas_hab():

	#COMBOBOX

	l_competencias = Label(frame_detalhes, text="Competência Específica da Habilidade: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_competencias.place(x=20, y=85)

	comphabi = ver_comp_especificas()
	comphabil = []

	for i in comphabi:
		comphabil.append(i[1])

	ecomphab_nome = ttk.Combobox(frame_detalhes, width=50, font=('Ivy 8 bold'))
	ecomphab_nome['values'] = (comphabil)
	ecomphab_nome.place(x=20,y=105)

	#CODIGO HABILIDADES

	l_tema = Label(frame_detalhes, text="Código de Habilidade: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_tema.place(x=400, y=85)
	enome_chabi = Entry(frame_detalhes, width=50, justify='left', relief='solid')
	enome_chabi.place(x=400, y=103 )

	#HABILIDADE TEXTO

	l_objetivos = Label(frame_detalhes, text="Habilidade: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_objetivos.place(x=20, y=140)
	enome_habi = Entry(frame_detalhes, width=97, justify='left', relief='solid')
	enome_habi.place(x=20, y=163)

	def nova_habilidade():

		competenciaespecifica = ecomphab_nome.get()
		codigoh = enome_chabi.get()
		htexto = enome_habi.get()

		lista_habilidade = [competenciaespecifica, codigoh, htexto]

		for i in lista_habilidade:
			if i=="":
				messagebox.showerror('Erro', 'Preencha todos os Campos.')
				return

		inserir_habilidades(lista_habilidade)

		messagebox.showinfo('Sucesso', 'Dados Inseridos com Sucesso!')

		ecomphab_nome.delete(0,END)
		enome_chabi.delete(0,END)
		enome_habi.delete(0,END)

		mostrar_hab()

	def update_habilidade():
		try:
			tree_itens = tree_turmas.focus()
			tree_dicionario = tree_turmas.item(tree_itens)
			tree_lista = tree_dicionario['values']

			valor_idh = tree_lista[0]

			ecomphab_nome.insert(0,tree_lista[1])
			enome_chabi.insert(0,tree_lista[2])
			enome_habi.insert(0,tree_lista[3])

			def updateh():

				competenciaespecifica = ecomphab_nome.get()
				codigoh = enome_chabi.get()
				htexto = enome_habi.get()

				lista_habilidade = [competenciaespecifica, codigoh, htexto, valor_idh]

				for i in lista_habilidade:
					if i=="":
						messagebox.showerror('Erro', 'Preencha todos os Campos.')
						return

				atualizar_habilidades(lista_habilidade)

				messagebox.showinfo('Sucesso', 'Dados Inseridos com Sucesso!')

				ecomphab_nome.delete(0,END)
				enome_chabi.delete(0,END)
				enome_habi.delete(0,END)

				mostrar_hab()

				botao_salvarh.destroy()

			botao_salvarh = Button(frame_detalhes, command=updateh, anchor=CENTER, text="Salvar Atualização".upper(), overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
			botao_salvarh.place(x=1032, y=195)

		except IndexError:
			messagebox.showerror('Erro', 'Selecione um dos campos da tabela.')


	def delete_habilidades():
		try:
			tree_itens = tree_turmas.focus()
			tree_dicionario = tree_turmas.item(tree_itens)
			tree_lista = tree_dicionario['values']

			valor_idh = tree_lista[0]

			deletar_habilidades([valor_idh])

			messagebox.showerror('Sucesso', 'Dados deletados com sucesso!')

			mostrar_hab()

		except IndexError:
			messagebox.showerror('Erro', 'Selecione um dos campos da tabela para ser deletados')


			#Linha Divisória
	l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
	l_linha.place(x=850, y=10)

	l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
	l_linha.place(x=850, y=10)

	l_linha = Label(frame_tabela, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
	l_linha.place(x=850, y=10)

	#Competencias Especificas

	botao_salvar_hb = Button(frame_detalhes,command=nova_habilidade, anchor=CENTER, text="Salvar".upper(), width=20, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
	botao_salvar_hb.place(x=1030, y=100)

	botao_atualizar_hb = Button(frame_detalhes,command=update_habilidade, anchor=CENTER, text="Editar".upper(), width=20, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co9, fg=co1)
	botao_atualizar_hb.place(x=1030, y=135)

	botao_deletar_hb = Button(frame_detalhes,command=delete_habilidades, anchor=CENTER, text="Deletar".upper(), width=20, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
	botao_deletar_hb.place(x=1030, y=165)




	def mostrar_hab():
		app_nome = Label(frame_tabela, text="Tabela de Habilidades", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
		app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)
		
		# creating a treeview with dual scrollbars
		list_header = ['ID','Competência Específica', 'Código', 'Habilidade']

		df_list = ver_habilidades()

		global tree_turmas

		tree_turmas = ttk.Treeview(frame_tabela, selectmode="extended", columns=list_header, show="headings")

 		# vertical scrollbar
		vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_turmas.yview)
		# horizontal scrollbar
		hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_turmas.xview)

		tree_turmas.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
		tree_turmas.grid(column=0, row=1, sticky='nsew')
		vsb.grid(column=1, row=1, sticky='ns')
		hsb.grid(column=0, row=2, sticky='ew')
		frame_tabela.grid_rowconfigure(0, weight=12)

		hd = ["nw","nw","e","e"]
		h = [30,500,80,720]
		n = 0
 
		for col in list_header:
			tree_turmas.heading(col, text=col.title(), anchor=NW)
			# adjust the column's width to the header string
			tree_turmas.column(col, width=h[n], anchor=hd[n])
			n+=1

		for item in df_list:
			tree_turmas.insert('', 'end', values=item)
			
	mostrar_hab()


def salvar():


	# Botões de Salvar, Editar e Deletar
	botao_exportarp = Button(frame_detalhes,command=exportar_planejamento, anchor=CENTER, text="Exportar Planejamento".upper(), width=20, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
	botao_exportarp.place(x=630, y=60)
	
	# Botões de Salvar, Editar e Deletar
	botao_exportarcg = Button(frame_detalhes,command=exportar_competencias_gerais, anchor=CENTER, text="Exportar Competências".upper(), width=20, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
	botao_exportarcg.place(x=630, y=100)

	# Botões de Salvar, Editar e Deletar
	botao_exportarce = Button(frame_detalhes,command=exportar_competencias_especificas, anchor=CENTER, text="Exportar Habilidades".upper(), width=20, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
	botao_exportarce.place(x=630, y=140)

	botao_exportarh = Button(frame_detalhes,command=exportar_competencias_especificas, anchor=CENTER, text="Exportar Habilidades".upper(), width=20, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
	botao_exportarh.place(x=630, y=180)

	l_texto = Label(frame_tabela, text='Desenvolvido por Matheus Soares - 2023', font=('Ivy 7 bold'), bg=co1, fg=co0)
	l_texto.place(x=1100, y=260)




def control(i):
	#CADASTRO DE CLIENTE
	if i == 'planejamento':

		for widget in frame_detalhes.winfo_children():
			widget.destroy()

		for widget in frame_tabela.winfo_children():
			widget.destroy()

		#Chamando Função Clientes
		cadastrar()

	if i == 'exportar':

		for widget in frame_detalhes.winfo_children():
			widget.destroy()

		for widget in frame_tabela.winfo_children():
			widget.destroy()

		#Chamando Função Clientes
		salvar()

	if i == 'competencias':

		for widget in frame_detalhes.winfo_children():
			widget.destroy()

		for widget in frame_tabela.winfo_children():
			widget.destroy()

		#Chamando Função Clientes
		inserir()

	if i == 'habilidadees':
		for widget in frame_detalhes.winfo_children():
			widget.destroy()

		for widget in frame_tabela.winfo_children():
			widget.destroy()

		cadas_hab()



#Criando Botoes ------------------------------------------------------------------------
#Cadastro
app_img_cadastro = Image.open('add.png')
app_img_cadastro = app_img_cadastro.resize((18,18))
app_img_cadastro = ImageTk.PhotoImage(app_img_cadastro)
app_cadastro = Button(frame_dados, command=lambda:control('planejamento'), image=app_img_cadastro, text=" Planejamento", width=130, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_cadastro.place(x=10, y=15)

#inserir
app_img_inserir = Image.open('add.png')
app_img_inserir = app_img_inserir.resize((18,18))
app_img_inserir = ImageTk.PhotoImage(app_img_inserir)
app_inserir = Button(frame_dados, command=lambda:control('competencias'), image=app_img_inserir, text=" Competências", width=130, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_inserir.place(x=180, y=15)

app_img_hab = Image.open('add.png')
app_img_hab = app_img_hab.resize((18,18))
app_img_inserir_hab = ImageTk.PhotoImage(app_img_hab)
app_inserir_hab = Button(frame_dados, command=lambda:control('habilidadees'), image=app_img_inserir, text=" Habilidades", width=130, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_inserir_hab.place(x=350, y=15)

#Salvar
app_img_salvar = Image.open('save.png')
app_img_salvar = app_img_salvar.resize((18,18))
app_img_salvar = ImageTk.PhotoImage(app_img_salvar)
app_salvar = Button(frame_dados, command=lambda:control('exportar'), image=app_img_salvar, text=" Exportar", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_salvar.place(x=590, y=15)


cadastrar()
#Executando Janela
janela.mainloop()
