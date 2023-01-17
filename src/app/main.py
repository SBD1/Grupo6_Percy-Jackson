from databaseHandler import DatabaseHandler
from psycopg2 import sql
import os

#DB Connection
db = DatabaseHandler(debug=False)
db.connect()



# Initial insert (Nivel)
columns = ["descricao"]
values = ["Inicial"]
statement = sql.SQL("""INSERT INTO public.Nivel({columns}) VALUES({values});""").format(
    columns=sql.SQL(", ").join(sql.Identifier(col) for col in columns),
    values=sql.SQL(", ").join(sql.Literal(val) for val in values)
)
# Initial insert (Sala)
columns = ["descricao", "id_nivel"]
values = ["Inicial", 1]
statement = sql.SQL("""INSERT INTO public.Sala({columns}) VALUES({values});""").format(
    columns=sql.SQL(", ").join(sql.Identifier(col) for col in columns),
    values=sql.SQL(", ").join(sql.Literal(val) for val in values)
)
# Initial insert (Jogador)
columns = ["progresso", "vida", "logar", "ataque", "defesa", "id_sala", "id_nivel"]
values = ["inicial", 100, 1, 10, 50, 1, 1]
statement = sql.SQL("""INSERT INTO public.Jogador({columns}) VALUES({values});""").format(
    columns=sql.SQL(", ").join(sql.Identifier(col) for col in columns),
    values=sql.SQL(", ").join(sql.Literal(val) for val in values)
)
# Executing insert statement
db.executeStatement(statement, verb="INSERT")

# Executing select statement
statement2 = sql.SQL("""SELECT * FROM public.Nivel""")
response2 = db.executeStatement(statement2, verb="SELECT", size=2000)
statement3 = sql.SQL("""SELECT * FROM public.Sala""")
response3 = db.executeStatement(statement3, verb="SELECT", size=2000)
statement4 = sql.SQL("""SELECT * FROM public.Jogador""")
response4 = db.executeStatement(statement4, verb="SELECT", size=2000)

print(response2)
print(response3)
print(response4)