from bateau import Bateau

class PorteAvion(Bateau):
    """长度4，标志 🚢"""
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=4, vertical=vertical)
        self.marque = "🚢"

class Croiseur(Bateau):
    """长度3，标志 🚤"""
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=3, vertical=vertical)
        self.marque = "🚤"


class Torpilleur(Bateau):
    """长度2，标志 🛶"""
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)
        self.marque = "🛶"


class SousMarin(Bateau):
    """长度2，标志 🐋"""
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)
        self.marque = "🐋"