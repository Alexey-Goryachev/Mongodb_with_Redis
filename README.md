# Mongodb_with_Redis
In this project, an Atlas MongoDB cloud database is created. 

Using ODM Mongoengine, models are created to store data in collections from files authors.json, quotes.json.

The search.py ​​file implements a script for searching quotes by tag, by author's name, or by a set of tags 
with the ability to shorten the values ​​for searching by name and tag. 

Also caching the result of executing the name: and tag: commands using Redis
