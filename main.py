from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from heros import herosList
from esquemas import Hero

web = FastAPI()

css = "{color:lightblue; text-align:center; padding-top:25px}"

#-------------------metodos get-----------------
@web.get('/heros/', tags=['List Heros'])
def getHeros():
    lista = []
    for hero in herosList:
        lista.append(hero['localized_name'])
    return lista

@web.get('/heros/{id}', tags=['ListHeros'])
def getHero(id: int):
    lista = list(filter(lambda hero : hero['id'] == id, herosList))
    return HTMLResponse(f"<style> h1 {css} </style> <h1> {lista[0]['localized_name']} </h1>")

@web.get('/heros/attr/', tags=['List heros by category'])
def getHeroByCat(cat: str):
        lista = list(filter(lambda hero : hero['primary_attr']==cat, herosList))
        listHeros = []
        for hero in lista:
            listHeros.append(hero['localized_name'])
        return listHeros

@web.get('/heros/legs/', tags=['List heros by category'])
def getHeroByLegs(legs: int):
    lista = list(filter(lambda hero : hero['legs'] == legs, herosList))
    listHeros = []
    for hero in lista:
        listHeros.append(hero['localized_name'])
    return listHeros

#-------------------metodos POST-----------------
#Inserciones en los datos.

@web.post('/heros', tags=['Inserción heros'])
def insertHero(hero: Hero): #la función recibirá a un hero que será de tipo Hero (referencia a la clase importada)
    if hero.id > 137 and len(hero.localized_name) > 0:
        #hacemos la inserción de los datos agregando un nuevo valor a la lista.
        herosList.append(hero)
        #La inserción se hace tomando la clase modelo en la que colocamos el esquema
        return herosList
    else:
        #Devolvemos mensaje a la documentación avisando de que alguna de las verificaciones no pasaron
        return JSONResponse(content={'Error': 'Alguno de los campos id o localized_name están vacíos'}, status_code=404)
    
#-------------------metodos PUT-----------------
#Modificación en los datos.

@web.put('/heros', tags=['Modificación heros'])
#La función putHero recibirá el esquema heredado de la clase Hero en la cual se declaró el basemodel de los datos
def putHero(heros: Hero):
    #Primero filtramos la info recibiendo el dato id del body de la documentación. Este dato se guarda en la instancia de la clase hero
    listHero = list(filter(lambda hero : hero['id'] == heros.id, herosList)) 
    #guardamos el dato para manejarlo mejor en otra variable
    hero = listHero[0]
    #reemplazamos los datos de la base filtrada por los obtenidos de la modificación del body en docs
    hero['name'] = heros.name
    hero['localized_name'] = heros.localized_name
    hero['primary_attr'] = heros.primary_attr
    hero['attack_type'] = heros.attack_type
    hero['roles'] = heros.roles
    hero['legs'] = heros.legs
    #guardamos y retornamos
    herosList.append(hero)
    return JSONResponse(content=herosList)