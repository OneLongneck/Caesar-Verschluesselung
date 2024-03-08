zahlen = []
text = []

def Verschlüsseln():
    inputbuchstaben = [*Eingabe]  # wandelt den eingegebenen String in eine Liste der einzelnen Buchstaben um

    for x in inputbuchstaben:
        zahlen.append(ord(x) + Rotzahl)        # weist jedem Buchstaben der Liste die dazugehörige Zahl anhand der Reihenfolge im Alphabet zu

    for y in zahlen:
        text.append(chr(y))

    Ausgabe = "".join(text)
    print("Verschlüsselt ergibt dein Tex:\n" + Ausgabe)

Auswahl = input("Gib 1 ein für Verschlüsseln, 2 für Entschlüsseln\n")
Eingabe = input("Was möchtest du Ver-/Entschlüsseln?\n")
Rotzahl = int(input("Was ist die Rotationszahl?\n"))

if Auswahl == "1":
    Verschlüsseln()
elif Auswahl == "2":
    Entschlüsseln()