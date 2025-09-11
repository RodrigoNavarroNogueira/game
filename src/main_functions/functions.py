import os

import dotenv
import pymysql
from classes.classes import *
import json

dotenv.load_dotenv()

def start():
    option = 0
    try:
        while option == 0 or option not in [1, 2, 3]:
            option = int(input(
                "\nSelecione a opção que você deseja:\n"
                "[ 1 ] - Jogar\n"
                "[ 2 ] - Configurações\n"
                "[ 3 ] - Fechar o Programa\n\n"
            ))
            if type(option) is int and option not in [1, 2, 3]:
                print('\nVocê não digitou uma opção válida')        
    except ValueError:
        print('\nVocê não digitou uma opção válida')
    return option


def character_menu():
    option = 0
    try:
        while option == 0 or option not in [1, 2, 3, 4]:
            option = int(input(
                "\nSelecione a opção que você deseja:\n"
                "[ 1 ] - Logar um Personagem\n"
                "[ 2 ] - Criar um Personagem\n"
                "[ 3 ] - Excluir Personagem\n"
                "[ 4 ] - Voltar ao início\n\n"
            ))
            if type(option) is int and option not in [1, 2, 3, 4]:
                print('\nVocê não digitou uma opção válida')        
    except ValueError:
        print('\nVocê não digitou uma opção válida')
    return option


def login(char_id):
    connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],)

    with connection:
        with connection.cursor() as cursor:
            sql = (f'SELECT * FROM characters WHERE id=%s')
            cursor.execute(sql, (char_id,))
            data_char = cursor.fetchall()  # type: ignore

    Jogador = instanciar_jogador(Humano)
    char = Jogador(*data_char[0])
    char.online = True
    return char


def logoff(varss):
    connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],)

    with connection:
        with connection.cursor() as cursor:
            for key in varss:
                if isinstance(varss[key], (dict, list)):
                    varss[key] = json.dumps(varss[key])

            set_clause = ', '.join([f"{key} = %s" for key in varss.keys()])
            values = list(varss.values())

            user_id = varss['id']

            values.append(user_id)

            query = f"UPDATE characters SET {set_clause} WHERE id = %s"

            # Executando a query
            cursor.execute(query, values)
        connection.commit()


def list_characters():
    connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],)

    with connection:
        with connection.cursor() as cursor:
            sql = (f'SELECT * FROM characters')
            cursor.execute(sql)
            char_list = cursor.fetchall()  # type: ignore
    
    return char_list


def character_menu_options(char_list):
    op = character_menu()

    if op == 1:
        char_id = character_select(char_list)
        print('logandoo,..')
        char = login(char_id)
        char.status = json.loads(char.status)
        char.nivel = 3
        char.hp = 100
        char.inventario = json.loads(char.inventario)
        varss = vars(char)
        logoff(varss)
    elif op == 2:
        print('AQUIUIIIIIIIII')
        criar_personagem()
    elif op == 3:
        ...
    elif op == 4:
        ...


def criar_personagem():
    Jogador = criar_jogador(Humano)
    char = Jogador(1, False, 0, 'Navas', 1.80, 30, 'Male')
    char_dict = vars(char)
    char_dict.pop('id')
    print(char_dict)

    connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],)

    with connection.cursor() as cursor:
    # Transforma listas e dicionários em JSON para armazenar corretamente
        for key in char_dict:
            if isinstance(char_dict[key], (dict, list)):
                char_dict[key] = json.dumps(char_dict[key])

        # Monta a query dinamicamente
        columns = ", ".join(char_dict.keys())  # Pega os nomes das colunas
        placeholders = ", ".join(["%s"] * len(char_dict))  # Placeholders %s
        values = tuple(char_dict.values())  # Pega os valores do dicionário

        sql = f"""INSERT INTO {TABLE_NAME} ({columns}) VALUES ({placeholders})"""

        # Conectando ao banco de dados e executando a query

        cursor.execute(sql, values)
    connection.commit()


def character_select(char_list):
    if len(char_list) <= 0:
        print('\nVocê ainda não criou nenhum personagem!')
    else:
        nick = ''
        for i, letra in enumerate(char_list):
            print(f'{i + 1} - {letra[1]}')
        
        slot = int(input('\nSelecione o char que você quer logar: \n'))

        for i, tupla in enumerate(char_list):
            i += 1
            if i == slot:
                nick = tupla[1]
    
        for t in char_list:
            if nick in t:
                return t[0]