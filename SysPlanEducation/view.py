import sqlite3 as lite

""" Criando Conexão """
try:
    conn = lite.connect('cadastro_planejamento.db') #nome do banco de dados
    print("Conexão realizada com sucesso! ")
except lite.Error as e:
    print("Erro ao conectar com banco de dados: ", e)

"""Tabela de Personais--------------------------------------------"""
#Inserir Personais

def inserir_planejamento(i):
    with conn:
        cur = conn.cursor()
        query = "INSERT INTO planejamento (nome_professor, disciplina, turmas, meta, descricao_aula, material) VALUES (?,?,?,?,?,?)"

        cur.execute(query, i)

#inserir_planejamento(['Zilmar', 'filosofia', '1° Ano', 'teste', 'teste 2', 'Projetor'])

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
        query = "UPDATE planejamento SET nome_professor=?, disciplina=?, turmas=?, meta=?, descricao_aula=?, material=? WHERE id=?"

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
