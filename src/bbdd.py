from sqlalchemy import create_engine


postgres_url = f'postgresql+psycopg2://postgres:123@localhost:5432'
engine = create_engine(f"{postgres_url}/ProPinPos")
connection = engine.connect()

def leer(consultar):
    consulta = list(connection.execute(consultar))
    return consulta

#Métodos a Implementar

#def crear(consultar):
#   consulta = list(connection.execute(consultar))
#    return consulta

#def actualizar(consultar):
#    consulta = list(connection.execute(consultar))
#    return consulta

#def borrar(consultar):
#    consulta = list(connection.execute(consultar))
#    return consulta
