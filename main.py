from fastapi import FastAPI,HTTPException
from typing import List
from database import SessionLocal
from schemas import Gameschemas
import modelz 
from fastapi.encoders import jsonable_encoder

app = FastAPI()

db=SessionLocal()

@app.get('/')
def Welcome():
    return('Welcome to the Game Catalog System')


@app.get('/games',response_model=List[Gameschemas],status_code=200)
def get_all_games_in_catalog():
    games= db.query(modelz.Games).order_by(modelz.Games.id).all()

    return jsonable_encoder(games)

@app.post('/games',response_model=Gameschemas)
def catalog_a_game(games:Gameschemas):
    db_game_registration= db.query(modelz.Games).filter(modelz.Games.id==games.id).first()
     
    if db_game_registration is not None:
        raise HTTPException(status_code=409,detail= 'A game previously created with this id')
    
    new_game=modelz.Games(
        id= games.id,
        name= games.name,
        multiplatform= games.multiplatform,
        price= games.price,
        for_sale= games.for_sale
    )

    
    db.add(new_game)
    db.commit()
    raise HTTPException(status_code=201,detail= 'Game successfully cataloged!')

@app.put('/games/{games_id}', response_model=Gameschemas)
def game_to_be_updated(games_id: int, games: Gameschemas):
    update_game = db.query(modelz.Games).filter(modelz.Games.id==games_id).first()
  
    if update_game is None: 
        raise HTTPException(status_code=400,detail= 'game does not exist in the catalog')
    
    if games.name:
        update_game.name= games.name
    
    try:
        if games.multiplatform:
            update_game.multiplatform= games.multiplatform
    except:
        pass
    try:
        if games.price:
            update_game.price= games.price
    except:
        pass
    try:
        if games.for_sale:
            update_game.for_sale= games.for_sale
    except:
        pass

    db.commit()  
    raise HTTPException(status_code=200,detail= 'Game successfully modified in catalog!')

@app.delete('/game/{game_id}')
def delete_game(game_id: int):
    delete_game = db.query(modelz.Games).filter(modelz.Games.id==game_id).first()

    if delete_game is None:
        raise HTTPException(status_code=400,detail= 'No game in the catalog')
    
    db.delete(delete_game)
    db.commit()

    raise HTTPException(status_code=200,detail= 'Game successfully deleted!')

