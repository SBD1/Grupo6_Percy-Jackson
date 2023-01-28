from databaseHandler import DatabaseHandler
from psycopg2 import sql
import os

# DB Connection
db = DatabaseHandler(debug=False)
db.connect()


# Initial insert (Nivel)

columns = ["descricao"]
values = ["Inicial"]
statement = sql.SQL("""INSERT INTO public.Nivel({columns}) VALUES({values});""").format(
    columns=sql.SQL(", ").join(sql.Identifier(col) for col in columns),
    values=sql.SQL(", ").join(sql.Literal(val) for val in values)
)
db.executeStatement(statement, verb="INSERT")


# Initial insert (Sala)
columns = ["nome", "descricao", "id_nivel"]
values = ["ola", "Sala 3", 1]
statement = sql.SQL("""INSERT INTO public.Sala({columns}) VALUES({values});""").format(
    columns=sql.SQL(", ").join(sql.Identifier(col) for col in columns),
    values=sql.SQL(", ").join(sql.Literal(val) for val in values)
)
db.executeStatement(statement, verb="INSERT")

# Initial insert (Jogador)
columns = ["nome", "vida", "progresso",
           "ataque", "defesa", "id_sala", "id_nivel"]
values = ["Savio", 100, "50%", 50, 1, 1, 1]
statement = sql.SQL("""INSERT INTO public.Jogador({columns}) VALUES({values});""").format(
    columns=sql.SQL(", ").join(sql.Identifier(col) for col in columns),
    values=sql.SQL(", ").join(sql.Literal(val) for val in values)
)
# Executing insert statement
db.executeStatement(statement, verb="INSERT")

# Executing select statement

'''
statement = sql.SQL("""SELECT * FROM public.Nivel, public.Sala, public.Jogador""")
response = db.executeStatement(statement, verb="SELECT", size=2000)
'''

select_nivel = sql.SQL("""SELECT * FROM public.Nivel""")
niveis = db.executeStatement(select_nivel, verb="SELECT", size=2000)
select_salas = sql.SQL("""SELECT * FROM public.Sala""")
salas = db.executeStatement(select_salas, verb="SELECT", size=2000)
select_jogadores = sql.SQL("""SELECT * FROM public.Jogador""")
jogadores = db.executeStatement(select_jogadores, verb="SELECT", size=2000)

print('Olá jogador! Você vê as seguintes salas a sua frente:\n\n')
print(salas)

choice = -1

while (choice != 0):
    id = input(
        '\n\n Digite o id da sala para a qual você deseja ir (Ou digite 0 para sair): ')
    if (int(id) == 0):
        break
    print('Indo para a sala [', id, ']')

    statement = sql.SQL("""UPDATE TABLE public.Jogador SET id_sala = {id_destino} WHERE jogador(id) IS 1;""").format(
        id_destino=sql.Literal(int(id)))
