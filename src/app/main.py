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
db.executeStatement(statement, verb="INSERT")


# Initial insert (Sala)
columns = ["descricao", "id_nivel"]
values = ["Sala Inicial", 1]
statement = sql.SQL("""INSERT INTO public.Sala({columns}) VALUES({values});""").format(
    columns=sql.SQL(", ").join(sql.Identifier(col) for col in columns),
    values=sql.SQL(", ").join(sql.Literal(val) for val in values)
)
db.executeStatement(statement, verb="INSERT")

# Initial insert (Sala)
columns = ["descricao", "id_nivel"]
values = ["Sala 2", 1]
statement = sql.SQL("""INSERT INTO public.Sala({columns}) VALUES({values});""").format(
    columns=sql.SQL(", ").join(sql.Identifier(col) for col in columns),
    values=sql.SQL(", ").join(sql.Literal(val) for val in values)
)
db.executeStatement(statement, verb="INSERT")

# Initial insert (Sala)
columns = ["descricao", "id_nivel"]
values = ["Sala 3", 1]
statement = sql.SQL("""INSERT INTO public.Sala({columns}) VALUES({values});""").format(
    columns=sql.SQL(", ").join(sql.Identifier(col) for col in columns),
    values=sql.SQL(", ").join(sql.Literal(val) for val in values)
)
db.executeStatement(statement, verb="INSERT")

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

'''
statement = sql.SQL("""SELECT * FROM public.Nivel, public.Sala, public.Jogador""")
response = db.executeStatement(statement, verb="SELECT", size=2000)
'''

statement2 = sql.SQL("""SELECT * FROM public.Nivel""")
response2 = db.executeStatement(statement2, verb="SELECT", size=2000)
statement3 = sql.SQL("""SELECT * FROM public.Sala""")
response3 = db.executeStatement(statement3, verb="SELECT", size=2000)
statement4 = sql.SQL("""SELECT * FROM public.Jogador""")
response4 = db.executeStatement(statement4, verb="SELECT", size=2000)

#print(response2)
#print(response3)
#print(response4)

print('Olá jogador! Você vê as seguintes salas a sua frente:\n\n')
print(response3)

choice = -1;

while(choice != 0):
    id = input('\n\n Digite o id da sala para a qual você deseja ir (Ou digite 0 para sair): ')
    if(int(id) == 0): 
        break
    print('Indo para a sala [', id, ']')
   
    statement = sql.SQL("""UPDATE TABLE public.Jogador SET id_sala = {id_destino} WHERE jogador(id) IS 1;""").format(
        id_destino=sql.Literal(int(id)))
