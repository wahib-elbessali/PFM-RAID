# PFM : Technologie RAID (Redundant Array of Independent Disks)

## Réalisé par
- El Bessali Wahib
- Mouine Aya
- Ait Himmi Amina
- Zaynab Zidane
- Bouissoufar Maryrm
- Rhim Nizar

## Encadré par
**Professeur MIHI SOUKAINA**

## Introduction
Dans ce rapport, nous présentons de manière détaillée la technologie RAID. L'objectif est d'exposer l'ensemble des définitions, explications, descriptions et comparaisons relatives à cette méthode (Redundant Array of Independent Disks). Conçue pour pallier les limites des disques durs individuels, la technologie RAID permet d’améliorer les performances, de renforcer la sécurité des données et d’augmenter la capacité de stockage grâce à la redondance et au regroupement de plusieurs supports de stockage.

## Présentation Générale du RAID
### Définition et Historique
Le RAID a été développé en 1987 à l’Université de Californie à Berkeley. Il combine plusieurs disques durs en une unité logique unique afin de :
- Améliorer les performances
- Renforcer la sécurité des données
- Augmenter la capacité de stockage

### Besoins et Avantages
- **Redondance des données** : garantit la disponibilité en cas de panne
- **Amélioration des performances** : grâce au striping
- **Tolérance aux pannes** : selon les niveaux RAID
- **Capacité accrue** : volume logique plus important

## Les Différents Niveaux de RAID

### RAID 0 – Striping
**Fonctionnement** : Les données sont divisées en blocs et écrites séquentiellement sur plusieurs disques.

**Avantages** :
- Performances accrues
- Implémentation simple
- Capacité totale utilisée

**Limites** :
- Aucune tolérance aux pannes
- Risque de perte totale

### RAID 1 – Mirroring
**Fonctionnement** : Les données sont dupliquées sur plusieurs disques.

**Avantages** :
- Haute sécurité
- Tolérance aux pannes

**Limites** :
- Coût élevé
- Écriture plus lente

### Comparaison RAID 0 vs RAID 1
- **RAID 0** : performance, 100% capacité utilisée, aucun backup
- **RAID 1** : sécurité, 50% capacité utilisée, duplication

### RAID 5 – Striping avec Parité
**Fonctionnement** : Striping avec ajout de blocs de parité, nécessite au moins 3 disques.

**Avantages** :
- Bonne tolérance aux pannes (1 disque)
- Bonne lecture

**Limites** :
- Écriture ralentie par le calcul de la parité
- Perte irréversible si 2 disques tombent en panne

### RAID 6 – Striping avec Double Parité
**Fonctionnement** : Comme le RAID 5, mais avec deux blocs de parité.

**Avantages** :
- Tolérance à 2 pannes simultanées
- Sécurité renforcée

**Limites** :
- Écriture plus lente que RAID 5
- Minimum 4 disques

### Comparaison RAID 5 vs RAID 6
| Caractéristique         | RAID 5 | RAID 6 |
|--------------------------|--------|--------|
| Nombre minimal de disques | 3      | 4      |
| Parité                  | Simple | Double |
| Tolérance aux pannes     | 1 disque | 2 disques |
| Performance d’écriture   | Plus rapide | Plus lente |

### RAID 50 – RAID 5 + RAID 0
**Fonctionnement** : Combinaison de plusieurs groupes RAID 5 en RAID 0.

**Avantages** :
- Performance accrue
- Tolérance à une panne par groupe
- Capacité utile élevée

**Inconvénients** :
- Moins résilient si plusieurs disques d’un groupe tombent
- Configuration complexe

### RAID 60 – RAID 6 + RAID 0
**Fonctionnement** : Groupes RAID 6 combinés en RAID 0

**Avantages** :
- Haute sécurité
- Tolérance à plusieurs pannes

**Inconvénients** :
- Capacité réduite
- Écriture plus lente
- Nombre de disques minimum élevé

### RAID 10 – Mirroring + Striping
**Fonctionnement** : Paires de disques en miroir, puis striping entre les paires.

**Avantages** :
- Performances élevées
- Haute tolérance aux pannes
- Reconstruction rapide

**Limites** :
- Coût très élevé
- Capacité utilisable = 50%

## Démonstration Pratique : RAID via VirtualBox sous Ubuntu
### Étapes :
1. **Ajout de Disques Virtuels** : Ajout de 4 disques dans VirtualBox 
2. **Vérification des Disques** : Liste des blocs sous Ubuntu
``` lsblk ```
3. **Installation de mdadm** : Outil RAID pour Linux
``` sudo apt install mdadm -y ```
4. **Création de RAID 10** : Utilisation des 4 disques
```
sudo mdadm --create /dev/md0 --level=10 --raid-devices=4 /dev/sdb /dev/sdc /dev/sdd /dev/sde
```
5. **Formatage et Montage** : Formatage et montage dans un dossier
```
sudo mkfs.ext4 /dev/md0
sudo mkdir /mnt/raid10
sudo mount /dev/md0 /mnt/raid10
```
6. **Montage Automatique** : Configuration pour montage au démarrage
```
echo "/dev/md0 /mnt/raid10 ext4 defaults 0 0" | sudo tee -a /etc/fstab
```
7. **Simulation de Défaillance** : Retrait d’un disque
```
sudo mdadm --fail /dev/md0 /dev/sdb
```
8. **Réintégration** : Récupération du RAID après ajout du disque
```
sudo mdadm --remove /dev/md0 /dev/sdb
sudo mdadm --add /dev/md0 /dev/sdb
```

## Conclusion
Ce rapport présente en détail la technologie RAID, ses différents niveaux, et une démonstration pratique via VirtualBox sous Ubuntu. Il permet de mieux appréhender les choix techniques possibles selon les besoins en performance, sécurité et coûts.

