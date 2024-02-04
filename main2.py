import json
import random

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

def ajouter_mot_phrase(nouvel_element):
    donnees = charger_donnees()
    if nouvel_element not in donnees['mots_phrases']:
        donnees['mots_phrases'].append(nouvel_element)
        enregistrer_donnees(donnees)

def ajouter_question(question_texte):
    donnees = charger_donnees()
    
    # Vérifier si la question n'existe pas déjà
    if not any(q['question'] == question_texte for q in donnees['questions']):
        nouvelle_question = {'question': question_texte, 'reponse': None}
        donnees['questions'].append(nouvelle_question)
        enregistrer_donnees(donnees)
    else:
        print("Cette question existe déjà dans la liste.")

def ajouter_connaissance(nouvelle_information, source):
    donnees = charger_donnees()
    nouvelle_connaissance = {'information': nouvelle_information, 'source': source}
    
    # Vérifier si la connaissance n'existe pas déjà
    if nouvelle_connaissance not in donnees['connaissances']:
        donnees['connaissances'].append(nouvelle_connaissance)
        enregistrer_donnees(donnees)
    else:
        print("Cette connaissance existe déjà dans la liste.")

# Fonction pour gérer la conversation
def gestion_conversation(reponse_utilisateur):
    donnees = charger_donnees()

    if "apprendre" in reponse_utilisateur.lower():
        nouvelle_information = input("Quelle est la nouvelle information? ")
        source = input("Quelle est la source de cette information? ")
        ajouter_connaissance(nouvelle_information, source)
        print("Merci pour la nouvelle information!")

    elif donnees['questions']:
        questions_possibles = [q for q in donnees['questions'] if q['question'] != donnees['derniere_question']]
        if questions_possibles:
            question = random.choice(questions_possibles)
            print(question['question'])
            donnees['derniere_question'] = question['question']  # Mettre à jour la dernière question
        else:
            print("Toutes les questions ont été posées. Ajoutez de nouvelles questions!")

    enregistrer_donnees(donnees)  # Mettre à jour les données même si toutes les questions ont été posées

# Fonction pour que vous posiez vos questions
def poser_question_utilisateur():
    question_utilisateur = input("Posez-moi une question : ")
    ajouter_question(question_utilisateur)

# Exemple d'utilisation dans une boucle
while True:
    reponse_utilisateur = input("Votre réponse (pour quitter, tapez 'exit', 'ciao' ou 'au revoir') : ")

    if reponse_utilisateur.lower() in ['exit', 'ciao', 'au revoir']:
        break

    gestion_conversation(reponse_utilisateur)
    poser_question_utilisateur()

# Afficher les données après les ajouts
print(charger_donnees())
