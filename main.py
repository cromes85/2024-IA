import json
import random

# Charger les données existantes depuis le fichier JSON
def charger_donnees():
    try:
        with open('donnees.json', 'r') as fichier:
            donnees = json.load(fichier)
    except FileNotFoundError:
        donnees = {'mots_phrases': [], 'questions': [], 'connaissances': [], 'derniere_question': None}
    return donnees

# Enregistrer les données dans le fichier JSON
def enregistrer_donnees(donnees):
    try:
        chemin_absolu = 'donnees.json'
        print("Avant l'enregistrement : ", donnees)
        with open(chemin_absolu, 'w') as fichier:
            json.dump(donnees, fichier, indent=2)
        print("Après l'enregistrement : ", donnees)
        print("Données enregistrées avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'enregistrement des données : {e}")

# Fonction pour ajouter un mot ou une phrase appris
def ajouter_mot_phrase(nouvel_element):
    donnees = charger_donnees()
    donnees['mots_phrases'].append(nouvel_element)
    enregistrer_donnees(donnees)

# Fonction pour ajouter une question apprise
def ajouter_question(question_reponse):
    donnees = charger_donnees()
    donnees['questions'].append(question_reponse)
    enregistrer_donnees(donnees)

# Fonction pour ajouter une nouvelle connaissance
def ajouter_connaissance(nouvelle_information, source):
    donnees = charger_donnees()
    nouvelle_connaissance = {'information': nouvelle_information, 'source': source}
    donnees['connaissances'].append(nouvelle_connaissance)
    enregistrer_donnees(donnees)

# Fonction pour gérer la conversation
def gestion_conversation(reponse_utilisateur):
    donnees = charger_donnees()

    # Si la clé 'derniere_question' existe
    if 'derniere_question' in donnees and donnees['derniere_question'] is not None:
        ajouter_question({'question': donnees['derniere_question'], 'reponse': reponse_utilisateur})
        donnees['derniere_question'] = None

    # Si l'utilisateur fournit une nouvelle information
    elif "apprendre" in reponse_utilisateur.lower():
        nouvelle_information = input("Quelle est la nouvelle information? ")
        source = input("Quelle est la source de cette information? ")
        ajouter_connaissance(nouvelle_information, source)
        print("Merci pour la nouvelle information!")

    # Si la liste des questions n'est pas vide
    elif donnees['questions']:
        question = random.choice(donnees['questions'])
        donnees['derniere_question'] = question['question']  # Mettre à jour la dernière question
        print(question['question'])

    # Exemple : si l'IA veut dire bonjour
    else:
        print("Bonjour! Comment ça va?")

    # Enregistrer les données mises à jour
    enregistrer_donnees(donnees)

# Boucle principale
while True:
    reponse_utilisateur = input("Votre réponse (pour quitter, tapez 'exit', 'ciao' ou 'au revoir') : ")
    
    if reponse_utilisateur.lower() in ['exit', 'ciao', 'au revoir']:
        break  # Sortir de la boucle infinie si l'utilisateur le demande
    
    gestion_conversation(reponse_utilisateur)
