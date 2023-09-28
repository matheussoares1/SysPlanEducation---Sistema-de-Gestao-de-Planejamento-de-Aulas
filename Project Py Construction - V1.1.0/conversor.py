import sqlite3
import csv

# Conectar ao banco de dados
def exportar_planejamento():

    conn = sqlite3.connect('cadastro_planejamento.db')

    # Criar um cursor
    cursor = conn.cursor()

    # Executar uma consulta SQL para selecionar os dados da tabela que deseja exportar
    cursor.execute("SELECT * FROM planejamento")

    # Recuperar todos os registros da consulta
    dados = cursor.fetchall()

    # Definir o nome do arquivo CSV de saída
    nome_arquivo_csv = 'planejamento.csv'

    # Escrever os dados no arquivo CSV
    with open(nome_arquivo_csv, 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
    
        # Escrever o cabeçalho (nomes das colunas)
        escritor_csv.writerow([i[0] for i in cursor.description])
    
        # Escrever os dados
        escritor_csv.writerows(dados)

    # Fechar a conexão com o banco de dados
    conn.close()

    print(f'Dados exportados para {nome_arquivo_csv}')




def exportar_competencias_gerais():
    conn = sqlite3.connect('cadastro_planejamento.db')

    # Criar um cursor
    cursor = conn.cursor()

    # Executar uma consulta SQL para selecionar os dados da tabela que deseja exportar
    cursor.execute("SELECT * FROM competencias_gerais")

    # Recuperar todos os registros da consulta
    dados = cursor.fetchall()

    # Definir o nome do arquivo CSV de saída
    nome_arquivo_csv = 'competencias_gerais.csv'

    # Escrever os dados no arquivo CSV
    with open(nome_arquivo_csv, 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
    
        # Escrever o cabeçalho (nomes das colunas)
        escritor_csv.writerow([i[0] for i in cursor.description])
    
        # Escrever os dados
        escritor_csv.writerows(dados)

    # Fechar a conexão com o banco de dados
    conn.close()

    print(f'Dados exportados para {nome_arquivo_csv}')


def exportar_competencias_especificas():
    conn = sqlite3.connect('cadastro_planejamento.db')

    # Criar um cursor
    cursor = conn.cursor()

    # Executar uma consulta SQL para selecionar os dados da tabela que deseja exportar
    cursor.execute("SELECT * FROM competencias_especificas")

    # Recuperar todos os registros da consulta
    dados = cursor.fetchall()

    # Definir o nome do arquivo CSV de saída
    nome_arquivo_csv = 'competencias_especificas.csv'

    # Escrever os dados no arquivo CSV
    with open(nome_arquivo_csv, 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
    
        # Escrever o cabeçalho (nomes das colunas)
        escritor_csv.writerow([i[0] for i in cursor.description])
    
        # Escrever os dados
        escritor_csv.writerows(dados)

    # Fechar a conexão com o banco de dados
    conn.close()

    print(f'Dados exportados para {nome_arquivo_csv}')

def exportar_habilidades():
    conn = sqlite3.connect('cadastro_planejamento.db')

    # Criar um cursor
    cursor = conn.cursor()

    # Executar uma consulta SQL para selecionar os dados da tabela que deseja exportar
    cursor.execute("SELECT * FROM habilidades")

    # Recuperar todos os registros da consulta
    dados = cursor.fetchall()

    # Definir o nome do arquivo CSV de saída
    nome_arquivo_csv = 'habilidades.csv'

    # Escrever os dados no arquivo CSV
    with open(nome_arquivo_csv, 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
    
        # Escrever o cabeçalho (nomes das colunas)
        escritor_csv.writerow([i[0] for i in cursor.description])
    
        # Escrever os dados
        escritor_csv.writerows(dados)

    # Fechar a conexão com o banco de dados
    conn.close()

    print(f'Dados exportados para {nome_arquivo_csv}')
