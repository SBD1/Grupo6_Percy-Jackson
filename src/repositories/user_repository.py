from psycopg2 import sql

from app.databaseHandler import DatabaseHandler


class UserRepository:
    def save_user(nome: str):
        db = DatabaseHandler(debug=False)
        db.connect()

        columns = ["nome", "vida", "progresso", "logar",
                   "ataque", "defesa", "id_sala", "id_nivel"]
        values = [nome, 100, "0%", 10, 50, 1, 1, 1]
        statement = sql.SQL("""INSERT INTO public.Jogador({columns}) VALUES({values});""").format(
            columns=sql.SQL(", ").join(sql.Identifier(col) for col in columns),
            values=sql.SQL(", ").join(sql.Literal(val) for val in values)
        )

        result = db.executeStatement(statement, verb='INSERT')

        if (result != True):
            print('erro')

    def find_user_by_name(name):
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

        return User(result[0], )
