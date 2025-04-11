# Projet



**Encadré par :** Professeur MIHI SOUKAINA

[a4paper,12pt]{article}
---
[utf8]{inputenc}
[french]{babel}
---

{0pt}
---

     % Vertical spacing at top (starred version for page top)
---
     % Horizontal centering
    (Redundant Array of Independent Disks)****}
---
    
    
---
    {****
    El Bessali Wahib \\
---
    Mouine Aya \\
    Zaynab Zidane \\
---
    Bouissoufar Maryrm \\
    ****}
---
    
    
---
    {****
    
---
     % Vertical spacing at bottom

Dans ce rapport, on présente de manière détaillée la technologie RAID. On y expose l'ensemble des définitions, explications, descriptions et comparaisons relatives à cette méthode (Redundant Array of Independent Disks). Conçue pour pallier les limites des disques durs individuels, la technologie RAID permet d’améliorer les performances, de renforcer la sécurité des données et d’augmenter la capacité de stockage grâce à la redondance et au regroupement de plusieurs supports de stockage.

## Présentation Générale du RAID

### Définition et Historique
Le RAID, ou Regroupement Redondant de Disques Indépendants, a été développé en 1987 par David Patterson, Garth Gibson et Randy Katz à l’Université de Californie à Berkeley. Cette technologie permet de combiner plusieurs disques durs (ou SSD) en une unité logique unique afin de :
---
[label={--}]
    - Renforcer la sécurité des données grâce à la redondance,
---
    - Augmenter la capacité de stockage.

Le RAID répond aux besoins essentiels suivants :
    - **Redondance des données :** La duplication ou la reconstruction des données sur plusieurs disques garantit leur disponibilité en cas de panne.
---
    - **Amélioration des performances :** L’utilisation simultanée de plusieurs disques (striping) permet d'accélérer les lectures et écritures.
    - **Capacité accrue :** Le regroupement de plusieurs disques permet d’obtenir un volume logique de grande taille facilitant l'extension du stockage.
---

## Les Différents Niveaux et Configurations du RAID
On décrit ici les différents niveaux de RAID ainsi que leurs caractéristiques.
---

### RAID 0 – Striping
---

#### Définition et Fonctionnement
---

#### Avantages
[label={--}]
---
    - **Performances accrues :** Accélération des vitesses de lecture et d’écriture.
    - **Utilisation totale de la capacité :** Aucun espace n'est perdu pour la parité.
---

#### Limites
---

    - **Absence de tolérance aux pannes :** La défaillance d’un disque entraîne la perte totale des données.
---
    - **Risque accru :** La répartition sur plusieurs disques augmente la probabilité de défaillance.

Le RAID 1 s’appuie sur la technique du **mirroring** : les données sont copiées sur au moins deux disques. Chaque opération d’écriture est ainsi dupliquée, garantissant une redondance complète.
#### Avantages
---

    - **Haute sécurité :** Les données demeurent disponibles même en cas de défaillance d’un disque.
---
    - **Tolérance aux pannes :** Le disque en miroir prend le relais en cas de panne.

#### Limites
[label={--}]
---
    - **Coût élevé :** Nécessite l'achat de disques supplémentaires (capacité utile réduite de moitié).

### Comparaison : RAID 0 vs RAID 1
---

    - **Opération principale :** RAID 0 utilise le striping tandis que RAID 1 mise sur le mirroring.
---
    - **Coût et capacité :** RAID 0 offre 100\% de capacité utilisable, contre 50\% pour RAID 1.

### RAID 5 – Striping avec Parité
---

#### Définition et Fonctionnement
---

#### Avantages et Limites
[label={--}]
---
    - **Tolérance aux pannes :** Peut supporter la défaillance d’un disque.
    - **Limite :** En cas d'échec de deux disques simultanément, la récupération des données est impossible.
---

### RAID 6 – Striping avec Double Parité

#### Définition et Fonctionnement
Le RAID 6 est une évolution du RAID 5 qui ajoute une seconde parité. Ce mécanisme double permet au système de supporter la défaillance simultanée de deux disques.
---

[label={--}]
    - **Performance d'écriture :** Légèrement inférieure à celle du RAID 5 en raison du calcul supplémentaire de la parité.
---
    - **Coût :** Nécessite un minimum de quatre disques, ce qui augmente le coût.

  { | l | l | l | }
**Caractéristique**            & **RAID 5** & **RAID 6** \\ 
---
Nombre minimal de disques           & 3              & 4               \\ 
Tolérance aux pannes                & 1 disque       & 2 disques       \\ 
---
Performances d'écriture             & Plus rapide    & Un peu plus lent\\ 

### RAID 50 et RAID 60 – Configurations Hybrides
---

#### RAID 50
---

Le RAID 50 combine plusieurs groupes RAID 5, chacun bénéficiant de la parité, qui sont ensuite agrégés en RAID 0 pour améliorer les performances globales.
---
****agraph{Avantages et Inconvénients}
    - **Avantages :**
---
    [label={****$$}]
        - Tolérance à la défaillance d’un disque par groupe.
---
        - Capacité utile élevée.
    - **Inconvénients :**
---
    [label={****$$}]
        - Configuration complexe.
---
    

****agraph{Définition et Fonctionnement}
****agraph{Avantages et Inconvénients}
---
[label={--}]
    [label={****$$}]
---
        - Excellente tolérance aux pannes grâce à la double parité.
    
---
    - **Inconvénients :**
        - Capacité brute réduite, car deux disques par groupe sont utilisés pour la parité.
---
        - Performances d’écriture légèrement inférieures.
    
---

### RAID 10 – Mirroring + Striping

#### Définition et Fonctionnement
Le RAID 10 (ou RAID 1+0) combine le mirroring et le striping. On configure d’abord des paires de disques en miroir, puis on répartit les données entre ces paires pour obtenir à la fois sécurité et rapidité d’accès.
---

[label={--}]
    - **Haute tolérance aux pannes :** Chaque paire peut tolérer la défaillance d’un disque.
---
    - **Reconstruction rapide :** En cas de panne, le système reconstruit rapidement les données à partir des miroirs.

#### Limites
[label={--}]
---
    - **Coût élevé :** Nécessite le double de disques pour obtenir la capacité utile désirée.
    - **Configuration complexe :** Demande une gestion rigoureuse de l'administration et de la surveillance.
---

## Démonstration Pratique : Mise en Place d’un RAID via VirtualBox sous Ubuntu
Dans cette section, on décrit les huit étapes suivies pour mettre en place un environnement RAID à l'aide de VirtualBox et Ubuntu, accompagnées de captures d’écran.
---

### Étape 1 : Ajout de Disques Virtuels
---

[width=0.8]{step1.png}

**Description :** On a démarré la machine Ubuntu et utilisé une commande de liste des blocs pour vérifier que les nouveaux disques étaient reconnus par le système.\\
[width=0.8]{step2.png}
---

### Étape 3 : Installation de {mdadm
**Description :** On a installé {mdadm}, l’outil indispensable pour créer et gérer des ensembles RAID sous Linux.\\
---

### Étape 4 : Création de l’Ensemble RAID
---

[width=0.8]{step4.png}

**Description :** On a formaté l’ensemble RAID avec un système de fichiers approprié et monté le volume dans un répertoire pour faciliter l’accès aux données.\\
[width=0.8]{step5.png}
---

### Étape 6 : Configuration du Montage Automatique
**Description :** On a modifié la configuration du système afin que l’ensemble RAID se monte automatiquement au démarrage de la machine.\\
---

### Étape 7 : Simulation d’une Défaillance de Disque
---

[width=0.8]{step7.png}

**Description :** On a retiré le disque défaillant puis l’a réintégré dans l’ensemble RAID afin de reconstruire le volume et rétablir son intégrité.\\
[width=0.8]{step8.png}
---

## Conclusion
Ce rapport présente en détail la technologie RAID, en décrivant ses différents niveaux et en démontrant, étape par étape, son implémentation pratique via VirtualBox sous Ubuntu. Ce projet de groupe permet de mieux comprendre les avantages et les compromis de chaque configuration RAID ainsi que les aspects pratiques liés à leur mise en œuvre. Nous espérons que ce travail contribuera à une compréhension approfondie de cette technologie.
---