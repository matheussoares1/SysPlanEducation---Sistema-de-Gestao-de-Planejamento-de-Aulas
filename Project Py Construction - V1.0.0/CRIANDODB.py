""" Crindo Banco de Dados """
import sqlite3

""" Criando Conexão """
try:
    conn = sqlite3.connect('cadastro_planejamento.db') #nome do banco de dados
    print("Conexão realizada com sucesso! ")
except sqlite3.Error as e:
    print("Erro ao conectar com banco de dados: ", e)


try:
    with conn:
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS competencias_gerais(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    comp_gerais TEXT
            )""")
        print("TABELA COMPETENCIAS GERAIS CRIADA COM SUCESSO")
except sqlite3.Error as e:
    print("Erro ao criar a tabela competencias_gerais ", e)


#TABELA COMPETENCIAS ESPECIFICAS
try:
    with conn:
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS competencias_especificas(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    comp_especificas_texto TEXT
            )""")
        
        print("TABELA COMPETENCIAS ESPECIFICAS CRIADA COM SUCESSO")
except sqlite3.Error as e:
    print("Erro ao criar a tabela competencias_gerais ", e)

#TABELA HABILIDADES
try:
    with conn:
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS habilidades(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    comp_especificas TEXT,
                    codigo TEXT,
                    habilidade TEXT,
                    FOREIGN KEY (comp_especificas) REFERENCES competencias_especificas (comp_especificas_texto) ON UPDATE CASCADE ON DELETE CASCADE
            )""")
        print("TABELA HABILIDADES CRIADA COM SUCESSO")
except sqlite3.Error as e:
    print("Erro ao criar a tabela competencias_gerais ", e)


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
                    competencias_ger TEXT,
                    competencias_esp TEXT,
                    habilidades TEXT,
                    objetos TEXT,
                    descricao TEXT,
                    recursos TEXT,
                    avaliacao TEXT,
                    FOREIGN KEY (habilidades) REFERENCES habilidades (habilidade) ON UPDATE CASCADE ON DELETE CASCADE,
                    FOREIGN KEY (competencias_ger) REFERENCES competencias_gerais (comp_gerais) ON UPDATE CASCADE ON DELETE CASCADE,
                    FOREIGN KEY (competencias_esp) REFERENCES competencias_especificas (comp_especificas_texto) ON UPDATE CASCADE ON DELETE CASCADE
                    
        ) """)

        print("TABELA PLANEJAMENTO CRIADA COM SUCESSO")

except sqlite3.Error as e:
    print("Erro ao criar a tabela PLANEJAMENTO ", e)


