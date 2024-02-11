from flask import Flask, request, jsonify, render_template, redirect
import json

app = Flask(__name__)

def charger_donnees():
    try:
        with open('donnees.json', 'r', encoding='utf-8') as fichier:
            donnees = json.load(fichier)
    except FileNotFoundError:
        donnees = {'mots_phrases': [], 'questions': [], 'connaissances': [], 'derniere_question': None}
    return donnees

def enregistrer_donnees(donnees):
    with open('donnees.json', 'w', encoding='utf-8') as fichier:
        json.dump(donnees, fichier, ensure_ascii=False, indent=2)

@app.route('/', methods=['GET'])
def accueil():
    return render_template('index.html')

@app.route('/ajouter/mot_phrase', methods=['POST'])
def ajouter_mot_phrase_api():
    donnees = charger_donnees()
    nouvel_element = request.form['nouvel_element']
    if nouvel_element and nouvel_element not in donnees['mots_phrases']:
        donnees['mots_phrases'].append(nouvel_element)
        enregistrer_donnees(donnees)
    return redirect('/')

@app.route('/ajouter/question', methods=['POST'])
def ajouter_question_api():
    donnees = charger_donnees()
    question_texte = request.form['question']
    if question_texte and not any(q['question'] == question_texte for q in donnees['questions']):
        nouvelle_question = {'question': question_texte, 'reponse': None}
        donnees['questions'].append(nouvelle_question)
        enregistrer_donnees(donnees)
    return redirect('/')

@app.route('/ajouter/connaissance', methods=['POST'])
def ajouter_connaissance_api():
    donnees = charger_donnees()
    nouvelle_information = request.form['nouvelle_information']
    source = request.form['source']
    nouvelle_connaissance = {'information': nouvelle_information, 'source': source}
    if nouvelle_connaissance not in donnees['connaissances']:
        donnees['connaissances'].append(nouvelle_connaissance)
        enregistrer_donnees(donnees)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
