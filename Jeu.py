import random
from grille import Grille
from bateau_4types import PorteAvion, Croiseur, Torpilleur, SousMarin
from story_bateau import chevauchent
# --------------------
# 将航空母舰和巡洋舰随机放置在网格上，确保不重叠
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

    print(grille)
    print("=== Bataille navale ===")
    print("Grille: 8 lignes x 10 colonnes. Entrez les coordonnées (ligne, colonne).")
    print("Tapez Ctrl+C pour quitter.")
    
    try:
        while True:
            grille.afficher(touche="💣")
            # Demande coup
            try:
                x = int(input("Ligne (0-7) : "))
                y = int(input("Colonne (0-9) : "))
            except ValueError:
                print("Veuillez entrer des entiers valides.")
                continue
            grille.tirer(x, y, touche="💣")
            # 检测所有的船是否沉没
            for b in [b1, b2]:
                if b.coule(grille,touche="💣"):
                    print(f"Le bateau {b.marque} est coulé!")
            # 检测游戏是否结束
            if b1.coule(grille,touche="💣") and b2.coule(grille,touche="💣"):
                print("Tous les bateaux sont coulés !")
                break
    except KeyboardInterrupt:
        print("\nJeu terminé.") 