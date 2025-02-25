import os

import dotenv
import pymysql
from classes.classes import *
import json

dotenv.load_dotenv()

def start():
    option = 0
    try:
        while option == 0 or option not in [1, 2, 3, 4]:
            option = int(input(
                "\nSelecione a opção que você deseja:\n"
                "[ 1 ] - Jogar\n"
                "[ 2 ] - Trocar Personagem\n"
                "[ 3 ] - Criar Novo Personagem\n"
                "[ 4 ] - Fechar o Programa\n\n"
            ))
            if type(option) is int and option not in [1, 2, 3, 4]:
                print('\nVocê não digitou uma opção válida')        
    except ValueError:
        print('\nVocê não digitou uma opção válida')
    return option


def login():
    connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],)

    with connection:
        with connection.cursor() as cursor:
            sql = (f'SELECT * FROM characters WHERE id=%s')
            cursor.execute(sql, (1,))
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


def exebicao():
    # funcao para mostrar o nome e id dos personagens já criados
    ...
