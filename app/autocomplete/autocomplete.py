import re
from collections import defaultdict, Counter
import pickle

def charger_et_nettoyer_corpus(filepath):
    import os
    # On construit le chemin absolu basé sur l'emplacement de ce fichier
    base_dir = os.path.dirname(os.path.abspath(__file__))
    abs_path = os.path.join(base_dir, '../malagasy_corpus.txt')
    abs_path = os.path.normpath(abs_path)
    with open(abs_path, 'r', encoding='utf-8') as f:
        texte = f.read().lower()
    # On ne garde que les lettres et les espaces (nettoyage des caractères spéciaux)
    # En malagasy, on garde les caractères comme 'ñ' si présents
    tokens = re.findall(r'\b\w+\b', texte)
    return tokens

def construire_modele_trigramme(tokens):
    # On crée un dictionnaire : {(mot1, mot2): {mot_suivant: compte}}
    model = defaultdict(Counter)
    
    for i in range(len(tokens) - 2):
        w1, w2, w3 = tokens[i], tokens[i+1], tokens[i+2]
        model[(w1, w2)][w3] += 1
        
    return model

def predire_prochain_mot(model, texte_entree, nb_suggestions=3):
    # Nettoyage de l'entrée utilisateur
    mots = re.findall(r'\b\w+\b', texte_entree.lower())
    
    if len(mots) < 2:
        return "Veuillez entrer au moins deux mots."
    
    # On récupère les deux derniers mots
    contexte = (mots[-2], mots[-1])
    
    if contexte in model:
        # On récupère les mots les plus fréquents après ce contexte
        suggestions = model[contexte].most_common(nb_suggestions)
        return [word for word, count in suggestions]
    else:
        return [] # Aucun mot trouvé dans le corpus pour ce contexte

# ... (vos fonctions charger_et_nettoyer_corpus et construire_modele_trigramme) ...

def sauvegarder_modele(model, filename):
    # On convertit le defaultdict en dict classique pour une meilleure compatibilité
    with open(filename, 'wb') as f:
        pickle.dump(dict(model), f)
    print(f"Modèle enregistré avec succès dans {filename}")

# --- EXECUTION UNIQUE ---
tokens = charger_et_nettoyer_corpus('../malagasy_corpus.txt')
mon_modele = construire_modele_trigramme(tokens)
sauvegarder_modele(mon_modele, 'malagasy_model.pkl')

# --- EXÉCUTION ---
# 1. Charger les données

# 2. Entraîner le modèle
