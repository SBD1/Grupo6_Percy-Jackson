from databaseHandler import DatabaseHandler
from psycopg2 import sql
import os

#DB Connection
db = DatabaseHandler(debug=False)
db.connect()



# Initial insert (test)
columns = ["nome", "idade", "poder"]
values = ["percy2", 94, "velocidade"]
statement = sql.SQL("""INSERT INTO public.test({columns}) VALUES({values});""").format(
    columns=sql.SQL(", ").join(sql.Identifier(col) for col in columns),
    values=sql.SQL(", ").join(sql.Literal(val) for val in values)
)

# Executing insert statement
db.executeStatement(statement, verb="INSERT")

# Executing select statement
statement2 = sql.SQL("""SELECT * FROM public.test""")
response = db.executeStatement(statement2, verb="SELECT", size=2000)

print(response)