import os

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

with connection:
    with connection.cursor() as cursor:
        # SQL
        cursor.execute(  # type: ignore
            f"""CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                id INT NOT NULL AUTO_INCREMENT,
                nome VARCHAR(100),
                localizacao JSON,
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
