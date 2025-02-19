import os

import dotenv
import pymysql
import textwrap

class Ser:
    def __init__(self):
        self.nome = None
        self.nivel = 1
        self.hp = 1
        self.mana = None
        self.rage = None
        self.buffs = []
        self.debuffs = []
        self.altura = None
        self.idade = None
        self.sexo = None
        self.atributos = {'forca': 1, 'agilidade': 1, 'destreza': 1, 'constituicao': 1, 'inteligencia': 1}
        self.status = {'ad': 1, 'ap': 1, 'deff': 1, 'mdef': 1, 'vel_atk': 1, 'cd': 1, 'crit': 1, 'vel_mov': 1}
        self.inventario = []
        self.equips = ['cabeça','armadura', 'calça', 'bota', 'luva', 'mao_direita', 'mao_esquerda', 'acessorio1', 'acessorio2']
        self.ouro = None
        self.emotes = []

    def atacar(self, alvo):
        alvo.hp -= self.status['ad']
        print(f'{self.nome} atacou {alvo.nome} causando {self.status["ad"]} de dano!')
        if alvo.hp <= 0:
            alvo.hp = 0
            print(f'{alvo.nome} foi derrotado!')

    def mostrar_status(self):
        print(f'{self.nome}: Vida = {self.hp}, Ataque = {self.status["ad"]}')

    def interagir(self, alvo):
        print(f'{self.nome} está interagindo com {alvo.nome}...')


class Humano(Ser):
    def __init__(self):
        super().__init__()
        self.raca = 'Humano'
        self.hp = 100
        self.mana = 50
        self.atributos = {'forca': 8, 'agilidade': 7, 'destreza': 7, 'constituicao': 8, 'inteligencia': 10}
        self.status = {'ad': 8, 'ap': 10, 'deff': 8, 'mdef': 8, 'vel_atk': 1, 'cd': 1, 'crit': 1, 'vel_mov': 1}

    def proeficiencia_espada(self):
        # se estiver com uma espada equipada, ela ganha +10 de dano
        ...

    def determinacao(self):
        # self.status lambda # vamos usar uma lambda para aumentar em 10% todos os status por 10s 
        ...


class Orc(Ser):
    def __init__(self):
        super().__init__()
        self.raca = 'Orc'
        self.hp = 120
        self.rage = 0
        self.atributos = {'forca': 10, 'agilidade': 8, 'destreza': 7, 'constituicao': 9, 'inteligencia': 6}
        self.status = {'ad': 10, 'ap': 6, 'deff': 9, 'mdef': 9, 'vel_atk': 1, 'cd': 1, 'crit': 1, 'vel_mov': 1}

    def proeficiencia_espada(self):
        # se estiver com uma espada equipada, ela ganha +10 de dano
        ...

    def furia_dos_orcs(self, alvo):
        # atordoa o alvo por 2s
        ...


class Elfo(Ser):
    def __init__(self):
        super().__init__()
        self.raca = 'Elf'
        self.hp = 100
        self.mana = 50
        self.atributos = {'forca': 7, 'agilidade': 9, 'destreza': 10, 'constituicao': 7, 'inteligencia': 7}
        self.status = {'ad': 7, 'ap': 7, 'deff': 7, 'mdef': 7, 'vel_atk': 1.1, 'cd': 1, 'crit': 1, 'vel_mov': 1}

    def proeficiencia_arco(self):
        # se estiver com um arco equipado, ele ganha +10 de dano
        ...

    def proeficiencia_adaga(self):
        # se estiver com uma adaga equipada, ela ganha +10 de dano
        ...

    def respiro_elfico(self):
        # Tira CC ou cura
        ...


class Anao(Ser):
    def __init__(self):
        super().__init__()
        self.raca = 'Anão'
        self.hp = 100
        self.mana = 50
        self.atributos = {'forca': 9, 'agilidade': 7, 'destreza': 7, 'constituicao': 10, 'inteligencia': 7}
        self.status = {'ad': 9, 'ap': 7, 'deff': 10, 'mdef': 10, 'vel_atk': 1, 'cd': 1, 'crit': 1, 'vel_mov': 1}

    def proeficiencia_machado(self):
        # se estiver com um machado equipado, ele ganha +10 de dano
        ...

    def pele_dura(self):
        # Ganha 30% de resistência a dano por 10 segundos, só pode ser usado com menos de 50% da vida. CD: 60s 
        ...

def criar_jogador(tipo_raca):
    class Jogador(tipo_raca):
        def __init__(self, nome, altura, idade, sexo):
            super().__init__()
            self.nome = nome
            self.altura = altura
            self.idade = idade
            self.sexo = sexo
            self.talentos = ['forca', 'defesa', 'utilidade']
            self.ouro = 0
            self.cla = None
            self.mapa = None

    return Jogador


class Npc(Elfo):
    def __init__(self, nome, altura, idade, sexo):
        super().__init__()
        dialogo = None
        self.nome = nome
        self.altura = altura
        self.idade = idade
        self.sexo = sexo
        self.ouro = 0
        self.loja = {'Espada': 100, 'Adaga': 70, 'Arco': 60, 'Machado': 120}
    # Falar com um NPC
    # trade
    def interagir(self, alvo):
        super().interagir(alvo)
        opcao = int(input(textwrap.dedent(f"""
        Olá {alvo.nome}, em que posso te ajudar hoje?

        1 - Dialogo...
        2 - O que você tem a venda?
        """).strip()))
        if opcao == 1:
            return 'Bom... vejo que você é novo por aqui, vou lhe contar o que anda acontecendo...'
        elif opcao == 2:
            loja = dict(self.loja)
            for item, preco in loja.items():
                print(f'{item} - {preco}G')
            return f'Seu gold: {alvo.ouro}'
 

class Criatura(Ser):
    def __init__(self, nome, tipo, altura, idade, sexo):
        super().__init__()
        self.nome = nome
        self.tipo = tipo
        self.altura = altura
        self.idade = idade
        self.sexo = sexo
        self.hp = 200
        self.rage = 0
        self.atributos = {'forca': 10, 'agilidade': 5, 'destreza': 5, 'constituicao': 9, 'inteligencia': 3}
        self.status = {'ad': 10, 'ap': 3, 'deff': 9, 'mdef': 9, 'vel_atk': 1, 'cd': 1, 'crit': 1, 'vel_mov': 1}


class Objeto(Ser):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome

    def interagir(self, alvo):
        return f'É apenas uma {self.nome}'


class Guerreiro():
    ...


class Mago():
    ...


class Arqueiro():
    ...


class Item:
    def __init__(self, nome, efeito, qtd):
        self.nome = nome
        self.efeito = efeito  # 'vida' ou 'ataque'
        self.qtd = qtd    # Quanto será adicionado
        self.descricao = ''

    def usar(self, personagem):
        if self.efeito == "vida":
            personagem.hp += self.qtd
            print(f"{personagem.nome} usou {self.nome} e recuperou {self.qtd} de vida!")
        elif self.efeito == "ataque":
            personagem.status['ad'] += self.qtd
            print(f"{personagem.nome} equipou {self.nome} e ganhou {self.qtd} de ataque!")
        else:
            print(f"O efeito {self.efeito} do item não é reconhecido.")


def interacao(alvo, player):
    print(alvo.interagir(player))


Jogador = criar_jogador(Humano)
char = Jogador('Navarro', 1.80, 30, 'Male')
print(vars(char))
print()

Jogador = criar_jogador(Elfo)
char2 = Jogador('Elfo', 1.82, 500, 'Female')
print(vars(char2))
print()

orc = Criatura('Orc Fedorento', 'orc', 2, 300, 'Male')
print(vars(orc))
print()


pedra = Objeto('Pedra')
char.atacar(pedra)
print()
npc = Npc('Fazendeiro', 1.65, 60, 'Male')

pocao = Item('Poção de Vida', 'vida', 10)
espada = Item("Espada Enferrujada", "ataque", 10)

interacao(pedra, char)

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
                nivel INT,
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
        cursor.execute(  # type: ignore
            f"""INSERT INTO {TABLE_NAME} (
                id, nome, nivel, hp, mana, rage, buffs, debuffs, altura, idade, sexo, 
                atributos, status, inventario, equips, ouro, emotes, raca, talentos, cla, mapa
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )""",
            (
                1, 'Navarro', 1, 100, 50, None, 
                '[]', '[]', 1.8, 30, 'Male',
                '{"forca": 8, "agilidade": 7, "destreza": 7, "constituicao": 8, "inteligencia": 10}', 
                '{"ad": 8, "ap": 10, "deff": 8, "mdef": 8, "vel_atk": 1, "cd": 1, "crit": 1, "vel_mov": 1}', 
                '[]', 
                '["cabeça", "armadura", "calça", "bota", "luva", "mao_direita", "mao_esquerda", "acessorio1", "acessorio2"]', 
                0, '[]', 'Humano', 
                '["forca", "defesa", "utilidade"]', 
                None, None
            )
        )
    connection.commit()

    with connection.cursor() as cursor:
        cursor.execute(  # type: ignore
            f"""INSERT INTO {TABLE_NAME} (
                id, nome, nivel, hp, mana, rage, buffs, debuffs, altura, idade, sexo, 
                atributos, status, inventario, equips, ouro, emotes, raca, talentos, cla, mapa
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )""",
            (
                2, 'Elfo', 1, 100, 50, None, 
                '[]', '[]', 1.82, 500, 'Female',
                '{"forca": 7, "agilidade": 9, "destreza": 10, "constituicao": 7, "inteligencia": 7}', 
                '{"ad": 7, "ap": 7, "deff": 7, "mdef": 7, "vel_atk": 1.1, "cd": 1, "crit": 1, "vel_mov": 1}', 
                '[]', 
                '["cabeça", "armadura", "calça", "bota", "luva", "mao_direita", "mao_esquerda", "acessorio1", "acessorio2"]', 
                0, '[]', 'Elf', 
                '["forca", "defesa", "utilidade"]', 
                None, None
            )
        )
    connection.commit()

    TABLE_NAME = 'monsters'

    with connection.cursor() as cursor:
        # SQL
        cursor.execute(  # type: ignore
            f"""CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                id INT NOT NULL AUTO_INCREMENT,
                nome VARCHAR(100),
                nivel INT,
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
                PRIMARY KEY (id)
            ) """
        )
        # CUIDADO: ISSO LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')  # type: ignore
    connection.commit()

    with connection.cursor() as cursor:
        cursor.execute(  # type: ignore
            f"""INSERT INTO {TABLE_NAME} (
                id, nome, nivel, hp, mana, rage, buffs, debuffs, altura, idade, sexo, 
                atributos, status, inventario, equips, ouro, emotes, raca
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )""",
            (
                1, 'Orc Fedorento', 1, 200, None, 0, 
                '[]', '[]', 2.2, 300, 'Male',
                '{"forca": 10, "agilidade": 5, "destreza": 5, "constituicao": 9, "inteligencia": 3}', 
                '{"ad": 10, "ap": 3, "deff": 9, "mdef": 9, "vel_atk": 1, "cd": 1, "crit": 1, "vel_mov": 1}', 
                '[]', 
                '["cabeça", "armadura", "calça", "bota", "luva", "mao_direita", "mao_esquerda", "acessorio1", "acessorio2"]', 
                0, '[]', 'Orc',
            )
        )
    connection.commit()


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
