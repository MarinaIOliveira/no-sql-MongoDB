import pymongo
import json

client = pymongo.MongoClient("localhost", 27017)
db = client.albuns

#Albuns
album1 = '{"nome" : "The Dark Side Of The Moon", "dataLancamento" : "1992-05-30", "duracao" : "3328", "artista" : {"nome" : "Pink Floyd"}}'
album2 = '{"nome" : "Master of Puppets", "dataLancamento" : "1985-05-30", "duracao" : "3328", "artista" : {"nome" : "Metallica"}}'
album3 = '{"nome" : "Nevermind", "dataLancamento" : "1992-05-30", "duracao" : "3328", "artista" : {"nome" : "Nirvana"}}'
album4 = '{"nome" : "Seventh Son of a Seventh Son", "dataLancamento" : "1992-05-30", "duracao" : "3328", "artista" : {"nome" : "Iron Maiden"}}'
album5 = '{"nome" : "Yellow Submarine", "dataLancamento" : "1992-05-30", "duracao" : "3328", "artista" : {"nome" : "The Beatles"}}'

albuns1 = json.loads(album1)
albuns2 = json.loads(album2)
albuns3 = json.loads(album3)
albuns4 = json.loads(album4)
albuns5 = json.loads(album5)

db.albuns.insert(albuns1)
db.albuns.insert(albuns2)
db.albuns.insert(albuns3)
db.albuns.insert(albuns4)
db.albuns.insert(albuns5)

#Artistas

artista1 = '{"nome" : "Pink Floyd", "dataNascimento" : "1962-05-30","nacionalidade" : "Inglaterra"}'
artista2 = '{"nome" : "Metallica", "dataNascimento" : "1950-01-01","nacionalidade" : "EUA"}'
artista3 = '{"nome" : "Nirvana", "dataNascimento" : "1962-01-01","nacionalidade" : "EUA"}'
artista4 = '{"nome" : "Iron Maiden", "dataNascimento" : "1970-01-01","nacionalidade" : "Inglaterra"}'
artista5 = '{"nome" : "The Beatles", "dataNascimento" : "1950-01-01","nacionalidade" : "Inglaterra"}'

artistas1 = json.loads(artista1)
artistas2 = json.loads(artista2)
artistas3 = json.loads(artista3)
artistas4 = json.loads(artista4)
artistas5 = json.loads(artista5)

db.artista.insert(artistas1)
db.artista.insert(artistas2)
db.artista.insert(artistas3)
db.artista.insert(artistas4)
db.artista.insert(artistas5)
