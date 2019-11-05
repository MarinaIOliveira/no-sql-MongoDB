import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client.albuns

albuns = db.artista.find({"nacionalidade" : "Inglaterra"})

for x in albuns:
    print (x)

#nome = albuns["nacionalidade"]
#print(albuns)
	