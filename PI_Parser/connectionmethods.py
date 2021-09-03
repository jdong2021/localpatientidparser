"""
Defines various methods used to connect to rabbitmq server, minio server, postgres db

Authored by Jon Dong 8/11/2021
"""
import psycopg2
import os
import pika




def connect_to_postgres():
    """ Connect to Postgres Server

    Connects to postgres db wth a hostname, db name, user and password. Returns connection and cursor
    """
    #connect to the postgres db
    con = psycopg2.connect(host=os.getenv("DBHOST"),
                           database=os.getenv("DBNAME"),
                           user=os.getenv("DBUSER"),
                           password=os.getenv("DBPASSWORD")
                           )
    #cursor
    cur = con.cursor()
    return con, cur

def connect_to_rabbitmq():
    """ Connect to RabbitMQ Server

    Connects to rabbitmq server given username, password,
    hostname of server, and port number. Returns credentials, connection and channel
    """
    credentials = pika.PlainCredentials(os.getenv("RABBITUSERNAME"), os.getenv("RABBITPASSWORD"))
    # establishes connections
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            os.getenv("RABBITHOSTNAME"),
            os.getenv("RABBITPORTNUM"),
            '/',
            credentials)
    )
    channel = connection.channel()

    return  connection, channel
