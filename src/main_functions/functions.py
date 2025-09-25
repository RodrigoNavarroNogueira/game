import os

import dotenv
import pymysql
from classes.classes import *
import json
import ast
from main_functions.combat import *

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
    
    race = data_char[0][20]
    race_map = {
        "Humano": Humano,
        "Elf": Elfo,
        "Orc": Orc,
        "Anão": Anao
    }
    RaceClass = race_map.get(race)

    if RaceClass is None:
        raise ValueError(f"Raça '{race}' não encontrada no mapeamento!")

    Jogador = instanciar_jogador(RaceClass)
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


def list_monsters():
    connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],)

    with connection:
        with connection.cursor() as cursor:
            sql = (f'SELECT * FROM monsters')
            cursor.execute(sql)
            monster_list = cursor.fetchall()  # type: ignore
    
    return monster_list


def character_menu_options():
    while True:
        char_list = list_characters()
        op = character_menu()

        if op == 1:
            char_id = character_select(char_list)
            if char_id:
                print('loading...')
                play(char_id)
        elif op == 2:
            criar_personagem()
        elif op == 3:
            char_id = character_select(char_list, delete=True)
            if char_id:
                excluir_personagem(char_id)
        elif op == 4:
            break


def criar_personagem():
    char_info = nick_altura_idade_sex()
    Jogador = criar_jogador(char_info[0])
    char = Jogador(1, False, 0, char_info[1], char_info[2], char_info[3], char_info[4])
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


def criar_criatura():
    orc = Criatura(1, 'aaa', ["base_map", 6, 10], 'orc', 2, 300, 'Male')
    monster_dict = vars(orc)
    monster_dict.pop('id')
    print(monster_dict)

    connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],)

    with connection.cursor() as cursor:
    # Transforma listas e dicionários em JSON para armazenar corretamente
        for key in monster_dict:
            if isinstance(monster_dict[key], (dict, list)):
                monster_dict[key] = json.dumps(monster_dict[key])

        # Monta a query dinamicamente
        columns = ", ".join(monster_dict.keys())  # Pega os nomes das colunas
        placeholders = ", ".join(["%s"] * len(monster_dict))  # Placeholders %s
        values = tuple(monster_dict.values())  # Pega os valores do dicionário

        sql = f"""INSERT INTO monsters ({columns}) VALUES ({placeholders})"""

        # Conectando ao banco de dados e executando a query

        cursor.execute(sql, values)
    connection.commit()


def character_select(char_list, delete=None):
    if len(char_list) <= 0:
        print('\nVocê ainda não criou nenhum personagem!')
    else:
        nick = ''
        print()
        for i, letra in enumerate(char_list):
            print(f'{i + 1} - {letra[1]}')
        
        if delete is not None:
            slot = int(input('\nSelecione o char que você quer excluir: \n'))
        else:
            slot = int(input('\nSelecione o char que você quer logar: \n\n'))

        for i, tupla in enumerate(char_list):
            i += 1
            if i == slot:
                nick = tupla[1]
    
        for t in char_list:
            if nick in t:
                return t[0]
            

def nick_altura_idade_sex():
    char_info = []
    raca = 0
    try:
        while raca == 0 or raca not in [1, 2, 3, 4]:
            raca = int(input(
                "\nSelecione a raça do seu personagem:\n\n"
                "[ 1 ] - Humano\n"
                "[ 2 ] - Elfo\n"
                "[ 3 ] - Anao\n"
                "[ 4 ] - Orc\n\n"
            ))
            if type(raca) is int and raca not in [1, 2, 3, 4]:
                print('\nVocê não digitou uma opção válida')        
    except ValueError:
        print('\nVocê não digitou uma opção válida')
    
    if raca == 1:
        char_info.append(Humano)
    elif raca == 2:
        char_info.append(Elfo)
    elif raca == 3:
        char_info.append(Anao)
    elif raca == 4:
        char_info.append(Orc)

    while True:
        nome = input('Nickname: ')
        if nome.isalpha() or all(c.isalpha() or c.isspace() for c in nome):
            nome = nome.strip()
            break
        else:
            print("Entrada inválida! O nome não pode conter números ou caracteres especiais.")
    char_info.append(nome)

    while True:
        altura = input('Altura do personagem: ')
        try:
            altura = float(altura)
            break
        except ValueError:
            print('Entrada inválida! Por favor, digite um número válido.')
    char_info.append(altura)

    while True:
        idade = input('Idade do personagem: ')
        try:
            idade = int(idade)
            break
        except ValueError:
            print('Entrada inválida! Por favor, digite um número válido.')
    char_info.append(idade)

    while True:
        sexo = input('Sexo do personagem (Male/Female): [M/F]: ').lower().strip()
        if sexo == 'm':
            char_info.append('Male')
            break
        elif sexo == 'f':
            char_info.append('Female')
            break
        else:
            print('Voce não digitou uma opção valida')

    return char_info


def excluir_personagem(char_id):
    connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],)

    with connection:
        with connection.cursor() as cursor:
            sql = (
                f'DELETE FROM characters '
                'WHERE id = %s'
            )
            cursor.execute(sql, (char_id,))  # type: ignore
            connection.commit()

    print(f'O personagem foi excluido!')


def load_map(monstros_instanciados, jogador_pos=None, monsters=None):
    mapa = [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    ]

    if jogador_pos:
        x, y = jogador_pos
        mapa[x][y] = 'P'

    if monsters:
        breakpoint()
        for n in range(0, len(monsters)):
            if monstros_instanciados[n].hp <= 0:
                monsters.pop(n)
        
        for m in monsters:
            x, y = m[1], m[2]
            mapa[x][y] = 'M'
    
    return mapa


def play(char_id):
    char = login(char_id)
    monstros_instanciados = load_monsters()
    coordenadas = gameplay(char, monstros_instanciados)
    s = json.dumps(coordenadas)
    char.localizacao = s
    char.online = False
    varss = vars(char)
    logoff(varss)


def gameplay(char, monstros_instanciados):
    # aqui esta vindo uma lista de objetos
    monster_list = list_monsters()
    monster_coordinates = []
    
    for n in range(0, len(monster_list)):
        lista = ast.literal_eval(monster_list[n][2])
        monster_coordinates.append(lista)
        monstros_instanciados[n].status = json.loads(monstros_instanciados[n].status)
        monstros_instanciados[n].mostrar_status()

    str_coord = char.localizacao
    coordenadas = ast.literal_eval(str_coord)

    char.status = json.loads(char.status)
    # char.nivel = 3
    # char.hp = 500
    # char.mana = 500
    char.inventario = json.loads(char.inventario)
    char.mostrar_status()

    while True:

        mapa = load_map(monstros_instanciados, jogador_pos=(coordenadas[1:3]), monsters=monster_coordinates)
        for linha in mapa:
            print(' '.join(linha))

        option = input(
            "\nSelecione a opção que você deseja:\n"
            "[ W ] - Andar para cima\n"
            "[ A ] - Andar para esquerda\n"
            "[ S ] - Andar para baixo\n"
            "[ D ] - Andar para direita\n"
            "[ Q ] - Atacar\n"
            "[ E ] - Interagir\n"
            "[ R ] - Defender\n"
            "[ L ] - Deslogar\n\n"
        ).upper()

        if option == 'W':
            aut = next_step_verify(mapa, coordenadas, 'W')
            if aut:
                coordenadas[1] -= 1
        elif option == 'A':
            aut = next_step_verify(mapa, coordenadas, 'A')
            if aut:
                coordenadas[2] -= 1
        elif option == 'S':
            aut = next_step_verify(mapa, coordenadas, 'S')
            if aut:
                coordenadas[1] += 1
        elif option == 'D':
            aut = next_step_verify(mapa, coordenadas, 'D')
            if aut:
                coordenadas[2] += 1
        elif option == 'Q':
            redor = aa_range_verify(mapa, coordenadas[1:])
            if not 'M' in redor or not '#' in redor:
                print('Você atacou, mas não acertou nada...')
            else:
                qtd_mons = redor.count('M')
                if qtd_mons == 1:
                    battle(char, monstros_instanciados[0])
                else:
                    print('Escolha qual monstro voce deseja enfrentar')
        elif option == 'L':
            return coordenadas


def next_step_verify(mapa, coordenadas, direction):
    if direction == 'W':
        next_step = mapa[coordenadas[1] - 1][coordenadas[2]]
        if next_step == ' ':
            return True
        else:
            print('Algo está bloqueando seu caminho...')
            return False
    elif direction == 'A':
        next_step = mapa[coordenadas[1]][coordenadas[2] - 1]
        if next_step == ' ':
            return True
        else:
            print('Algo está bloqueando seu caminho...')
            return False
    elif direction == 'S':
        next_step = mapa[coordenadas[1] + 1][coordenadas[2]]
        if next_step == ' ':
            return True
        else:
            print('Algo está bloqueando seu caminho...')
            return False
    elif direction == 'D':
        next_step = mapa[coordenadas[1]][coordenadas[2] + 1]
        if next_step == ' ':
            return True
        else:
            print('Algo está bloqueando seu caminho...')
            return False


def load_monsters():
    monster_list = list_monsters()
    monstros_instanciados = []
    for n in range(1, len(monster_list) + 1):
        connection = pymysql.connect(
        host=os.environ['MYSQL_HOST'],
        user=os.environ['MYSQL_USER'],
        password=os.environ['MYSQL_PASSWORD'],
        database=os.environ['MYSQL_DATABASE'],)

        with connection:
            with connection.cursor() as cursor:
                sql = (f'SELECT * FROM monsters WHERE id=%s')
                cursor.execute(sql, (n,))
                data_mons = cursor.fetchall()  # type: ignore

        Criatura = instanciar_criatura(Ser)
        monster = Criatura(*data_mons[0])
        monstros_instanciados.append(monster)

    return monstros_instanciados

