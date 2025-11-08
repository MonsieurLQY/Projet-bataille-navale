# bateau.py

class Bateau:
    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        """
        ligne (int): 起始行号（必填）
        colonne (int): 起始列号（必填）
        longueur (int): 船的长度，默认为 1
        vertical (bool): 是否垂直放置，默认为 False（水平）
        """
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    @property
    def positions(self):
        """
        返回船在棋盘上的所有坐标列表。
        如果是水平的，则列变化；
        如果是垂直的，则行变化。
        """
        positions = []
        for i in range(self.longueur):
            if self.vertical:
                positions.append((self.ligne + i, self.colonne))
            else:
                positions.append((self.ligne, self.colonne + i))
        return positions
