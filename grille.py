class Grille:    
    def __init__(self, nombre_lignes, nombre_colonnes):
        # 使用一维列表模拟 L×C 的矩阵
        self.lignes = nombre_lignes
        self.colonnes = nombre_colonnes
        self.vide = "~"
        # 初始化时，全为 '~'
        self.matrice = [self.vide] * (self.lignes * self.colonnes)

    def tirer(self, ligne, colonne):
        # 将二维坐标转换为一维索引
        if 0 <= ligne < self.lignes and 0 <= colonne < self.colonnes:
            index = ligne * self.colonnes + colonne
            if self.matrice[index] == self.vide:
                self.matrice[index] = "x"
                print("Plouf! Tir dans l'eau.")
            else:
                print("Déjà tiré ici.")
        else:
            print("Coordonnées hors grille!")

    def __str__(self):
        # 将一维矩阵按行格式化成多行字符串
        lignes = []
        for i in range(self.lignes):
            debut = i * self.colonnes
            fin = debut + self.colonnes
            lignes.append("".join(self.matrice[debut:fin]))
        return "\n".join(lignes)