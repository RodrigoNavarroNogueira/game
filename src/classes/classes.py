import os

import textwrap
import dotenv
import pymysql

TABLE_NAME = 'characters'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

class Ser:
    def __init__(self):
        self.nome = None
        self.localizacao = []
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
        def __init__(self, id, online, xp, nome, altura, idade, sexo):
            super().__init__()
            self.id = id
            self.localizacao = ["base_map", 2, 3]
            self.online = online
            self.xp = xp
            self.nome = nome
            self.altura = altura
            self.idade = idade
            self.sexo = sexo
            self.talentos = ['forca', 'defesa', 'utilidade']
            self.ouro = 0
            self.cla = None
            self.mapa = None

    return Jogador


def instanciar_jogador(tipo_raca):
    class Jogador(tipo_raca):
        def __init__(self, id, nome, localizacao, online, nivel, xp, hp, mana, rage, buffs, debuffs, altura, idade, sexo, atributos, status, inventario, equips, ouro, emotes, raca, talentos, cla, mapa):
            super().__init__()
            self.id = id
            self.nome = nome
            self.localizacao = localizacao
            self.online = online
            self.nivel = nivel
            self.xp = xp
            self.hp = hp
            self.mana = mana
            self.rage = rage
            self.buffs = buffs
            self.debuffs = debuffs
            self.altura = altura
            self.idade = idade
            self.sexo = sexo
            self.atributos = atributos
            self.status = status
            self.inventario = inventario
            self.equips = equips
            self.ouro = ouro
            self.emotes = emotes
            self.raca = raca
            self.talentos = talentos
            self.cla = cla
            self.mapa = mapa

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
    def __init__(self, id, nome, raca, altura, idade, sexo):
        super().__init__()
        self.id = id
        self.nome = nome
        self.raca = raca
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
