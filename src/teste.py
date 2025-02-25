import os

import dotenv
import pymysql
import textwrap
import json
from classes.classes import Humano, Elfo, Criatura, Objeto, Npc, Item, criar_jogador, instanciar_jogador


def interacao(alvo, player):
    print(alvo.interagir(player))


def init_game():
    pass


Jogador = criar_jogador(Humano)
char = Jogador(1, False, 0, 'Navarro', 1.80, 30, 'Male')
varss = vars(char)
char_dict = {'id': varss['id']}
char_dict.update({k: v for k, v in varss.items() if k != 'id'})

Jogador = criar_jogador(Elfo)
char2 = Jogador(2, False, 0, 'Elfo', 1.82, 500, 'Female')
varss = vars(char2)
char2_dict = {'id': varss['id']}
char2_dict.update({k: v for k, v in varss.items() if k != 'id'})

TABLE_NAME = 'characters'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

with connection:
    with connection.cursor() as cursor:
        # SQL
        cursor.execute(  # type: ignore
            f"""CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                id INT NOT NULL AUTO_INCREMENT,
                nome VARCHAR(100),
                online BOOLEAN NOT NULL,
                nivel INT,
                xp INT,
                hp INT,
                mana INT NULL,
                rage INT NULL,
                buffs JSON,
                debuffs JSON,
                altura FLOAT,
                idade INT,
                sexo VARCHAR(10),
                atributos JSON,
                status JSON,
                inventario JSON,
                equips JSON,
                ouro INT,
                emotes JSON,
                raca VARCHAR(50),
                talentos JSON,
                cla VARCHAR(100),
                mapa VARCHAR(100),
                PRIMARY KEY (id)
            ) """
        )
       # CUIDADO: ISSO LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')  # type: ignore
    connection.commit()

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

    with connection.cursor() as cursor:
    # Transforma listas e dicionários em JSON para armazenar corretamente
        for key in char2_dict:
            if isinstance(char2_dict[key], (dict, list)):
                char2_dict[key] = json.dumps(char2_dict[key])

        # Monta a query dinamicamente
        columns = ", ".join(char2_dict.keys())  # Pega os nomes das colunas
        placeholders = ", ".join(["%s"] * len(char2_dict))  # Placeholders %s
        values = tuple(char2_dict.values())  # Pega os valores do dicionário

        sql = f"""INSERT INTO {TABLE_NAME} ({columns}) VALUES ({placeholders})"""

        # Conectando ao banco de dados e executando a query

        cursor.execute(sql, values)
    connection.commit()


connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

with connection:
    with connection.cursor() as cursor:
        sql = (f'SELECT * FROM characters WHERE id=%s')
        cursor.execute(sql, (1,))
        data_char = cursor.fetchall()  # type: ignore

    with connection.cursor() as cursor:
        sql = (f'SELECT * FROM characters WHERE id=%s')
        cursor.execute(sql, (2,))
        data_char2 = cursor.fetchall()  # type: ignore



Jogador = instanciar_jogador(Humano)
charrr = Jogador(*data_char[0])

Jogador = instanciar_jogador(Humano)
charrr2 = Jogador(*data_char2[0])

charrr.online = True
charrr2.online = True
charrr.status = json.loads(charrr.status)
charrr2.status = json.loads(charrr2.status)
charrr2.atacar(charrr)
charrr.nivel = 2
charrr.inventario = json.loads(charrr.inventario)
charrr.inventario.append('Espada Básica')
varss = vars(charrr)
print(varss)

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

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
