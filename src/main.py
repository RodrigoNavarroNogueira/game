import os

import dotenv
import pymysql
import textwrap
import json
from classes.classes import Humano, Elfo, Criatura, Objeto, Npc, Item, criar_jogador, instanciar_jogador


def interacao(alvo, player):
    print(alvo.interagir(player))


# Jogador = criar_jogador(Humano)
# char = Jogador(1, False, 0, 'Navarro', 1.80, 30, 'Male')
# varss = vars(char)
# char_dict = {'id': varss['id']}
# char_dict.update({k: v for k, v in varss.items() if k != 'id'})
# print(char_dict)
# print()

# Jogador = criar_jogador(Elfo)
# char2 = Jogador(2, False, 0, 'Elfo', 1.82, 500, 'Female')
# varss = vars(char2)
# char2_dict = {'id': varss['id']}
# char2_dict.update({k: v for k, v in varss.items() if k != 'id'})
# print(char2_dict)
# print()

# orc = Criatura(1, 'Orc Fedorento', 'orc', 2, 300, 'Male')
# varss = vars(orc)
# monster_dict = {'id': varss['id']}
# monster_dict.update({k: v for k, v in varss.items() if k != 'id'})
# print(monster_dict)
# print()

# pedra = Objeto('Pedra')
# char.atacar(pedra)
# print()
# npc = Npc('Fazendeiro', 1.65, 60, 'Male')

# pocao = Item('Poção de Vida', 'vida', 10)
# espada = Item("Espada Enferrujada", "ataque", 10)

# interacao(pedra, char)

# TABLE_NAME = 'characters'

# dotenv.load_dotenv()

# connection = pymysql.connect(
#     host=os.environ['MYSQL_HOST'],
#     user=os.environ['MYSQL_USER'],
#     password=os.environ['MYSQL_PASSWORD'],
#     database=os.environ['MYSQL_DATABASE'],
# )

# with connection:
#     with connection.cursor() as cursor:
#         # SQL
#         cursor.execute(  # type: ignore
#             f"""CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
#                 id INT NOT NULL AUTO_INCREMENT,
#                 nome VARCHAR(100),
#                 online BOOLEAN NOT NULL,
#                 nivel INT,
#                 xp INT,
#                 hp INT,
#                 mana INT NULL,
#                 rage INT NULL,
#                 buffs JSON,
#                 debuffs JSON,
#                 altura FLOAT,
#                 idade INT,
#                 sexo VARCHAR(10),
#                 atributos JSON,
#                 status JSON,
#                 inventario JSON,
#                 equips JSON,
#                 ouro INT,
#                 emotes JSON,
#                 raca VARCHAR(50),
#                 talentos JSON,
#                 cla VARCHAR(100),
#                 mapa VARCHAR(100),
#                 PRIMARY KEY (id)
#             ) """
#         )
#        # CUIDADO: ISSO LIMPA A TABELA
#         cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')  # type: ignore
#     connection.commit()

#     with connection.cursor() as cursor:
#     # Transforma listas e dicionários em JSON para armazenar corretamente
#         for key in char_dict:
#             if isinstance(char_dict[key], (dict, list)):
#                 char_dict[key] = json.dumps(char_dict[key])

#         # Monta a query dinamicamente
#         columns = ", ".join(char_dict.keys())  # Pega os nomes das colunas
#         placeholders = ", ".join(["%s"] * len(char_dict))  # Placeholders %s
#         values = tuple(char_dict.values())  # Pega os valores do dicionário

#         sql = f"""INSERT INTO {TABLE_NAME} ({columns}) VALUES ({placeholders})"""

#         # Conectando ao banco de dados e executando a query

#         cursor.execute(sql, values)
#     connection.commit()

#     with connection.cursor() as cursor:
#     # Transforma listas e dicionários em JSON para armazenar corretamente
#         for key in char2_dict:
#             if isinstance(char2_dict[key], (dict, list)):
#                 char2_dict[key] = json.dumps(char2_dict[key])

#         # Monta a query dinamicamente
#         columns = ", ".join(char2_dict.keys())  # Pega os nomes das colunas
#         placeholders = ", ".join(["%s"] * len(char2_dict))  # Placeholders %s
#         values = tuple(char2_dict.values())  # Pega os valores do dicionário

#         sql = f"""INSERT INTO {TABLE_NAME} ({columns}) VALUES ({placeholders})"""

#         # Conectando ao banco de dados e executando a query

#         cursor.execute(sql, values)
#     connection.commit()

#     TABLE_NAME = 'monsters'

#     with connection.cursor() as cursor:
#         # SQL
#         cursor.execute(  # type: ignore
#             f"""CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
#                 id INT NOT NULL AUTO_INCREMENT,
#                 nome VARCHAR(100),
#                 nivel INT,
#                 hp INT,
#                 mana INT NULL,
#                 rage INT NULL,
#                 buffs JSON,
#                 debuffs JSON,
#                 altura FLOAT,
#                 idade INT,
#                 sexo VARCHAR(10),
#                 atributos JSON,
#                 status JSON,
#                 inventario JSON,
#                 equips JSON,
#                 ouro INT,
#                 emotes JSON,
#                 raca VARCHAR(50),
#                 PRIMARY KEY (id)
#             ) """
#         )
#         # CUIDADO: ISSO LIMPA A TABELA
#         cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')  # type: ignore
#     connection.commit()

#     with connection.cursor() as cursor:
#     # Transforma listas e dicionários em JSON para armazenar corretamente
#         for key in monster_dict:
#             if isinstance(monster_dict[key], (dict, list)):
#                 monster_dict[key] = json.dumps(monster_dict[key])

#         # Monta a query dinamicamente
#         columns = ", ".join(monster_dict.keys())  # Pega os nomes das colunas
#         placeholders = ", ".join(["%s"] * len(monster_dict))  # Placeholders %s
#         values = tuple(monster_dict.values())  # Pega os valores do dicionário

#         sql = f"""INSERT INTO {TABLE_NAME} ({columns}) VALUES ({placeholders})"""

#         # Conectando ao banco de dados e executando a query

#         cursor.execute(sql, values)
#     connection.commit()

#     with connection.cursor() as cursor:
#         sql = (
#             f'SELECT * FROM characters '
#         )
#         cursor.execute(sql)  # type: ignore
#         data5 = cursor.fetchall()  # type: ignore

#         for row in data5:
#             print(row)
#             print(type(data5))

#     with connection.cursor() as cursor:
#         sql = (
#             f'DELETE FROM characters '
#             'WHERE id = %s'
#         )
#         cursor.execute(sql, (2,))  # type: ignore
#         connection.commit()

#         cursor.execute(f'SELECT * FROM characters ')  # type: ignore

#         for row in cursor.fetchall():  # type: ignore
#             print(row)

#     with connection.cursor() as cursor:
#         sql = (
#             f'UPDATE monsters '
#             'SET hp=%s, rage=%s '
#             'WHERE id=%s'
#         )
#         cursor.execute(sql, (190, 10, 1))  # type: ignore
#         cursor.execute(f'SELECT * FROM monsters ')  # type: ignore
#         connection.commit()

#         for row in cursor.fetchall():  # type: ignore
#             print(row)

#     with connection.cursor() as cursor:
#         sql = (f'SELECT * FROM characters WHERE id=%s')
#         cursor.execute(sql, (1,))
#         data_char = cursor.fetchall()  # type: ignore


# Jogador = instanciar_jogador(Humano)
# char = Jogador(*data_char[0])


#interacao(npc, char)

# char.mostrar_status()
# char2.mostrar_status()
# orc.mostrar_status()
# print()

# char.atacar(orc)
# orc.mostrar_status()
# print()

# char2.atacar(orc)
# orc.mostrar_status()
# print()

# orc.atacar(char)
# char.mostrar_status()
# espada.usar(char)
# char.atacar(orc)
# orc.mostrar_status()
# pocao.usar(char)
# char.mostrar_status()

# FAZER A PRIMEIRA SKILL RACIAL DOS HUMANOS



# Ser
#  ├── Jogador
#  │     ├── Guerreiro
#  │     │     ├── Paladino
#  │     │     └── Berserker
#  │     ├── Mago
#  │     │     ├── Elementalista
#  │     │     └── Necromante
#  │     └── Arqueiro
#  │           ├── Atirador de Elite
#  │           └── Ladino
#  ├── Npc
#  ├── Criatura
#  └── Objeto

# Raca
#  ├── Humano
#  ├── Elfo
#  ├── Orc
#  └── Anão


# class Personagem:
#     def __init__(self, nome, tamanho, idade, sexo,
#     forca=1, agilidade=1, destreza=1, constituicao=1, inteligencia=1, vida=100, nivel=1, mana=None, classe=None, raca=None, cla=None):
#         self.nome = nome
#         self.tamanho = tamanho
#         self.idade = idade
#         self.sexo = sexo
#         self.atributos = {
#             'forca': forca,
#             'agilidade': agilidade,
#             'destreza': destreza,
#             'constituicao': constituicao,
#             'inteligencia': inteligencia
#         }


# boneco = Personagem('Navarro', 1.80, 30, 'Man')
# enemy = Personagem('Monstro', 1, 500, 'Male')
# print(f'Boneco criado: {vars(boneco)}')
# print(f'Inimigo criado: {vars(enemy)}')





# # Classe para um personagem
# class Personagem:
#     # Atributos padrão
#     vida_padrao = 100
#     ataque_padrao = 10

#     def __init__(self, nome, vida=None, ataque=None):
#         # Se valores não forem passados, usar os padrões da classe
#         self.nome = nome
#         self.vida = vida if vida is not None else self.vida_padrao
#         self.ataque = ataque if ataque is not None else self.ataque_padrao

#     def atacar(self, outro_personagem):
#         print(f"{self.nome} ataca {outro_personagem.nome} causando {self.ataque} de dano!")
#         outro_personagem.vida -= self.ataque
#         if outro_personagem.vida <= 0:
#             outro_personagem.vida = 0
#             print(f"{outro_personagem.nome} foi derrotado!")

#     def mostrar_status(self):
#         print(f"{self.nome}: Vida = {self.vida}, Ataque = {self.ataque}")

# # Classe para itens
# class Item:
#     def __init__(self, nome, efeito, valor):
#         self.nome = nome
#         self.efeito = efeito  # 'vida' ou 'ataque'
#         self.valor = valor    # Quanto será adicionado

#     def usar(self, personagem):
#         if self.efeito == "vida":
#             personagem.vida += self.valor
#             print(f"{personagem.nome} usou {self.nome} e recuperou {self.valor} de vida!")
#         elif self.efeito == "ataque":
#             personagem.ataque += self.valor
#             print(f"{personagem.nome} usou {self.nome} e ganhou {self.valor} de ataque!")
#         else:
#             print(f"O efeito {self.efeito} do item não é reconhecido.")

# # Criando objetos
# heroi = Personagem("Herói")
# inimigo = Personagem("Dragão", vida=200, ataque=20)
# pocao = Item("Poção de Vida", "vida", 50)
# espada = Item("Espada Flamejante", "ataque", 10)

# # Simulação de combate
# heroi.mostrar_status()
# inimigo.mostrar_status()

# heroi.atacar(inimigo)
# inimigo.mostrar_status()

# # Usar itens
# pocao.usar(heroi)
# espada.usar(heroi)

# # Status após usar os itens
# heroi.mostrar_status()


from main_functions.functions import *


def loop():
    while True:
        opcao = start()

        if opcao == 1:
            character_menu_options()
        elif opcao == 2:
            pass
        elif opcao == 3:
            print('\nFinalizando o programa, até mais!\n')
            raise SystemExit
# fazer não se mexer se tiver outro player, monstro, npc ou parede
# arrumar no banco de dados a coluna online
loop()
