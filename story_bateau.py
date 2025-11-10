# story_bateau.py
# User Story : "chevauchement"
# Objectif : vérifier si deux bateaux se chevauchent ou non

from bateau import Bateau

def chevauchent(b1, b2):
    """Retourne True si deux bateaux se chevauchent (ont au moins une position commune)."""
    return any(pos in b2.positions for pos in b1.positions)

'''
# --- Cas 1 : deux bateaux qui SE chevauchent ---
b1 = Bateau(2, 3, longueur=3)            # [(2,3), (2,4), (2,5)]
b2 = Bateau(2, 4, longueur=2)            # [(2,4), (2,5)] => chevauchement
print("Cas 1 : chevauchent =", chevauchent(b1, b2))  # ✅ True


# --- Cas 2 : deux bateaux qui NE se chevauchent PAS ---
b3 = Bateau(0, 0, longueur=2)
b4 = Bateau(1, 0, longueur=3, vertical=True)
print("Cas 2 : chevauchent =", chevauchent(b3, b4))  # ✅ False
'''