import request.request as req

def add_attraction(data):
    print(data, flush=True)
    if (not "nom" in data or data["nom"] == ""):
        return False
    
    if (not "description" in data or data["description"] == ""):
        return False

    if (not "difficulte" in data or data["difficulte"] is None):
        return False

    if (not "visible" in data):
        data["visible"] = True

    if ("attraction_id" in data and data["attraction_id"]):
      requete = f"UPDATE attraction SET nom='{data['nom']}', description='{data['description']}', difficulte={data['difficulte']}, visible={data['visible']} WHERE attraction_id = {data['attraction_id']}"
      req.insert_in_db(requete)
      id = data['attraction_id']
    else:
      requete = "INSERT INTO attraction (nom, description, difficulte, visible) VALUES (?, ?, ?, ?);"
      id = req.insert_in_db(requete, (data["nom"], data["description"], data["difficulte"], data["visible"]))

    return id

def get_all_attraction():
    json = req.select_from_db("SELECT * FROM attraction")
    
    return json

def get_visible_attraction():
    json = req.select_from_db("SELECT * FROM attraction WHERE visible=1")

    for i in range(0, len(json)):
        json[i]['reviews'] = req.select_from_db('SELECT r.* FROM review r INNER JOIN attraction_review ar  ON ar.review_id = r.review_id WHERE ar.attraction_id = ?', (json[i]['attraction_id'],))
       

    return json

def get_attraction(id):
    if (not id):
        return False

    json = req.select_from_db("SELECT * FROM attraction WHERE attraction_id = ?", (id,))

    if len(json) > 0:
        return json[0]
    else:
        return []

def delete_attraction(id):
    if (not id):
        return False

    req.delete_from_db("DELETE FROM attraction WHERE attraction_id = ?", (id,))

    return True

def associate(data):
    if("attraction_id" in data and data['attraction_id'] == None):
        return False
    if("review_id" in data and data['review_id'] == None):
        return False
    
    # Vérifiez si la critique est déjà associé 
    check_requete = "SELECT 1 FROM attraction_review WHERE review_id = ?;"
    result = req.select_from_db(check_requete, (data["review_id"],))
    if result:
        return False
    
    # Vérifiez si l'attraction existe
    check_requete_attraction = "SELECT 1 FROM attraction WHERE attraction_id = ?;"
    result_attraction = req.select_from_db(check_requete_attraction, (data["attraction_id"],))
    if result_attraction:
        return False
    
    # Vérifiez si la critique existe
    check_requete_review = "SELECT 1 FROM attraction WHERE review_id = ?;"
    result_review = req.select_from_db(check_requete_review, (data["review_id"],))
    if result_review:
        return False

    requete = "INSERT INTO attraction_review (attraction_id, review_id) VALUES (?, ?);"
    id = req.insert_in_db(requete, (data["attraction_id"], data["review_id"]))
    return True

def dissociate(data):
    if("attraction_id" in data and data['attraction_id'] == None):
        return False
    if("review_id" in data and data['review_id'] == None):
        return False
    
    # Vérifiez si la critique est déjà associé existe déjà
    check_requete = "SELECT 1 FROM attraction_review WHERE attraction_id = ? and review_id = ?;"
    result = req.select_from_db(check_requete, (data["attraction_id"], data["review_id"]))
    if not result:
        return False
    
    requete = "DELETE FROM attraction_review WHERE attraction_id = ? and review_id = ?"
    req.delete_from_db(requete, (data["attraction_id"], data["review_id"]))
    return True

def getReviewFromAttraction(id):
    if (not id):
        return False
    
    json = req.select_from_db("SELECT review.review_id, review.author_lastname, review.author_firstname, review.text, review.score FROM review INNER JOIN attraction_review ON review.review_id = attraction_review.review_id WHERE attraction_review.attraction_id = ?", (id,))

    if len(json) > 0:
        return json
    else:
        return []