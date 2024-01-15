

import os
import pyttsx3
from PyPDF2 import PdfReader

robot = pyttsx3.init()
robot.say("bonjour je suis sarah")
robot.say("je vais te faire la lecture écoute")


def pdf_en_texte(chemin_pdf):
    txt = ""
    with open(chemin_pdf, "rb") as fichier_pdf:
        lecteur_pdf = PdfReader(fichier_pdf)
        for page_num in range(len(lecteur_pdf.pages)):
            page = lecteur_pdf.pages[page_num]
            txt += page.extract_text()
    return txt

def synthese_vocale(txt):
    moteur_synthese = pyttsx3.init()
    moteur_synthese.say(txt)
    moteur_synthese.runAndWait()

if __name__ == "__main__":
    chemin_pdf = os.path.abspath("test.pdf")  # Spécifié le chemin absolu du fichier PDF
    if os.path.exists(chemin_pdf):
        txt_pdf = pdf_en_texte(chemin_pdf)

        if txt_pdf:
            print("Contenu extrait du PDF :\n", txt_pdf)
            synthese_vocale(txt_pdf)
        else:
            print("Erreur lors de l'extraction du texte.")
    else:
        print(f"Le fichier PDF '{chemin_pdf}' n'a pas été trouvé.")
