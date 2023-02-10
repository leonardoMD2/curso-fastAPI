from fastapi import FastAPI, Path
from fastapi.responses import HTMLResponse, JSONResponse
from heros import herosList
from esquemas import Hero
from config.database import Session, engine, Base
from models.hero import HerosClass as HeroModel
from fastapi.encoders import jsonable_encoder #para convertir el objeto que devuelve la consulta a json

web = FastAPI()

css = "{color:lightblue; text-align:center; padding-top:25px}"

Base.metadata.create_all(bind=engine)

#-------------------metodos get-----------------
@web.get('/heros/', tags=['List Heros'])
def getHeros():
    db = Session()
    consulta = db.query(HeroModel).all() #la variable consulta devuelve un objeto de la clase modelo, no un iterable
    return JSONResponse(status_code=200, content=jsonable_encoder(consulta))

@web.get('/heros/{id}', tags=['heros'], response_model=Hero)
def getHero(id: int = Path(ge=1, le=200)) -> Hero:
    db = Session()
    #Hacemos la query por id solicitando a la bd (HeroModel) que filtre si el id del modelo es igual al parámetro; que de eso me devuelva el primer registro
    consulta = db.query(HeroModel).filter(HeroModel.id == id).first()
    if not consulta:
        return JSONResponse(status_code=404, content={'Mensaje':'No se encontró coincidencia'})
    return JSONResponse(status_code=200, content=jsonable_encoder(consulta))


@web.get('/heros/attr/', tags=['List heros by category'])
def getHeroByCat(cat: str):
        db = Session()
        consulta = db.query(HeroModel).filter(HeroModel.primary_attr == cat).all()
        return JSONResponse(content=jsonable_encoder(consulta))

@web.get('/heros/legs/', tags=['List heros by category'])
def getHeroByLegs(legs: int):
    db = Session()
    consulta = db.query(HeroModel).filter(HeroModel.legs == legs).all()
    return JSONResponse(content=jsonable_encoder(consulta))

#-------------------metodos POST-----------------
#Inserciones en los datos.

@web.post('/heros', tags=['Inserción heros'], response_model=dict)
def insertHero(hero: Hero): #la función recibirá a un hero que será de tipo Hero (referencia a la clase importada)
    db = Session() #creamos la sesión para trabajar la db
    
    newHero = HeroModel(**hero.dict()) #Guardamos como variable el modelo de la bd que recibe TODOS (**) los parametros requeridos por la clase convirtiendolos a un diccionario
    db.add(newHero) #agregamos el nuevo hero
    db.commit() #actualizamos la db para guardar el registro nuevo
        #La inserción se hace tomando la clase modelo en la que colocamos el esquema
    return JSONResponse(status_code=201, content={'mensaje': 'Se agregó el heroe correctamente'})
   
    
#-------------------metodos PUT-----------------
#Modificación en los datos.

@web.put('/heros', tags=['Modificación heros'])
#La función putHero recibirá el esquema heredado de la clase Hero en la cual se declaró el basemodel de los datos
def putHero(heros: Hero):
    
    db = Session()
    consulta = db.query(HeroModel).filter(HeroModel.id == heros.id).first()
    consulta.name = heros.name
    consulta.localized_name = heros.localized_name
    consulta.primary_attr = heros.primary_attr
    consulta.attack_type = heros.attack_type
    consulta.roles = heros.roles
    consulta.legs = heros.legs
    #guardamos y retornamos
    resultado = db.query(HeroModel).all()
    db.commit()
    return JSONResponse(status_code= 200,content={"mensaje":"Se modificó correctamente el heroe"})