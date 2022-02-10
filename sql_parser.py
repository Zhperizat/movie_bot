import sqlite3


class SQLighter:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def get_user_info(self, table, id):
        """Получаем всех активных подписчиков бота"""
        query=f"""SELECT name, year, city FROM `{table}` WHERE `id` = '{id}' """
        with self.connection:
            return self.cursor.execute(query).fetchone()

    def get_all_films(self, table):
        """Получаем всех активных подписчиков бота"""
        query=f"""SELECT * FROM `{table}`"""
        with self.connection:
            return self.cursor.execute(query).fetchone()

    def user_exists(self, user_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute("""SELECT * FROM `hospi_info` WHERE `user_id`=? """, (user_id,)).fetchall()
            return bool(len(result))

    def add_new_movies(self, name, year, city):
        """Добавляем нового подписчика"""
        query = f"""INSERT INTO `fentezi` (`name`, `year`, `city`) 
        VALUES( '{name}', '{year}', '{city}')"""
        with self.connection:
            return self.cursor.execute(query)

    def create_table(self):
        with self.connection:
            query = """CREATE TABLE IF NOT EXISTS fentezi(
                `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , 
                `name` TEXT, 
                `year` TEXT, 
                `city` TEXT) """
            return self.cursor.execute(query)

    def table_exist(self):
        c = self.cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='hospi_info' ''')
        # if the count is 1, then table exists
        if c.fetchone()[0] == 1:
            print('Table exists.')
            return True
        else:
            print('Table does not exist.')
            return False

    def update_info(self, user_id, field, text):
        """Обновляем статус подписки пользователя"""
        query=f"""UPDATE `hospi_info` SET `{field}`='{text}' WHERE `user_id` = '{user_id}' """
        with self.connection:
            return self.cursor.execute(query)

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()