import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host= 'localhost',
        user = 'root',
        password= '',
        database= 'boletins',
    )
    return conexao

def cadastrar_aluno():
    conexao = conectar()
    mycursor = conexao.cursor()
    nome = input('DIGITE O NOME DO ALUNO!')
    serie = int(input('QUAL A SERIE DO ALUNO?'))
    sql = "INSERT INTO alunos (nome, serie) VALUES (%s, %s)"
    val = (nome, serie)
    mycursor.execute(sql, val)
    conexao.commit()
    mycursor.close()
    conexao.close()

def inserir_materia():
    conexao = conectar()
    mycursor = conexao.cursor()
    materia = input('DIGITE O NOME Da materia')
    sql = "INSERT INTO materias (nome) VALUES (%s)"
    val = (materia,)
    mycursor.execute(sql, val)
    conexao.commit()
    mycursor.close()
    conexao.close()

def motrar_alunos():
    conexao = conectar()
    mycursor = conexao.cursor()
    mycursor.execute("SELECT * FROM alunos")
    resultância = mycursor.fetchall()
    print(f'{"Id":^20}{"Aluno":^20}{"Série":^20}')
    for aluno in resultância: 
        print(f'{aluno[0]:^20}{aluno[1]:^20}{aluno[2]:^20}')
    mycursor.close()
    conexao.close()

def expulsar_aluno():
    conexao = conectar()
    mycursor = conexao.cursor()
    id = int(input('Quem vai sair da lista?'))
    sql = "DELETE FROM alunos WHERE id = %s "
    val = (id,)
    mycursor.execute(sql, val)
    conexao.commit()
    mycursor.close()
    conexao.close()


def atualizar_aluno():
    conexao = conectar()
    mycursor = conexao.cursor()
    id = int(input('Quem vai ser atualizado?'))
    nome = (input('Quem é o aluno?'))
    serie = int(input('Qual a serie?'))
    sql = "UPDATE alunos SET nome = %s, serie = %s WHERE id = %s"
    val = (nome, serie, id)
    mycursor.execute(sql, val)
    conexao.commit()
    mycursor.close()
    conexao.close()


def mostrar_aluno_join():   
    conexao = conectar()
    mycursor = conexao.cursor()
    sql = "SELECT \
    alunos.nome AS aluno, \
    materias.nome AS materias \
    FROM alunos_tem_materias \
    INNER JOIN alunos ON alunos_tem_materias.id_alunos = alunos.id \
    INNER JOIN materias ON alunos_tem_materias.id_materias = materias.id"
    mycursor.execute(sql)
    juncao = mycursor.fetchall()
    print(f'{"Aluno":^20}{"Matéria":^20}')
    for aluno in juncao: 
        print(f'{aluno[0]:^20}{aluno[1]:^20}')
    mycursor.close()
    conexao.close()


    
def aluno_especifico():
    conexao = conectar()
    mycursor = conexao.cursor()
    id = int(input('Qual o numro de aluno?'))
    sql = "SELECT * FROM alunos WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    frutos = mycursor.fetchall()
    for aluno in frutos:
        print(f'Aqui esta o aluno {aluno}')
    mycursor.close()
    conexao.close()


while True:
    print('''\nO que você precisa ?
1- Adicionar Dados
2- Inserir Matéria
3- Mostrar Alunos
4- Expulsar Aluno
5- Atualizar Aluno
6- Mostrar Tabelas Juntas
7- Mostrar aluno específico
8- Sair''')

    escolha = int(input('\n Sua resposta : '))

    if escolha == 1:
        cadastrar_aluno()

    elif escolha == 2:
        inserir_materia()

    elif escolha == 3:
        motrar_alunos()

    elif escolha == 4:
        expulsar_aluno()

    elif escolha == 5:
        atualizar_aluno()
    
    elif escolha == 6:
        mostrar_aluno_join()
    
    elif escolha == 7:
        aluno_especifico()
    
    elif escolha == 8:
        print ('até mais...')

        break

    else:
        print('Opção inválida!')