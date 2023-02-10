from pydantic import BaseModel
from typing import Optional

#creamos el esquema modelo por el cual ingresaremos info a la bd de heros.

class Hero(BaseModel):
    
    id: Optional[int] #Agregando el opcional en la id permite que el engine de la bd coloque de forma autoincremental y automática las id
    name: Optional[str]
    localized_name: str
    primary_attr: str
    attack_type: str
    roles: str
    legs: int