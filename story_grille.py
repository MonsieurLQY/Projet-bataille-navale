# story_grille.py
# User Story : "Plouf dans l'eau"
# Objectif : permettre à un joueur de tirer sur une grille et de visualiser le résultat.

from grille import Grille

#  创建一张 5x8 的网格
g = Grille(5, 8)

#  重复执行：显示网格 -> 请求输入 -> 射击 -> 重新显示
while True:
    # 显示当前网格
    print(g)
    
    # 请求玩家输入坐标
    try:
        x = int(input("Entrez la ligne (0-4) : "))
        y = int(input("Entrez la colonne (0-7) : "))
    except ValueError:
        print("Veuillez entrer des nombres valides !")
        continue  # 如果输入无效，重新输入

    # 射击指定位置
    g.tirer(x, y)

    # 返回步骤 2（循环继续）
    print("\n--- Nouvelle grille ---\n")
