from models import Authors, Quotes
import connect_to_mongo

import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)

#function of searching data in the database by a set of tags
def search_quotes(query):
    if query.startswith("tags:"):
        tags = query[5:].split(',')
        quotes = Quotes.objects(tags__in=tags)
        return quotes

    elif query == "exit":
        return "exit"

    else:
        return "Invalid command."

#function of searching data in the database by the name of the author and the name of the tag, plus the result is cached using Redis
@cache
def search_quotes_cache(query):
    if query.startswith("name:"):
        author_name = query[5:]
        author = Authors.objects(fullname__iregex=f"^{author_name}").first()
        if author:
            quotes = Quotes.objects(author=author.id)
            return quotes
        else:
            return "Author not found."

    elif query.startswith("tag:"):
        tag = query[4:]
        quotes = Quotes.objects(tags__iregex=f"^{tag}")
        return quotes


if __name__ == '__main__':
    while True:
        user_input = input("Enter command: ")
        if user_input.startswith("name:") or user_input.startswith("tag:"):
            result = search_quotes_cache(user_input)
            if isinstance(result, str):
                print(result)
            else:
                for quote in result:
                    print(f"Author: {quote.author.fullname}")
                    print(f"Quote: {quote.quote}")
                    print("-" * 40)
                    
        else:
            result = search_quotes(user_input)
            if result == "exit":
                print("Script finished")
                break
            elif isinstance(result, str):
                print(result)
            else:
                for quote in result:
                    print(f"Author: {quote.author.fullname}")
                    print(f"Quote: {quote.quote}")
                    print("-" * 40)
                    