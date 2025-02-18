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
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        print(cursor)
       # CUIDADO: ISSO LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')  # type: ignore
    connection.commit()

    # Começo a manipular dados a partir daqui

    with connection.cursor() as cursor:
        cursor.execute(  # type: ignore
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES ("Rodrigo", 23) '
        )
        cursor.execute(  # type: ignore
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES ("Miguel", 24) '
        )
        result = cursor.execute(  # type: ignore
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES ("Rafael", 25) '
        )
        print(result)
    connection.commit()
