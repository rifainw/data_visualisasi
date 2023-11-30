import psycopg2
import sshtunnel
from sshtunnel import SSHTunnelForwarder
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

with SSHTunnelForwarder(
    ('SSH_HOST', 'SSH_PORT'),
    ssh_username="USERNAME",
    ssh_password="PASSWORD",
        remote_bind_address=('host', 'port_db')) as server:

    # Connect to postgresql
    local_port = str(server.local_bind_port)
    engine = create_engine('postgresql://user:password@host:'+local_port+'/db_name')

    Session = sessionmaker(bind=engine)
    session = Session()

    session.close()

server.start()

def connect():
    return psycopg2.connect(host="host", port=server.local_bind_port,user="user", password="password", database="db_name")