import streamlit as st
import unicodedata
import re

# --- 1. FONCTION INTELLIGENTE ---
def signature_prenom(texte):
    if not texte: return ""
    texte = texte.lower().strip()
    texte = unicodedata.normalize('NFD', texte)
    texte = ''.join(c for c in texte if unicodedata.category(c) != 'Mn')
    texte = texte.replace("ph", "f").replace("y", "i").replace("h", "")
    texte = re.sub(r'(.)\1+', r'\1', texte)
    return texte

# --- 2. DONNÉES COMPLÈTES (2015-2024) ---
base_donnees = {
    2024: ["Gabriel", "Raphaël", "Léo", "Noah", "Louise", "Arthur", "Jade", "Adam", "Jules", "Maël", "Ambre", "Eden", "Alba", "Léon", "Liam", "Isaac", "Emma", "Sacha", "Alma", "Marceau", "Elio", "Romy", "Alice", "Noé", "Lucas", "Anna", "Mia", "Lou", "Gabin", "Inaya", "Mohamed", "Aaron", "Adèle", "Lina", "Eva", "Ayden", "Iris", "Imrân", "Agathe", "Malo", "Elena", "Paul", "Ethan", "Giulia", "Léna", "Noûr", "Hugo", "Naël", "Jeanne", "Olivia", "Ibrahim", "Marius", "Luna", "Victoire", "Léonie", "Eliott", "Nathan", "Victor", "Zoé", "Chloé", "Théo", "Martin", "Nina", "Sofia", "Léa", "Tom", "Ezio", "Gaspard", "Mathis", "Ismaël", "Alya", "Côme", "Léandre", "Charlotte", "Romane", "Victoria", "Amir", "Augustin", "Lyam", "Nino", "Aylan", "Antoine", "Inès", "Esmée", "Robin", "Ava", "Kaïs", "Valentin", "Zayn", "Andréa", "Basile", "Timéo", "Lucie", "Simon", "Lola", "Rayan", "Axel", "Sohan", "Lya", "Charlie"],
    2023: ["Gabriel", "Léo", "Raphaël", "Maël", "Louise", "Noah", "Alba", "Jules", "Adam", "Arthur", "Jade", "Isaac", "Liam", "Sacha", "Rose", "Eva", "Alma", "Lucas", "Léon", "Naël", "Alice", "Gabin", "Romy", "Mia", "Mohamed", "Anna", "Lina", "Elio", "Hugo", "Noé", "Ethan", "Marceau", "Aaron", "Paul", "Léna", "Ayden", "Inaya", "Julia", "Agathe", "Lou", "Iris", "Elena", "Imrân", "Nathan", "Adèle", "Giulia", "Théo", "Victoire", "Marius", "Léa", "Ibrahim", "Chloé", "Olivia", "Malo", "Noûr", "Luna", "Juliette", "Jeanne", "Nina", "Eliott", "Nino", "Mathis", "Victor", "Léonie", "Martin", "Lyam", "Gaspard", "Sofia", "Victoria", "Romane", "Lola", "Timéo", "Milo", "Augustin", "Robin", "Valentin", "Léandre", "Axel", "Lya", "Ava", "Alya", "Kaïs", "Antoine", "Tiago", "Nolan", "Côme", "Sohan", "Lucie", "Rayan", "Amir", "Charlotte", "Enzo", "Maé", "Mila", "Soan", "Alessio", "Yanis", "Margaux", "Albane", "Samuel"],
    2022: ["Gabriel", "Léo", "Raphaël", "Maël", "Louis", "Louise", "Jade", "Ambre", "Noah", "Jules", "Arthur", "Adam", "Emma", "Eden", "Lucas", "Liam", "Rose", "Naël", "Sacha", "Isaac", "Gabin", "Alice", "Léna", "Hugo", "Romy", "Anna", "Lina", "Aaron", "Mia", "Léon", "Mohamed", "Noé", "Paul", "Lou", "Ethan", "Julia", "Chloé", "Elena", "Elio", "Alma", "Marceau", "Agathe", "Théo", "Iris", "Nathan", "Inaya", "Léa", "Tom", "Nino", "Eva", "Luna", "Juliette", "Victoire", "Imrân", "Marius", "Adèle", "Giulia", "Ayden", "Malo", "Nina", "Inès", "Zoé", "Gaspard", "Martin", "Lyam", "Olivia", "Victor", "Léonie", "Noûr", "Rayan", "Timéo", "Eliott", "Victoria", "Milo", "Robin", "Tiago", "Valentin", "Ibrahim", "Axel", "Augustin", "Amir", "Emy", "Ismaël", "Enzo", "Lucie", "Sohan", "Lyana", "Nolan", "Mattéo", "Samuel", "Lola", "Mathéo", "Simon", "Antoine", "Mila", "Alessio", "Charlotte", "Sofia", "Louna", "Kaïs"],
    2021: ["Léo", "Raphaël", "Jade", "Louise", "Louis", "Maël", "Arthur", "Jules", "Noah", "Emma", "Adam", "Lucas", "Ambre", "Hugo", "Alice", "Gabin", "Liam", "Rose", "Sacha", "Mia", "Eden", "Anna", "Alba", "Aaron", "Romy", "Léon", "Lina", "Léna", "Isaac", "Noé", "Paul", "Nathan", "Naël", "Chloé", "Julia", "Lou", "Ethan", "Mohamed", "Léa", "Inès", "Iris", "Elena", "Tom", "Théo", "Malo", "Zoé", "Nina", "Inaya", "Juliette", "Nino", "Marceau", "Mathis", "Victor", "Ayden", "Léonie", "Luna", "Jeanne", "Milo", "Martin", "Mila", "Adèle", "Robin", "Victoire", "Imrân", "Elio", "Timéo", "Olivia", "Eliott", "Axel", "Lola", "Lyam", "Victoria", "Lucie", "Margaux", "Giulia", "Romane", "Antoine", "Nolan", "Augustin", "Sofia", "Gaspard", "Valentin", "Noûr", "Charlotte", "Emy", "Amir", "Samuel", "Côme", "Ismaël", "Ibrahim", "Rayan", "Lyana", "Margot", "Sarah", "Louna", "Sohan", "Mathéo", "Mya", "Kaïs", "Manon"],
    2020: ["Léo", "Gabriel", "Raphaël", "Louise", "Jade", "Arthur", "Jules", "Emma", "Lucas", "Noah", "Liam", "Ambre", "Lina", "Gabin", "Rose", "Chloé", "Mia", "Sacha", "Eden", "Léa", "Inès", "Paul", "Nathan", "Anna", "Mila", "Aaron", "Mohamed", "Julia", "Léon", "Tom", "Romy", "Léna", "Noé", "Lou", "Naël", "Théo", "Tiago", "Elena", "Isaac", "Agathe", "Eva", "Juliette", "Inaya", "Marius", "Zoé", "Nina", "Victor", "Martin", "Léonie", "Mathis", "Jeanne", "Timéo", "Axel", "Lola", "Robin", "Enzo", "Eliott", "Adèle", "Marceau", "Luna", "Nino", "Valentin", "Romane", "Nolan", "Malo", "Lucie", "Milo", "Margaux", "Antoine", "Olivia", "Samuel", "Imrân", "Victoria", "Louna", "Augustin", "Amir", "Mya", "Lyam", "Sofia", "Yanis", "Ibrahim", "Charlotte", "Sarah", "Noûr", "Gaspard", "Giulia", "Lya", "Ismaël", "Margot", "Sohan", "Clément", "Evan", "Kaïs", "Baptiste", "Maxence", "Lyana", "Côme", "Soan", "Emy", "Elise"],
    2019: ["Léo", "Raphaël", "Arthur", "Emma", "Louis", "Jade", "Louise", "Lucas", "Adam", "Maël", "Jules", "Hugo", "Alice", "Liam", "Lina", "Chloé", "Noah", "Ethan", "Paul", "Mia", "Inès", "Léa", "Tiago", "Rose", "Mila", "Ambre", "Sacha", "Gabin", "Nathan", "Mohamed", "Anna", "Aaron", "Eden", "Julia", "Léna", "Tom", "Noé", "Théo", "Elena", "Léon", "Zoé", "Juliette", "Naël", "Manon", "Martin", "Mathis", "Eva", "Nolan", "Timéo", "Agathe", "Lou", "Lola", "Victor", "Nina", "Marius", "Enzo", "Jeanne", "Inaya", "Axel", "Romy", "Antoine", "Léonie", "Romane", "Iris", "Robin", "Isaac", "Luna", "Lucie", "Adèle", "Amir", "Valentin", "Rayan", "Sarah", "Louna", "Eliott", "Augustin", "Ayden", "Clément", "Charlotte", "Samuel", "Margaux", "Marceau", "Olivia", "Sofia", "Noûr", "Evan", "Yanis", "Mathéo", "Maxence", "Ibrahim", "Margot", "Malo", "Sohan", "Maxime", "Nino", "Simon", "Rafaël", "Lyam", "Mya", "Elise"],
    2018: ["Gabriel", "Raphaël", "Léo", "Louis", "Emma", "Lucas", "Jade", "Adam", "Louise", "Arthur", "Jules", "Hugo", "Maël", "Ethan", "Alice", "Chloé", "Liam", "Inès", "Paul", "Lina", "Nathan", "Léa", "Gabin", "Sacha", "Rose", "Noah", "Léna", "Anna", "Mila", "Tom", "Mohamed", "Mia", "Ambre", "Elena", "Julia", "Théo", "Aaron", "Eden", "Noé", "Timéo", "Juliette", "Victor", "Martin", "Mathis", "Lou", "Zoé", "Nolan", "Enzo", "Lola", "Eva", "Axel", "Agathe", "Jeanne", "Léon", "Antoine", "Naël", "Lucie", "Marius", "Robin", "Nina", "Sarah", "Romane", "Inaya", "Valentin", "Charlotte", "Léonie", "Samuel", "Rayan", "Tiago", "Amir", "Augustin", "Adèle", "Romy", "Iris", "Luna", "Louna", "Eliott", "Sofia", "Maxence", "Margaux", "Léana", "Mathéo", "Gaspard", "Evan", "Clémence", "Alexandre", "Isaac", "Olivia", "Yanis", "Elise", "Simon", "Imrân", "Clara", "Nino", "Malo", "Rafaël", "Kylian", "Marceau", "Ibrahim", "Victoire"],
    2017: ["Gabriel", "Emma", "Raphaël", "Léo", "Louis", "Adam", "Jules", "Lucas", "Louise", "Jade", "Maël", "Ethan", "Arthur", "Nathan", "Liam", "Alice", "Chloé", "Inès", "Paul", "Léa", "Lina", "Mila", "Tom", "Manon", "Léna", "Sacha", "Noah", "Gabin", "Nolan", "Enzo", "Mohamed", "Rose", "Timéo", "Anna", "Zoé", "Théo", "Aaron", "Lola", "Ambre", "Mathis", "Mia", "Juliette", "Noé", "Axel", "Victor", "Lou", "Antoine", "Valentin", "Sarah", "Lucie", "Jeanne", "Martin", "Eden", "Eva", "Naël", "Romane", "Rayan", "Robin", "Marius", "Agathe", "Nina", "Léon", "Baptiste", "Léonie", "Maxime", "Charlotte", "Samuel", "Inaya", "Evan", "Mathéo", "Yanis", "Eliott", "Sofia", "Margaux", "Augustin", "Louna", "Luna", "Clara", "Elise", "Alexandre", "Léana", "Thomas", "Simon", "Gaspard", "Adèle", "Amir", "Tiago", "Clémence", "Rafaël", "Olivia", "Isaac", "Anaïs", "Lana", "Ibrahim", "Nino", "Lyam", "Kaïs", "Capucine", "Ismaël", "Imrân"],
    2016: ["Raphaël", "Jules", "Emma", "Adam", "Lucas", "Louis", "Louise", "Ethan", "Jade", "Hugo", "Chloé", "Liam", "Maël", "Nathan", "Arthur", "Inès", "Léa", "Alice", "Paul", "Mila", "Léna", "Nolan", "Lina", "Manon", "Sacha", "Tom", "Noah", "Timéo", "Enzo", "Lola", "Théo", "Gabin", "Zoé", "Rose", "Mohamed", "Mathis", "Aaron", "Sarah", "Juliette", "Ambre", "Lucie", "Julia", "Clément", "Axel", "Eva", "Noé", "Antoine", "Elena", "Victor", "Romane", "Maxime", "Baptiste", "Eden", "Martin", "Jeanne", "Yanis", "Mia", "Rayan", "Lou", "Léonie", "Valentin", "Charlotte", "Louna", "Marius", "Nina", "Clara", "Evan", "Inaya", "Lana", "Maëlys", "Agathe", "Thomas", "Sofia", "Alexandre", "Samuel", "Clémence", "Léon", "Elise", "Anaïs", "Lilou", "Simon", "Lenny", "Léana", "Augustin", "Rafaël", "Théa", "Eliott", "Olivia", "Tiago", "Adèle", "Lyam", "Mathilde", "Gaspard", "Margot", "Capucine", "Kaïs", "Imrân", "Luna", "Victoria", "Ibrahim"],
    2015: ["Gabriel", "Jules", "Raphaël", "Léo", "Lucas", "Louis", "Louise", "Adam", "Emma", "Hugo", "Ethan", "Jade", "Chloé", "Inès", "Nathan", "Arthur", "Léa", "Paul", "Manon", "Nolan", "Timéo", "Maël", "Théo", "Lina", "Léna", "Lola", "Sacha", "Tom", "Zoé", "Noah", "Gabin", "Mohamed", "Mathis", "Sarah", "Anna", "Lucie", "Mila", "Juliette", "Rose", "Axel", "Ambre", "Noé", "Baptiste", "Eva", "Louna", "Aaron", "Martin", "Elena", "Antoine", "Victor", "Yanis", "Maëlys", "Rayan", "Jeanne", "Mathéo", "Valentin", "Clara", "Robin", "Nina", "Evan", "Louane", "Léonie", "Maxence", "Lou", "Lilou", "Alexandre", "Inaya", "Eden", "Clémence", "Margaux", "Charlotte", "Naël", "Marius", "Mia", "Lenny", "Agathe", "Adèle", "Simon", "Alexis", "Samuel", "Léon", "Elsa", "Lana", "Tiago", "Sofia", "Rafaël", "Léana", "Elise", "Olivia", "Kaïs", "Gaspard", "Mathilde", "Alicia", "Margot", "Esteban", "Noémie", "Ilyès", "Eliott", "Giulia", "Aya"]
}

# --- 3. INTERFACE WEB (STREAMLIT) ---
st.title("👶 Testeur d'Originalité")
st.write("Vérifiez si un prénom fait partie du Top 100 en France (2015-2024).")

prenom_saisi = st.text_input("Entrez un prénom :", "")

if st.button("Vérifier"):
    if prenom_saisi:
        signature_saisie = signature_prenom(prenom_saisi)
        nom_officiel_trouve = "" 
        details_trouves = [] # Liste pour stocker (rang, année)

        # Recherche dans toutes les années
        for annee, liste_noms in base_donnees.items():
            for nom_db in liste_noms:
                if signature_prenom(nom_db) == signature_saisie:
                    nom_officiel_trouve = nom_db
                    rang = liste_noms.index(nom_db) + 1
                    details_trouves.append((rang, annee))
                    break 

        nom_affichage = nom_officiel_trouve if nom_officiel_trouve else prenom_saisi.capitalize()

        if not details_trouves:
            st.success(f"Résultat pour {nom_affichage}")
            st.balloons()
            st.header("✨ Score : EXCELLENT")
            st.write("Ce prénom n'est jamais apparu dans le Top 100 sur les 10 dernières années.")
        else:
            # Calculs
            liste_rangs = [d[0] for d in details_trouves]
            moyenne = sum(liste_rangs) / len(liste_rangs)
            meilleur_rang, meilleure_annee = min(details_trouves)

            # Couleur selon originalité
            if moyenne <= 10: 
                niveau = "Mauvais (Très populaire)"
                couleur = "red"
            elif 10 < moyenne <= 50:
                niveau = "Passable"
                couleur = "orange"
            elif 50 < moyenne <= 80:
                niveau = "Acceptable"
                couleur = "orange"
            else:
                niveau = "Satisfaisant"
                couleur = "blue"

            # Affichage des résultats
            st.markdown(f"### Résultat pour **{nom_affichage}**")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(label="Années Top 100", value=f"{len(details_trouves)} / 10")
            with col2:
                st.metric(label="Moyenne", value=f"{moyenne:.1f}")
            with col3:
                st.metric(label="Meilleur", value=f"{meilleur_rang} ({meilleure_annee})")

            st.markdown(f"#### Score d'originalité : :{couleur}[{niveau}]")
