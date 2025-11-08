class Grille:    
    def __init__(self, nombre_lignes, nombre_colonnes):
        # 使用一维列表模拟 L×C 的矩阵
        self.lignes = nombre_lignes
        self.colonnes = nombre_colonnes
        self.vide = "~"
        # 初始化时，全为 '~'
        self.matrice = [self.vide] * (self.lignes * self.colonnes)

    def tirer(self, ligne, colonne, touche='x'):
        """Tire sur (ligne, colonne).
        - 如果命中船（'⛵'），将该格替换为 touche（默认 'x'）并提示 `Touché!`
        - 如果是海水（'~'），仅提示 `Plouf!`（不把海水误标为 'x'）
        - 已经射击过的位置，提示 `Déjà tiré ici.`
        """
        if 0 <= ligne < self.lignes and 0 <= colonne < self.colonnes:
            index = ligne * self.colonnes + colonne
            contenu = self.matrice[index]
            if contenu == self.vide:
                print("Plouf! Tir dans l'eau.")
            elif contenu == touche:
                # 已经被标记过（可能是 'x' 或其他自定义 touche）
                print("Déjà tiré ici.")
            else:
                # 命中（例如 '⛵'）或其他未标记的目标
                self.matrice[index] = touche
                print("Touché!")
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

    def ajoute(self, bateau):
        """Place un bateau sur la grille en remplaçant par '⛵' aux positions du bateau.
        Ne fait rien (retourne False) si le bateau ne rentre pas entièrement dans la grille.
        Retourne True si le placement a été effectué.
        """
        # 验证所有格子都在网格内
        for (x, y) in bateau.positions:
            if not (0 <= x < self.lignes and 0 <= y < self.colonnes):
                return False
        # 放置船
        for (x, y) in bateau.positions:
            index = x * self.colonnes + y
            self.matrice[index] = bateau.marque
        return True
