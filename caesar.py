zahlen = []
text = []

def Verschlüsseln():
    inputbuchstaben = [*Eingabe]  # wandelt den eingegebenen String in eine Liste der einzelnen Buchstaben um

    for x in inputbuchstaben:
        zahlen.append((ord(x) - 96 + Rotzahl) % 26)        # weist jedem Buchstaben der Liste die dazugehörige Zahl anhand der Reihenfolge im Alphabet zu
    for y in zahlen:
        text.append(chr(y + 96))

    Ausgabe = "".join(text)
    print("Verschlüsselt ergibt dein Text:\n" + Ausgabe)

def Entschlüsseln():
    inputbuchstaben = [*Eingabe]

    for x in inputbuchstaben:
        zahlen.append((ord(x) - 96 + Rotzahl) % 26)
    for y in zahlen:
        text.append(chr(y + 96))

    Ausgabe = "".join(text)
    print("Entschlüsselt ergibt dein Text:\n" + Ausgabe)

Auswahl = input("Gib für Verschlüsseln 1 ein, für Entschlüsseln 2\n")
Eingabe = input("Was möchtest du Ver-/Entschlüsseln?\n")
Rotzahl = int(input("Was ist die Rotationszahl?\n"))

if Auswahl == "1":
    Verschlüsseln()
elif Auswahl == "2":
    Entschlüsseln()