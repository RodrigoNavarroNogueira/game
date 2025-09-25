import os

import dotenv
import pymysql
from classes.classes import *
import json
import ast
import time


def aa_range_verify(mapa, coordenadas):
    a1 = mapa[coordenadas[0] - 1][coordenadas[1]] #w
    a2 = mapa[coordenadas[0]][coordenadas[1] - 1] #a
    a3 = mapa[coordenadas[0] + 1][coordenadas[1]] #s
    a4 = mapa[coordenadas[0]][coordenadas[1] + 1] #d
    a5 = mapa[coordenadas[0] - 1][coordenadas[1] + 1] #3
    a6 = mapa[coordenadas[0] - 1][coordenadas[1] - 1] #1
    a7 = mapa[coordenadas[0] + 1][coordenadas[1] + 1] #9
    a8 = mapa[coordenadas[0] + 1][coordenadas[1] - 1] #7
    redor = [a1, a2, a3, a4, a5, a6, a7, a8]
    return redor

    # char.atacar(monster)
    # monster.mostrar_status()
    # print()

    # monster.atacar(char)
    # char.mostrar_status()
    # #espada.usar(char)
    # char.atacar(monster)
    # monster.mostrar_status()
    # #pocao.usar(char)
    # char.mostrar_status()


def battle(char, monster):
    while char.hp or monster.hp > 0:
        char.atacar(monster)
        char.usar_magia(monster)
        if monster.hp <= 0:
            print('A LUTA ACABOU!')
            break
        else:
            time.sleep(1)
        monster.atacar(char)
        if char.hp <= 0:
            print('A LUTA ACABOU!')
            break
        else:
            time.sleep(1)
        time.sleep(1)

        char.mostrar_status()
        monster.mostrar_status()