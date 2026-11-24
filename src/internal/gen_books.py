import httpx2 

fields= ["author_name", "first_publish_year", "title", "language", "key"]
url_base = "https://openlibrary.org/search.json?"

def get_books(author : str, language : str, limit : int) -> dict:
    params = {"q": author, "language": language, "fields": ",".join(fields), "limit": limit}
    
    try: 
        author_info_request = httpx2.get(url_base, params=params)
        author_info_response = author_info_request.json()["docs"]
        return author_info_response
      
    except KeyError as e:
        return {"Error": e}
    except httpx2.HTTPStatusError as e:
        return {"Error": e}

    return {"Error": "Unexpected"} #THIS IS TEMPORARY IDK WHAT TO PUT ON THIS 
