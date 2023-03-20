from database import Database
from save_json import writeAJson

db = Database(database="dex", collection="pokemons")
db.reset_database()
pokemons = db.collection.find()

def getPokemonByDex(number: int):
    return db.collection.find({"id": number})

pokemon = db.collection.find({"type": "Fire", "base.Defense": { "$lte": 50 }})
writeAJson(pokemon, "pokemon_fire")

pokemon = db.collection.find({"type": "Water", "base.Attack": { "$lte": 60 }})
writeAJson(pokemon, "pokemon_water")

pokemon = db.collection.find({"type": "Bug", "base.Attack": { "$lte": 70 }})
writeAJson(pokemon, "pokemon_bug")

pokemon = db.collection.find({"type": "Bug", "base.Attack": { "$lte": 30 }, "base.Defense": { "$lte": 30}})
writeAJson(pokemon, "pokemon_bug_weak")

pokemon = db.collection.find({"type": "Flying", "base.Attack": { "$lte": 30 }, "base.Defense": { "$lte": 30}})
writeAJson(pokemon, "pokemon_flying_weak")
