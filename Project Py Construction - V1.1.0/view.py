import sqlite3 as lite

""" Criando Conexão """
try:
    conn = lite.connect('cadastro_planejamento.db') #nome do banco de dados
    print("Conexão realizada com sucesso! ")
except lite.Error as e:
    print("Erro ao conectar com banco de dados: ", e)

def criar_comp_gerais(i):
    with conn:
        cur = conn.cursor()
        query = "INSERT INTO competencias_gerais (comp_gerais) VALUES (?)"

        cur.execute(query, i)

def ver_comp_gerais():
    listacg = []
    with conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM competencias_gerais')
        linhacg= cur.fetchall()

        for i in linhacg:
            listacg.append(i)
    return listacg


def atualizar_comp_gerais(i):
    with conn:
        cur = conn.cursor()
        query = "UPDATE competencias_gerais SET comp_gerais=? WHERE id=?"

        cur.execute(query, i)


def deletar_comp_gerais(i):
    with conn:
        cur = conn.cursor()
        query = "DELETE FROM competencias_gerais WHERE id=?"

        cur.execute(query, i)

#////////////////////////////////////////////



def criar_comp_especificas(i):
    with conn:
        cur = conn.cursor()
        query = "INSERT INTO competencias_especificas (comp_especificas_texto) VALUES (?)"
        cur.execute(query, i)
    return cur.lastrowid  # Retorna o ID da última linha inserida

#teste = ["maravilha"]
#criar_comp_especificas(teste)


def ver_comp_especificas():
    listace = []
    with conn:
        cur = conn.cursor()
        cur.execute('SELECT id, comp_especificas_texto FROM competencias_especificas')
        linhace = cur.fetchall()

        for i in linhace:
            listace.append(i)

    return listace


def atualizar_comp_especificas(i):
    with conn:
        cur = conn.cursor()
        query = "UPDATE competencias_especificas SET comp_especificas_texto=? WHERE id=?"

        cur.execute(query, i)

def deletar_comp_especificas(i):
    with conn:
        cur = conn.cursor()
        query = "DELETE FROM competencias_especificas WHERE ID=?"

        cur.execute(query, i)

#/////////////////////////////////////////////////////////


def inserir_habilidades(i):
    with conn:
        cur = conn.cursor()
        query = "INSERT INTO habilidades (comp_especificas, codigo, habilidade) VALUES (?,?,?)"

        cur.execute(query, i)

def ver_habilidades():
    listahb = []
    with conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM habilidades')

        linhahb = cur.fetchall()

        for i in linhahb:
            listahb.append(i)

    return listahb


def atualizar_habilidades(i):
    with conn:
        cur = conn.cursor()
        query = "UPDATE habilidades SET comp_especificas=?, codigo=?, habilidade=? WHERE id=?"

        cur.execute(query, i)


def deletar_habilidades(i):
    with conn:
        cur = conn.cursor()
        query = "DELETE FROM habilidades WHERE id=?"

        cur.execute(query, i)


"""Tabela de PLANEJAMENTO--------------------------------------------"""
#Inserir PeLANEJAMENTO

def inserir_planejamento(i):
    with conn:
        cur = conn.cursor()
        query = "INSERT INTO planejamento (tema, objetivos, area_conhecimento, disciplina, competencias_ger, competencias_esp, habilidades, objetos, descricao, recursos, avaliacao) VALUES (?,?,?,?,?,?,?,?,?,?,?)" 

        cur.execute(query, i)

#inserir_planejamento(['Zilmar', '', '', '', '', '', '', '', '', ''])

#VER todos os ppersonais (SELECIONAR) R
def ver_planejamento():
    lista = []
    with conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM planejamento')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

#print(ver_planejamento())


def atualizar_planejamento(i):
    with conn:
        cur = conn.cursor()
        query = "UPDATE planejamento SET tema=?, objetivos=?, area_conhecimento=?, disciplina=?, competencias_ger=?,competencias_esp=?, habilidades=?, objetos=?, descricao=?, recursos=?, avaliacao=?  WHERE id=?"

        cur.execute(query, i)

#l = ['Zilmar', 'filosofia', '2° Ano', 'teste', 'teste 2', 'Projetor', 1]
#atualizar_planejamento(l)

#print(ver_planejamento())


def deletar_planejamento(i):
    with conn:
        cur = conn.cursor()
        query = "DELETE FROM planejamento WHERE id=?"

        cur.execute(query, i)


#deletar_planejamento([1])
#print(ver_planejamento())


#print(ver_planejamento())
#print(ver_comp_especificas())
#print(ver_habilidades())
#print(ver_comp_gerais())