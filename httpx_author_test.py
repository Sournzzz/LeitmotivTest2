import httpx2

fields= ["author_name", "first_publish_year", "title", 
         #"language"
         "key"
         ]

authors = [
    {"name": "Bertrand Russell", "language": "eng"},
    #{"name": "John Locke", "language": "eng"},
    #{"name": "Martin Heidegger", "language": "ger"},
]

url_base = "https://openlibrary.org/search.json?"


titles = []
keys = []

book_count = 0

for x, author in enumerate(authors, start=1):
    print(f"{x}\n==={author['name']}===\n")

    name = author["name"]
    language = author["language"]
    params = {"q": name, "language": language, "fields": ",".join(fields), "limit": 5}
    
    try: 

        author_info_request = httpx2.get(url_base, params=params)
        author_info_docs = author_info_request.json()["docs"] #List of dicts containing all the information about the books found
        print(type(author_info_docs))

        for info in author_info_docs:
            
            keys.append(info["key"])

            """
            titles.append(info["title"]) 
            
            if name in info["author_name"]:
                
                print(info)
                book_count += 1
            """ 

    except KeyError as e:
        print(f"Error: {e}, Info: \n{info}")
        
    except httpx2.HTTPStatusError as e:
        print(e) 

"""
print(book_count)

titles = sorted(titles)
for title in titles:
    print(title)


keys = sorted(keys)
equal_key = 0
current_key = ""

for key in keys: 
    if current_key == key: 
        equal_key += 1
    current_key = key

print(equal_key)
""" 