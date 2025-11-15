# 🚢 Bataille navale — 战舰游戏 / 海战游戏

欢迎来到 **Bataille navale**，一个基于终端的经典海战游戏！这是一个中文/法文双语项目。

**快速开始** | **Quick Start**

```powershell
python Jeu.py
```

---

## 📖 简介（中文）

这是一个基于终端的"Battleship / 海战"小游戏。程序会在 8 行 x 10 列的网格上随机放置两艘船：
- **航空母舰 🚢**（长度 4 格）
- **巡洋舰 🚤**（长度 3 格）

玩家通过输入行列坐标来进行射击，目标是击沉全部船只，并在游戏结束时看到用时总数。

### 游戏特点

✨ **核心功能**
- 网格大小：8 行（0-7）× 10 列（0-9）
- 两艘船随机放置（确保不重叠）
- 实时显示网格与击沉状态
- 击沉后的船只显示原始图标
- 统计总击次数

🎮 **游戏机制**
- 输入行与列坐标进行射击
- `x` 表示已射击过的空海
- `💣` 表示命中的位置
- 原始船图标（🚢/🚤）显示已沉没的船
- `~` 表示未探索的海水

### 系统要求

- **Python** 3.7 或更高版本
- **编码** 建议 UTF-8（用于正确显示 emoji）
- **操作系统** Windows/Linux/Mac（任何支持 Python 的系统）

### 设置编码（Windows PowerShell）

如果 emoji 显示不正确，先运行：

```powershell
chcp 65001
```

然后再启动游戏。

### 快速开始

#### 步骤 1：进入项目目录
```powershell
cd d:\python\code\projet-bataille-navale
```

#### 步骤 2：运行游戏
```powershell
python Jeu.py
```

#### 步骤 3：输入坐标进行射击
```
Ligne (0-7) : 3
Colonne (0-9) : 5
```

#### 步骤 4：击沉所有船只以赢得比赛
游戏会显示：
```
Tous les bateaux sont coulés !
Nombre total de coups: 23
```

### 游戏规则

1. 网格显示后，输入要射击的**行号**（0-7）
2. 再输入**列号**（0-9）
3. 系统会显示：
   - `Touché!` — 如果命中船只
   - 或无输出提示——如果射入空海（稍后会显示 `x`）
   - `Déjà tiré ici.` — 如果已经射击过该位置
4. 网格实时更新，显示你的射击结果
5. 当两艘船都被击沉时，显示总击次数并结束游戏
6. 按 **Ctrl+C** 可随时退出

### 游戏示例

```
~~~~~~~~💣~
x💣💣💣~~~~
~~~~🚤~~~~~
~~~~~~~~~~ 
~~~~~~~~x~
~~~~~🚤~~~
~~~~~~~~~~
~~~~~~~~~~

Ligne (0-7) : 3
Colonne (0-9) : 2

Touché!

Nombre total de coups: 12
```

---

## 📖 Présentation (français)

**Bataille navale** est un petit jeu classique de bataille navale joué dans le terminal. Le programme place aléatoirement deux navires sur une grille 8x10 :
- **Porte-Avion 🚢** (longueur 4)
- **Croiseur 🚤** (longueur 3)

Le joueur entre des coordonnées (ligne, colonne) pour tirer et tenter de couler tous les navires. À la fin du jeu, le nombre total de coups est affiché.

### Caractéristiques du jeu

✨ **Fonctionnalités principales**
- Grille : 8 lignes (0-7) × 10 colonnes (0-9)
- Deux navires placés aléatoirement sans chevauchement
- Affichage en temps réel de la grille
- Les navires coulés affichent leur icône d'origine
- Comptage du nombre total de tirs

🎮 **Mécanique du jeu**
- Entrez des coordonnées (ligne, colonne) pour tirer
- `x` représente une case déjà tirée (vide)
- `💣` représente un coup qui a touché
- Icône originale (🚢/🚤) affiche les navires coulés
- `~` représente l'eau inexplorée

### Prérequis système

- **Python** 3.7 ou supérieur
- **Encodage** recommandé UTF-8 (pour afficher correctement les emojis)
- **Système d'exploitation** Windows/Linux/Mac (tout système supportant Python)

### Configuration de l'encodage (Windows PowerShell)

Si les emojis ne s'affichent pas correctement, exécutez d'abord :

```powershell
chcp 65001
```

Puis lancez le jeu.

### Démarrage rapide

#### Étape 1 : Accédez au répertoire du projet
```powershell
cd d:\python\code\projet-bataille-navale
```

#### Étape 2 : Lancez le jeu
```powershell
python Jeu.py
```

#### Étape 3 : Entrez les coordonnées pour tirer
```
Ligne (0-7) : 2
Colonne (0-9) : 4
```

#### Étape 4 : Coulez tous les navires pour gagner
Le jeu affichera :
```
Tous les bateaux sont coulés !
Nombre total de coups: 18
```

### Règles du jeu

1. Après l'affichage de la grille, entrez le **numéro de ligne** (0-7)
2. Puis entrez le **numéro de colonne** (0-9)
3. Le système affiche :
   - `Touché!` — si vous avez touché un navire
   - ou rien — si vous avez manqué (affichera `x` plus tard)
   - `Déjà tiré ici.` — si vous avez déjà tiré sur cette case
4. La grille se met à jour en temps réel
5. Quand les deux navires sont coulés, le nombre total de tirs s'affiche et le jeu se termine
6. Appuyez sur **Ctrl+C** pour quitter à tout moment

### Exemple de partie

```
~~~~~~~~💣~
x💣💣💣~~~~
~~~~🚤~~~~~
~~~~~~~~~~
~~~~~~~~x~
~~~~~🚤~~~
~~~~~~~~~~
~~~~~~~~~~

Ligne (0-7) : 1
Colonne (0-9) : 3

Touché!
Le bateau 🚤 est coulé!

Nombre total de coups: 15
```

---

## 📁 Structure du projet

| Fichier | Description |
|---------|-------------|
| `Jeu.py` | Point d'entrée du jeu（游戏入口）|
| `grille.py` | Classe Grille et opérations（网格类及操作）|
| `bateau.py` | Classe Bateau de base（船舶基类）|
| `bateau_4types.py` | Définition des 4 types de navires（四种船舶定义）|
| `story_bateau.py` | Utilitaires pour les navires（船舶工具函数）|
| `story_grille.py` | Utilitaires pour la grille（网格工具函数）|
| `test_*.py` | Tests unitaires（单元测试）|
| `requirements.txt` | Dépendances Python（Python 依赖）|

---

## 🛠️ Installation & Configuration

### Prérequis
- Python 3.7+
- pip (gestionnaire de paquets Python)

### Installation

1. **克隆或下载项目** / **Cloner ou télécharger le projet**
   ```powershell
   # Clonez depuis GitHub ou téléchargez le ZIP
   git clone https://github.com/MonsieurLQY/Projet-bataille-navale.git
   cd Projet-bataille-navale
   ```

2. **创建虚拟环境**（推荐）/ **Créer un environnement virtuel** (recommandé)
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **安装依赖** / **Installer les dépendances**
   ```powershell
   pip install -r requirements.txt
   ```

4. **运行游戏** / **Lancer le jeu**
   ```powershell
   python Jeu.py
   ```

---

## 🐛 Dépannage / 故障排除

| Problème / 问题 | Solution / 解决方案 |
|---|---|
| Les emojis ne s'affichent pas correctement / emoji 显示不正确 | Exécutez `chcp 65001` avant de lancer le jeu / 运行游戏前先运行 `chcp 65001` |
| `ModuleNotFoundError` | Installez les dépendances avec `pip install -r requirements.txt` / 用 `pip install -r requirements.txt` 安装依赖 |
| Entrée non valide / 输入无效 | Entrez uniquement des entiers valides entre 0-7 (ligne) et 0-9 (colonne) / 只输入 0-7 之间的行号和 0-9 之间的列号 |
| Python non trouvé / 找不到 Python | Assurez-vous que Python 3.7+ est installé et dans le PATH / 确保 Python 3.7+ 已安装并在 PATH 中 |

---

## 👨‍💻 Auteur / 作者

**MonsieurLQY**

---

## 📜 License / 许可证

Ce projet est fourni à titre éducatif. / 此项目仅供教育用途。

---

**祝你游戏愉快！** 🎮 **Bon jeu !**
