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


def ajouter_question(question_reponse):
    donnees = charger_donnees()
    if question_reponse not in donnees['questions']:
        donnees['questions'].append(question_reponse)
        enregistrer_donnees(donnees)
    else:
        print("Cette question existe déjà dans la liste.")


def ajouter_connaissance(nouvelle_information, source):
    donnees = charger_donnees()
    nouvelle_connaissance = {'information': nouvelle_information, 'source': source}
    if nouvelle_connaissance not in donnees['connaissances']:
        donnees['connaissances'].append(nouvelle_connaissance)
        enregistrer_donnees(donnees)
    else:
        print("Cette connaissance existe déjà dans la liste.")


def gestion_conversation(reponse_utilisateur):
    donnees = charger_donnees()

    # Exemple : si l'IA veut dire bonjour
    if not donnees['mots_phrases']:
        print("Bonjour! Comment ça va?")
        donnees['mots_phrases'].append("Bonjour, comment ça va?")
        enregistrer_donnees(donnees)
        return

    # Si l'utilisateur fournit une nouvelle information
    if "apprendre" in reponse_utilisateur.lower():
        nouvelle_information = input("Quelle est la nouvelle information? ")
        source = input("Quelle est la source de cette information? ")
        ajouter_connaissance(nouvelle_information, source)
        print("Merci pour la nouvelle information!")

    # Si la liste des questions n'est pas vide
    elif donnees['questions']:
        question = random.choice(donnees['questions'])
        print(question['question'])

    # Enregistrer les données mises à jour
    enregistrer_donnees(donnees)

# Exemple d'utilisation dans une boucle
while True:
    reponse_utilisateur = input("Votre réponse (pour quitter, tapez 'exit', 'ciao' ou 'au revoir') : ")

    if reponse_utilisateur.lower() in ['exit', 'ciao', 'au revoir']:
        break  # Sortir de la boucle infinie si l'utilisateur le demande

    gestion_conversation(reponse_utilisateur)
