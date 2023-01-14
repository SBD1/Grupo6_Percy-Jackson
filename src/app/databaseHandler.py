import psycopg2
import psycopg2.extras
import configFunctions
from constants import VALID_REST_VERBS


class DatabaseHandler:
    def __init__(self, filename="config.ini", section="database", debug=False) -> None:
        # Database related operators
        self.conn = None  # Database connection
        self.cursor = None  # Cursor for transactions when connected

        # Parse Database configuration data from database.ini config file
        # Declare a new parser
        self.databaseParameters = configFunctions.getConfigParameters(section, filename, debug)

    def __del__(self) -> None:
        print("Terminanting: Deleting and closing connection")
        self.closeConnection()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Cleaning up")
        self.closeConnection()

    def connect(self, databaseName=None) -> None:
        # Default to the database name in the configuration file
        if databaseName is None:
            databaseName = self.databaseParameters["database"]

        # Check if there already is a connection to the database, if so, raise Exception
        if self.conn is not None:
            raise Exception("Connection to {0} already open".format(databaseName))

        try:
            # Connect to the PostgreSQL database specified by databaseName
            print('Connecting to the {0} database...'.format(databaseName))

            # Connect to request database using databaseParameters
            self.conn = psycopg2.connect(host=self.databaseParameters["host"], user=self.databaseParameters["user"], password=self.databaseParameters["password"], dbname=databaseName)

            # Create a cursor
            self.cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            if(self.cursor):
                print('Successfully connected to database!')
                
        except (Exception, psycopg2.DatabaseError) as error:
            print('An error occured: ', error)

    def closeConnection(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.cursor = None
            print("Closed database connection")

    def executeStatement(self, statement, verb, size=1):
        if verb not in VALID_REST_VERBS:
            return None

        # Execute the statement
        self.cursor.execute(statement)

        if verb == "SELECT":
            # Get as many rows as desired, defaults to 1 which fulfills the role of fetchone(), fetchmany() and fetchall()
            if size == 1:
                response = self.cursor.fetchone()
            else:
                response = self.cursor.fetchmany(size)

            return response
        else:
            return True