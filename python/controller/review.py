import request.request as req

def add_review(data):
    print(data, flush=True)

    if (not "author_lastname" in data or data["author_lastname"] == ""):
        return False
    if (not "author_firstname" in data or data["author_firstname"] == ""):
        return False
    if (not "text" in data or data["text"] == ""):
        return False
    if (not "score" in data or data["score"] == None):
        return False

    if (data['score'] > 5 or data['score'] < 0):
        return False
  
    if ("review_id" in data and data["review_id"]):
        requete = f"UPDATE review SET author_lastname='{data['author_lastname']}', author_firstname='{data['author_firstname']}', text='{data['text']}', score='{data['score']}' WHERE review_id = {data['review_id']}"
        req.insert_in_db(requete)
        id = data['review_id']
    else:
        requete = "INSERT INTO review (author_lastname, author_firstname, text, score) VALUES (?, ?, ?, ?);"
        id = req.insert_in_db(requete, (data["author_lastname"], data["author_firstname"], data["text"],data["score"],))

    return id

def get_all_review():
    json = req.select_from_db("SELECT * FROM review")
    
    return json

def delete_review(id):
    if (not id):
        return False

    req.delete_from_db("DELETE FROM review WHERE review_id = ?", (id,))
    return True