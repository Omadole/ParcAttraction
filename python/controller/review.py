import request.request as req

def add_review(data):
  print(data, flush=True)

  if (not "author" in data or data["author"] == ""):
        return False
  
  if (not "description" in data or data["description"] == ""):
        return False
  
  if ("review_id" in data and data["review_id"]):
      requete = f"UPDATE review SET author='{data['author']}', description='{data['description']}' WHERE review_id = {data['review_id']}"
      req.insert_in_db(requete)
      id = data['review_id']
  else:
      requete = "INSERT INTO review (author, description) VALUES (?, ?);"
      id = req.insert_in_db(requete, (data["author"], data["description"]))

  return id



def get_all_review():
    json = req.select_from_db("SELECT * FROM review")
    
    return json


def delete_review(id):
    if (not id):
        return False

    req.delete_from_db("DELETE FROM review WHERE review_id = ?", (id,))

    return True