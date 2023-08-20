""" Crindo Banco de Dados """
import sqlite3

""" Criando Conexão """
try:
    conn = sqlite3.connect('cadastro_planejamento.db') #nome do banco de dados
    print("Conexão realizada com sucesso! ")
except sqlite3.Error as e:
    print("Erro ao conectar com banco de dados: ", e)


#Criando tabela de planejamento

try:
    with conn:
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS planejamento(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tema TEXT,
                    objetivos TEXT,
                    area_conhecimento TEXT,
                    disciplina TEXT,
                    competencias TEXT,
                    habilidades TEXT,
                    objetos TEXT,
                    descricao TEXT,
                    recursos TEXT,
                    avaliacao TEXT
                    
        ) """)

        print("TABELA PLANEJAMENTO CRIADA COM SUCESSO")

except sqlite3.Error as e:
    print("Erro ao criar a tabela PLANEJAMENTO ", e)
