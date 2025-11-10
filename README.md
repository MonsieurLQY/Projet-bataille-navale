## Bataille navale — 使用说明 / Mode d'emploi

以下说明同时包含中文与法语。先读中文或法语任一部分来了解如何玩本游戏。

---

## 简介（中文）

这是一个基于终端的“Battleship / Bataille navale”小游戏。程序会在 8 行 x 10 列的网格上随机放置两艘船（航空母舰 Porte-Avion 和巡洋舰 Croiseur）。玩家通过输入格子的行与列来进行射击，目标是击沉全部船只。

主要特点：
- 网格大小：8 行（0-7） x 10 列（0-9）
- 随机放置两艘船（不重叠）
- 使用终端输入行/列来“射击”
- 使用 Ctrl+C 退出游戏

## 运行要求（中文）
- Python 3.7 或更高
- 在 Windows 的 PowerShell 下运行时，若要正确显示 emoji（例如 💣），建议将控制台编码改为 UTF-8：

```powershell
chcp 65001
```

（可选）若不想使用 emoji，也可以直接运行，会默认使用程序内定义的符号显示命中/未命中。

## 使用方法（中文）
1. 在项目根目录运行：

```powershell
python Jeu.py
```

2. 程序会显示网格并提示输入：
   - 输入行（Ligne）: 整数 0 到 7
   - 输入列（Colonne）: 整数 0 到 9
3. 每次输入后程序会在指定坐标处“开火”，并显示命中/未命中的状态。若输入无效（非整数或超范围），程序会提示重新输入。
4. 当所有船只被击沉时，程序会提示“Tous les bateaux sont coulés !”并结束。
5. 使用 Ctrl+C 可以随时终止游戏。

示例交互（中文说明）：
- 程序提示：Ligne (0-7) :  输入 3 回车
- 程序提示：Colonne (0-9) : 输入 5 回车

---

## Présentation (français)

Petit jeu “Bataille navale” en terminal. Deux bateaux sont placés aléatoirement sur une grille 8x10 : un Porte-Avion et un Croiseur. Le joueur entre des coordonnées (ligne, colonne) pour tirer et tenter de couler les bateaux.

Caractéristiques principales :
- Grille : 8 lignes (0-7) × 10 colonnes (0-9)
- Deux bateaux placés aléatoirement sans chevauchement
- Entrée clavier pour tirer
- Ctrl+C pour quitter

## Prérequis (français)
- Python 3.7 ou supérieur
- Sous Windows PowerShell, pour afficher correctement les emojis (ex. 💣) :

```powershell
chcp 65001
```

## Comment jouer (français)
1. Depuis la racine du projet lancez :

```powershell
python Jeu.py
```

2. Le jeu affiche la grille et demande :
   - Ligne (0-7) : saisir un entier
   - Colonne (0-9) : saisir un entier
3. Après chaque tir, l'état (touché / manqué) est mis à jour. Si l'entrée est invalide, le jeu en informe et redemande.
4. Quand tous les bateaux sont coulés, le jeu affiche : “Tous les bateaux sont coulés !” et se termine.
5. Appuyez sur Ctrl+C pour quitter à tout moment.

Exemple d'interaction (français) :
- Ligne (0-7) : 2
- Colonne (0-9) : 7

---

## Fichiers utiles
- `Jeu.py` : point d'entrée du jeu
- `grille.py` : implémentation de la grille et des opérations (ajout de bateau, tir, affichage)
- `bateau.py`, `bateau_4types.py` : définition des bateaux
- `test_*.py` : tests unitaires fournis pour certaines parties du projet

## Dépannage rapide
- 若遇到编码或 emoji 问题：在 PowerShell 运行 `chcp 65001` 并使用支持 UTF-8 的字体。
- 若输入后无反应或异常：请检查 Python 版本并确认在项目根目录运行 `python Jeu.py`。

---

祝你游戏愉快！ / Bon jeu !

