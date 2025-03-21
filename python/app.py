from flask import Flask, jsonify, request
from flask_cors import CORS

import request.request as req
import controller.auth.auth as user
import controller.attraction as attraction
import controller.review as review

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'


# Attraction
@app.post('/attraction')
def addAttraction():
    print("okok", flush=True)
    # Fonction vérif token
    checkToken = user.check_token(request)
    if (checkToken != True):
        return checkToken

    json = request.get_json()
    retour = attraction.add_attraction(json)
    if (retour):
        return jsonify({"message": "Element ajouté.", "result": retour}), 200
    return jsonify({"message": "Erreur lors de l'ajout.", "result": retour}), 500

@app.get('/attraction')
def getAllAttraction():
    
    # Fonction vérif token
    checkToken = user.check_token(request)
    if(checkToken != True):
      return checkToken
    
    result = attraction.get_all_attraction()
    return result, 200

@app.get('/attraction/visible')
def getVisibleAttraction():
    result = attraction.get_visible_attraction()
    return result, 200

@app.get('/attraction/<int:index>')
def getAttraction(index):
    # Fonction vérif token
    checkToken = user.check_token(request)
    if (checkToken != True):
        return checkToken

    result = attraction.get_attraction(index)
    return result, 200

@app.delete('/attraction/<int:index>')
def deleteAttraction(index):

    # Fonction vérif token
    checkToken = user.check_token(request)
    if (checkToken != True):
        return checkToken

    json = request.get_json()
    
    if (attraction.delete_attraction(index)):
        return "Element supprimé.", 200
    return jsonify({"message": "Erreur lors de la suppression."}), 500

@app.post('/attraction/associate_review')
def addReviewToAttraction():
    print("okok", flush=True)
    # Fonction vérif token
    checkToken = user.check_token(request)
    if (checkToken != True):
        return checkToken
    
    json = request.get_json()
    retour = attraction.associate(json)

    if (retour):
        return jsonify({"message": "Element ajouté.", "result": retour}), 200
    return jsonify({"message": "Erreur lors de l'ajout.", "result": retour}), 500

@app.get('/attraction/associate_review/<int:index>')
def getReviewAssociate(index):
    # Fonction vérif token
    checkToken = user.check_token(request)
    if (checkToken != True):
        return checkToken

    result = attraction.getReviewFromAttraction(index)
    return result, 200

@app.delete('/attraction/dissociate_review')
def deleteReviewToAttraction():
    print("okok", flush=True)
    # Fonction vérif token
    checkToken = user.check_token(request)
    if (checkToken != True):
        return checkToken
    
    json = request.get_json()
    retour = attraction.dissociate(json)

    if (retour):
        return jsonify({"message": "Element supprimé.", "result": retour}), 200
    return jsonify({"message": "Erreur lors de la suppression.", "result": retour}), 500




# Review
@app.post('/review')
def addReview():
    print("okok", flush=True)
    # Fonction vérif token
    checkToken = user.check_token(request)
    if (checkToken != True):
        return checkToken

    json = request.get_json()
    retour = review.add_review(json)
    if (retour):
        return jsonify({"message": "Element ajouté.", "result": retour}), 200
    return jsonify({"message": "Erreur lors de l'ajout.", "result": retour}), 500

@app.get('/review')
def getAllReview():
    
    # Fonction vérif token
    checkToken = user.check_token(request)
    if(checkToken != True):
      return checkToken
    
    result = review.get_all_review()
    return result, 200

@app.delete('/review/<int:index>')
def deleteReview(index):
    
    # Fonction vérif token
    checkToken = user.check_token(request)
    if(checkToken != True):
      return checkToken
    
    json = request.get_json()

    if (attraction.delete_attraction(index)):
        return "Element supprimé.", 200
    return jsonify({"message": "Erreur lors de la suppression."}), 500

@app.post('/login')
def login():
    json = request.get_json()

    if (not 'name' in json or not 'password' in json):
        result = jsonify({'messages': ["Nom ou/et mot de passe incorrect"]})
        return result, 400
    
    cur, conn = req.get_db_connection()
    requete = f"SELECT * FROM users WHERE name = '{json['name']}' AND password = '{json['password']}';"
    cur.execute(requete)
    records = cur.fetchall()
    conn.close()

    result = jsonify({"token": user.encode_auth_token(list(records[0])[0]), "name": json['name']})
    return result, 200