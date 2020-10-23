import templates as temp
from tkinter import *

codes = {
    "avocat": temp.Code_lettres("avocat", "a", "k"),
    "cassette": temp.Code_chiffres("cassette", "k", 7),
    "cesar": temp.Code_lettres("cesar", "a", "x")
}

print("Bienvenue sur Dcrypte !")

running = True

while running:
    action = input("Encoder ou decoder un message ? (e/d)(Quitter : q) : ")

    if action == "e":
        msg = input("Entrez le message à encoder :\n")
        msg = msg.lower()

        choice = input("Choisissez le code avec lequel encoder le message (Tapez \"help\" si vous ne connaisssez pas les codes disponibles) :\n")

        if choice == "help":
            print("Codes disponibles :")
            for code in codes:
                print(code)

        elif choice in codes:
            print("Message encodé :")
            print(codes[choice].encoder(msg))
            r = Tk()
            r.withdraw()
            r.clipboard_clear()
            r.clipboard_append(codes[choice].encoder(msg))
            r.update()
            r.destroy()
            print("Copié dans le presse papier")

        else:
            print("Code inconnu...")

    elif action == "d":
        msg = input("Entrez le message à décoder :\n")
        msg = msg.lower()

        choice = input("Choisissez le code dans lequel a été encodé le message :\n")

        if choice in codes:
            print("Message décodé :")
            print(codes[choice].decoder(msg))

        else:
            print("Code inconnu...")

    elif action == "q":
        running = False
