import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#directorios de creación de la BD
sqlite_file_name = '../database.sqlite'
#obtenemos la dirección
base_dir = os.path.dirname(os.path.realpath(__file__))

#Unificamos el nombre con el directorio
database_url = f'sqlite:///{os.path.join(base_dir,sqlite_file_name)}'

#El primer paso es crear un "motor" de SQLAlchemy
engine = create_engine(database_url, echo=True)

#Cada instancia de la Session será una sesión de base de datos. La clase en sí aún no es una sesión de base de datos.Pero una vez que creamos una instancia de la Session, esta instancia será la sesión real de la base de datos.
Session = sessionmaker(bind=engine)

#Ahora usaremos la función declarative_base()que devuelve una clase.
#Posteriormente heredaremos de esta clase para crear cada uno de los modelos o clases de base de datos (los modelos ORM):
Base = declarative_base()