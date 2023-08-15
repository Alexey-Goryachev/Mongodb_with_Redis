from models import Authors, Quotes
import connect_to_mongo
import json

file_authors = 'authors.json'
file_quotes = 'quotes.json'

#loading data from a file into the Authors collection
with open(file_authors, 'r', encoding='utf-8') as fa:
    unpackeds = json.load(fa)
    for unpack in unpackeds:
        author = Authors(fullname=unpack.get("fullname"), born_date=unpack.get("born_date"), born_location=unpack.get("born_location"),
                         description=unpack.get("description")).save()

#loading data from a file into the Quotes collection
with open(file_quotes, 'r', encoding='utf-8') as fq:
    unpackeds = json.load(fq)
    for unpack in unpackeds:
        author_name = unpack.get("author")
        author = Authors.objects(fullname=author_name).first()
        quote = Quotes(tags=unpack.get("tags"), author=author, quote=unpack.get("quote")).save()




 