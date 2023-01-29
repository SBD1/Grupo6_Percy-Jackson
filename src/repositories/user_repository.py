
import sys
from psycopg2 import sql

from app.users import User
from app.databaseHandler import DatabaseHandler



class UserRepository:
    def __init__(self) -> None:
        self.db = DatabaseHandler(debug=False)
        self.db.connect()

    def __del__(self) -> None:
        self.db.closeConnection()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.closeConnection()
    
    def save_user(self, nome):
        columns = ["nome", "vida", "progresso",
                   "ataque", "defesa", "id_sala", "id_nivel"]
        values = [nome, 100, "0%", 50, 20, True, 1, 1]
        statement = sql.SQL("""INSERT INTO public.Jogador({columns}) VALUES({values});""").format(
            columns=sql.SQL(", ").join(sql.Identifier(col) for col in columns),
            values=sql.SQL(", ").join(sql.Literal(val) for val in values)
        )

        result = self.db.executeStatement(statement, verb='INSERT')

        if (result != True):
            print('erro')

    def find_user_by_name(self, name):
        statement = sql.SQL(f"""
            SELECT 
                *
            FROM 
                public.Jogador AS J 
            WHERE 
                J.nome = {name}; 
        """)

        result = self.db.executeStatement(statement, verb='SELECT')

        # return User(result[0], result[1], result[2],)
        return True
    
    def load_character(self, nome):
        columns = ["nome", "vida", "progresso",
                   "ataque", "defesa", "logado", "id_sala", "id_nivel"]
        values = [nome, 100, "0%", 50, 20, True, 1, 1]
        statement = sql.SQL("""INSERT INTO public.Jogador({columns}) VALUES({values});""").format(
            columns=sql.SQL(", ").join(sql.Identifier(col) for col in columns),
            values=sql.SQL(", ").join(sql.Literal(val) for val in values)
        )

        result = self.db.executeStatement(statement, verb='INSERT')

        if (result != True):
            print('erro')