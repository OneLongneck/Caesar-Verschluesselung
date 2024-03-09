zahlen = []
text = []

def Verschlüsseln():
    for x in inputbuchstaben:
        zahlen.append((ord(x) - 96 + Rotzahl) % 26)        # weist jedem Buchstaben der Liste die dazugehörige Zahl anhand der Reihenfolge im Alphabet zu

def Entschlüsseln():
    for x in inputbuchstaben:
        zahlen.append((ord(x) - 96 - Rotzahl) % 26)

    Ausgabe = "".join(text)
    print("Entschlüsselt ergibt dein Text:\n" + Ausgabe)

Auswahl = input("Gib für Verschlüsseln 1 ein, für Entschlüsseln 2\n")
Eingabe = input("Was möchtest du Ver-/Entschlüsseln?\n")
Rotzahl = int(input("Was ist die Rotationszahl?\n"))

inputbuchstaben = [*Eingabe]  # wandelt den eingegebenen String in eine Liste der einzelnen Buchstaben um

if Auswahl == "1":
    Verschlüsseln()
elif Auswahl == "2":
    Entschlüsseln()

for y in zahlen:
        text.append(chr(y + 96))

Ausgabe = "".join(text)
print("Dein neuer Text ist:\n" + Ausgabe)