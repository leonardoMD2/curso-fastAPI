#Modelo de tabla HERO

#importamos la base para crear 
from config.database import Base
from sqlalchemy import Column,String,Integer

#creación de tabla basandonos en la clase que hereda la Base. Con esto le indicamos que es una entidad de la BD
class HerosClass(Base):
    __tablename__ = 'heros'

    id = Column(Integer, primary_key = True)
    name= Column(String)
    localized_name= Column(String)
    primary_attr= Column(String)
    attack_type = Column(String)
    roles = Column(String)
    legs = Column(Integer)
