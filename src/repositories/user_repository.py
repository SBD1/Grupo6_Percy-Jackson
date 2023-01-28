
import sys
sys.path.append('/src/app')

from app.users import User
from app.databaseHandler import DatabaseHandler
from psycopg2 import sql



class UserRepository:
    def save_user(self, nome):
        db = DatabaseHandler(debug=False)
        db.connect()

        columns = ["nome", "vida", "progresso",
                   "ataque", "defesa", "id_sala", "id_nivel"]
        values = [nome, 100, "0%", 50, 20, 1, 1]
        statement = sql.SQL("""INSERT INTO public.Jogador({columns}) VALUES({values});""").format(
            columns=sql.SQL(", ").join(sql.Identifier(col) for col in columns),
            values=sql.SQL(", ").join(sql.Literal(val) for val in values)
        )

        result = db.executeStatement(statement, verb='INSERT')

        if (result != True):
            print('erro')

    def find_user_by_name(self, name):
        db = DatabaseHandler(debug=False)
        db.connect()

        statement = sql.SQL(f"""
            SELECT 
                *
            FROM 
                public.Jogador AS J 
            WHERE 
                J.nome = {name}; 
        """)

        result = db.executeStatement(statement, verb='SELECT')

        return User(result[0], result[1], result[2],)
