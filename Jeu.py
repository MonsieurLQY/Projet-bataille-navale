import random
from grille import Grille
from bateau_4types import PorteAvion, Croiseur, Torpilleur, SousMarin
from story_bateau import chevauchent
# --------------------
# 将航空母舰和巡洋舰随机放置在网格上，确保不重叠
# Placer aléatoirement le Porte-Avion et le Croiseur sur la grille, en veillant à ce qu'ils ne se chevauchent pas
# --------------------
def creer_bateaux(lignes=8, colonnes=10):
    
    while True:
        # Generate random positions and orientations for both ships
        grille_cache = Grille(lignes, colonnes)

        x1 = random.randint(0, lignes-1)
        y1 = random.randint(0, colonnes-1)
        est_vertical1 = random.choice([True, False])
        b1 = PorteAvion(x1, y1, est_vertical1)

        x2 = random.randint(0, lignes-1)
        y2 = random.randint(0, colonnes-1)
        est_vertical2 = random.choice([True, False])
        b2 = Croiseur(x2, y2, est_vertical2)

        # Try placing both ships
        if grille_cache.ajoute(b1):
            if grille_cache.ajoute(b2) and not chevauchent(b1, b2):
                return b1, b2
           
        
if __name__ == "__main__":

    touche="💣"
    
    LIGNES, COLONNES = 8, 10
    b1, b2 = creer_bateaux(LIGNES, COLONNES)
    grille = Grille(LIGNES, COLONNES)
    grille.ajoute(b1)
    grille.ajoute(b2)

    print(grille) # Affiche la grille complète (pour le débogage) deletez cette ligne si vous ne voulez pas voir les bateaux
   
    print("=== Bataille navale ===")
    print("Grille: 8 lignes x 10 colonnes. Entrez les coordonnées (ligne, colonne).")
    print("Tapez Ctrl+C pour quitter.")
    
    # 为了在船沉没后显示其原始图标，在主循环里维护已沉没船的集合并使用自定义显示函数
    # Pour afficher les icônes d'origine des navires après leur naufrage, maintenir un ensemble de navires coulés et utiliser une fonction d'affichage personnalisée dans la boucle principale
    bateaux = [b1, b2]
    pos_to_bateau = {}
    for b in bateaux:
        for p in b.positions:
            pos_to_bateau[p] = b

    bateaux_coules = set()
    nombre_coups = 0  # 计数总击次 / Compter le nombre total de tirs

    def afficher_personnalisee(grille, pos_to_bateau, bateaux_coules, touche="💣"):
        """按要求显示：
        - 已射中的位置用 'x' 表示
        - 命中标记使用 touche
        - 对于已沉没的船，显示其原始图标
        - 其他格子显示 '~'
        
        Affichage selon les exigences :
        - Les positions touchées mais manquées affichent 'x'
        - Les coups qui ont touché un navire affichent le caractère touche
        - Pour les navires coulés, afficher leur icône d'origine
        - Les autres cellules affichent '~'
        """
        lignes = []
        for i in range(grille.lignes):
            ligne = []
            for j in range(grille.colonnes):
                idx = i * grille.colonnes + j
                contenu = grille.matrice[idx]
                pos = (i, j)
                if contenu == 'x':
                    ch = 'x'
                elif contenu == touche:
                    ch = touche
                else:
                    bateau = pos_to_bateau.get(pos)
                    if bateau is not None and bateau in bateaux_coules:
                        ch = bateau.marque
                    else:
                        ch = '~'
                ligne.append(ch)
            lignes.append("".join(ligne))
        print("\n".join(lignes))

    try:
        while True:
            afficher_personnalisee(grille, pos_to_bateau, bateaux_coules, touche=touche)
            # Demande coup
            try:
                x = int(input("Ligne (0-7) : "))
                y = int(input("Colonne (0-9) : "))
            except ValueError:
                print("Veuillez entrer des entiers valides.")
                continue

            grille.tirer(x, y, touche=touche)
            nombre_coups += 1  # 每次击中后累加计数 / Incrémenter le compteur après chaque tir

            # 检测船只是否刚刚被击沉；如果被击沉，将其标记为已沉没并在格子上显示原始图标
            # Vérifier si un navire vient d'être coulé; s'il l'est, le marquer comme coulé et afficher son icône d'origine sur la grille
            for b in bateaux:
                if b not in bateaux_coules and b.coule(grille, touche=touche):
                    bateaux_coules.add(b)
                    # 将船的所有格子写回为船的图标，便于后续（和调试）观察
                    # Réécrire toutes les cellules du navire avec son icône d'origine pour une observation ultérieure (et un débogage)
                    for (xx, yy) in b.positions:
                        if 0 <= xx < grille.lignes and 0 <= yy < grille.colonnes:
                            grille.matrice[xx * grille.colonnes + yy] = b.marque
                    print(f"Le bateau {b.marque} est coulé!")

            # 检测游戏是否结束（使用已记录的沉没集合）
            # Vérifier si le jeu est terminé (en utilisant l'ensemble des navires coulés enregistrés)
            if len(bateaux_coules) == len(bateaux):
                afficher_personnalisee(grille, pos_to_bateau, bateaux_coules, touche=touche)
                print("Tous les bateaux sont coulés !")
                print(f"Nombre total de coups: {nombre_coups}")
                break
    except KeyboardInterrupt:
        print("\nJeu terminé.") 