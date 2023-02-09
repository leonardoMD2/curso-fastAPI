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

Session = sessionmaker(bind=engine)

Base = declarative_base()