import argparse
import psycopg2

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import Error

parser = argparse.ArgumentParser()
parser.add_argument('--db_name', type=str, default='sensor_data',
                    help='Database name.')
parser.add_argument('--user', type=str, default='postgres',
                    help='Username to connect to the database.')
parser.add_argument('--password', type=str, default='my_password',
                    help='Password to connect to the database.')
parser.add_argument('--host', type=str, default='localhost',
                    help='The name of the server or IP address.')
parser.add_argument('--port', type=str, default='5432',
                    help='Port for connecting to the database.')
args = parser.parse_args()


def create_connection(db_user, db_password,
                      db_host, db_port, db_name=None):
    """A function to create a connection to a PostgreSQL database instance.

    Parameters:
    ----------
        - db_user: type[`str`]

        Username to connect to the database.

        - db_password: type[`str`]

        Password to connect to the database.

        - db_host: type[`str`]

        The name of the server or IP address that the database is running on.

        - db_port: type[`str`]

        Port for connecting to the database.

        - db_name: type[`str`]

        Database name.

    Returns:
    -------
        type[`psycopg2.extensions.connection`]

        A connection object to a PostgreSQL database instance.
    """

    print('Connection to PostgreSQL...')
    connection = None
    try:
        connection = psycopg2.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
            database=db_name
        )
        print("Connection to PostgreSQL successful.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return connection


def create_database(connection: psycopg2.extensions.connection) -> None:
    """Database creation in PostgreSQL.

    Database for data from the sensor.

    Parameters:
    ----------
        - connection: type[`psycopg2.extensions.connection`]

        A connection object to a PostgreSQL database instance.

    Returns:
    -------
        type[`bool`]: whether the database was created or not.
    """

    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()

    print('Database creation...')
    try:
        create_db_query = 'CREATE DATABASE sensor_data'
        cursor.execute(create_db_query)
        print('The database has been created successfully.')
    except (Exception, Error) as error:
        print(error)
    else:
        connection.commit()
        return True


def create_table(connection: psycopg2.extensions.connection) -> None:
    """Function for creating a table in a database.

    Table for data that comes from the sensor.

    The table consists of columns, where id is an automatically generated id,
    temperature is a float numeric field, pressure is a float numeric field,
    alt is a float numeric field, humidity is a float numeric field,
    timestamp is a time field.

    Parameters:
    ----------
        - connection: type[`psycopg2.extensions.connection`]

        A connection object to a PostgreSQL database instance.
    """

    cursor = connection.cursor()

    create_table_query = '''CREATE TABLE input_data
                         (ID INT PRIMARY KEY NOT NULL
                            GENERATED ALWAYS AS IDENTITY,
                         TEMPERATURE REAL NOT NULL,
                         PRESSURE REAL NOT NULL,
                         ALT REAL NOT NULL,
                         HUMIDITY REAL NOT NULL,
                         TIMESTAMP TIMESTAMP WITHOUT TIME ZONE NOT NULL);
                         '''
    print('Creating a table...')
    try:
        cursor.execute(create_table_query)
        connection.commit()
        print('The table was created successfully.')
    except (Exception, Error) as error:
        print(error)
    else:
        connection.commit()


if __name__ == "__main__":

    connection = create_connection(
        args.user,
        args.password,
        args.host,
        args.port
    )

    if create_database(connection):
        connection = create_connection(
            args.user,
            args.password,
            args.host,
            args.port,
            args.db_name
        )
        create_table(connection)
