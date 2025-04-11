PFM : Technologie RAID
(Redundant Array of Independent Disks)

Réalisé par
El Bessali Wahib

Mouine Aya

Ait Himmi Amina

Zaynab Zidane

Bouissoufar Maryrm

Rhim Nizar

Encadré par
Professeur MIHI SOUKAINA

Table des Matières
Introduction

Présentation Générale du RAID

Définition et Historique

Besoins et Avantages du RAID

Les Différents Niveaux et Configurations du RAID

RAID 0 – Striping

Définition et Fonctionnement

Avantages

Limites

RAID 1 – Mirroring

Définition et Fonctionnement

Avantages

Limites

Comparaison : RAID 0 vs RAID 1

RAID 5 – Striping avec Parité

Définition et Fonctionnement

Avantages et Limites

RAID 6 – Striping avec Double Parité

Définition et Fonctionnement

Avantages et Limites

Comparaison : RAID 5 vs RAID 6

RAID 50 et RAID 60 – Configurations Hybrides

RAID 50

Définition et Fonctionnement

Avantages et Inconvénients

RAID 60

Définition et Fonctionnement

Avantages et Inconvénients

RAID 10 – Mirroring + Striping

Définition et Fonctionnement

Avantages

Limites

Démonstration Pratique : Mise en Place d’un RAID via VirtualBox sous Ubuntu

Étape 1 : Ajout de Disques Virtuels

Étape 2 : Vérification des Disques

Étape 3 : Installation de mdadm

Étape 4 : Création de l’Ensemble RAID

Étape 5 : Formatage et Montage du RAID

Étape 6 : Configuration du Montage Automatique

Étape 7 : Simulation d’une Défaillance de Disque

Étape 8 : Récupération et Reconstruction du RAID

Conclusion

Introduction
Dans ce rapport, nous présentons de manière détaillée la technologie RAID. L'objectif est d'exposer l'ensemble des définitions, explications, descriptions et comparaisons relatives à cette méthode (Redundant Array of Independent Disks). Conçue pour pallier les limites des disques durs individuels, la technologie RAID permet d’améliorer les performances, de renforcer la sécurité des données et d’augmenter la capacité de stockage grâce à la redondance et au regroupement de plusieurs supports de stockage.

Présentation Générale du RAID
Définition et Historique
Le RAID, ou Regroupement Redondant de Disques Indépendants, a été développé en 1987 par David Patterson, Garth Gibson et Randy Katz à l’Université de Californie à Berkeley. Cette technologie permet de combiner plusieurs disques durs (ou SSD) en une unité logique unique afin de :

Améliorer les performances (vitesse de lecture/écriture),

Renforcer la sécurité des données grâce à la redondance,

Augmenter la capacité de stockage.

Besoins et Avantages du RAID
Le RAID répond aux besoins essentiels suivants :

Redondance des données : La duplication ou la reconstruction des données sur plusieurs disques garantit leur disponibilité en cas de panne.

Amélioration des performances : L’utilisation simultanée de plusieurs disques (striping) permet d'accélérer les lectures et écritures.

Tolérance aux pannes : Certains niveaux de RAID assurent le fonctionnement du système même en cas de défaillance de certains disques.

Capacité accrue : Le regroupement de plusieurs disques permet d’obtenir un volume logique de grande taille, facilitant ainsi l'extension du stockage.

Les Différents Niveaux et Configurations du RAID
RAID 0 – Striping
Définition et Fonctionnement
Le RAID 0 se base sur la technique du striping : les données sont découpées en blocs et distribuées de façon séquentielle sur plusieurs disques. Par exemple, un bloc de 64 Ko peut être réparti entre plusieurs disques, permettant un accès simultané et une amélioration notable des performances.

Avantages
Performances accrues : Accélération des vitesses de lecture et d’écriture.

Implémentation simple : La configuration est simple et économique.

Utilisation totale de la capacité : Aucun espace n'est perdu pour la parité.

Limites
Absence de tolérance aux pannes : La défaillance d’un disque entraîne la perte totale des données.

Risque accru : La répartition sur plusieurs disques augmente la probabilité de défaillance.

RAID 1 – Mirroring
Définition et Fonctionnement
Le RAID 1 s’appuie sur la technique du mirroring : les données sont copiées sur au moins deux disques. Chaque opération d’écriture est ainsi dupliquée, garantissant une redondance complète.

Avantages
Haute sécurité : Les données demeurent disponibles même en cas de défaillance d’un disque.

Tolérance aux pannes : Le disque en miroir prend le relais en cas de panne.

Limites
Coût élevé : Nécessite l'achat de disques supplémentaires (capacité utile réduite de moitié).

Écriture plus lente : Chaque opération d’écriture est effectuée plusieurs fois.

Comparaison : RAID 0 vs RAID 1
Opération principale : RAID 0 utilise le striping tandis que RAID 1 mise sur le mirroring.

Coût et capacité : RAID 0 offre 100% de capacité utilisable, contre 50% pour RAID 1.

Performances : RAID 0 est plus rapide, mais RAID 1 offre une meilleure sécurité.

RAID 5 – Striping avec Parité
Définition et Fonctionnement
Le RAID 5 combine la technique du striping avec l’ajout d’un bloc de parité. Les données sont réparties en blocs sur au moins trois disques, et un bloc de parité est calculé et réparti sur tous les disques, permettant ainsi la reconstruction des données en cas de panne d’un disque.

Avantages et Limites
Tolérance aux pannes : Peut supporter la défaillance d’un disque.

Performances : Offre de bonnes performances en lecture, bien que l'écriture soit ralentie par le calcul de la parité.

Limite : En cas d'échec de deux disques simultanément, la récupération des données est impossible.

RAID 6 – Striping avec Double Parité
Définition et Fonctionnement
Le RAID 6 est une évolution du RAID 5 qui ajoute une seconde parité. Ce mécanisme double permet au système de supporter la défaillance simultanée de deux disques.

Avantages et Limites
Tolérance améliorée : Permet de survivre à la panne de deux disques.

Performance d'écriture : Légèrement inférieure à celle du RAID 5 en raison du calcul supplémentaire de la parité.

Coût : Nécessite un minimum de quatre disques, ce qui augmente le coût.

Comparaison : RAID 5 vs RAID 6
Caractéristique	RAID 5	RAID 6
Nombre minimal de disques	3	4
Parité	Simple	Double
Tolérance aux pannes	1 disque	2 disques
Performances d'écriture	Plus rapide	Un peu plus lent
RAID 50 et RAID 60 – Configurations Hybrides
RAID 50
Définition et Fonctionnement
Le RAID 50 combine plusieurs groupes RAID 5, chacun bénéficiant de la parité, qui sont ensuite agrégés en RAID 0 pour améliorer les performances globales.

Avantages et Inconvénients
Avantages :

Performance améliorée grâce au striping sur les groupes RAID 5.

Tolérance à la défaillance d’un disque par groupe.

Capacité utile élevée.

Inconvénients :

Moins résilient si plusieurs disques d’un même groupe échouent.

Configuration complexe.

RAID 60
Définition et Fonctionnement
Le RAID 60 combine la double parité du RAID 6 avec le striping du RAID 0. Des groupes RAID 6 sont constitués puis agrégés pour obtenir un système à la fois performant et très tolérant aux pannes.

Avantages et Inconvénients
Avantages :

Excellente tolérance aux pannes grâce à la double parité.

Sécurité renforcée même en cas de défaillance multiple.

Inconvénients :

Capacité brute réduite, car deux disques par groupe sont utilisés pour la parité.

Performances d’écriture légèrement inférieures.

Nécessite un nombre minimum de disques élevé.

RAID 10 – Mirroring + Striping
Définition et Fonctionnement
Le RAID 10 (ou RAID 1+0) combine le mirroring et le striping. On configure d’abord des paires de disques en miroir, puis on répartit les données entre ces paires pour obtenir à la fois sécurité et rapidité d’accès.

Avantages
Performance élevée : Accès rapide en lecture et écriture grâce au striping.

Haute tolérance aux pannes : Chaque paire peut tolérer la défaillance d’un disque.

Reconstruction rapide : En cas de panne, le système reconstruit rapidement les données à partir des miroirs.

Limites
Coût élevé : Nécessite le double de disques pour obtenir la capacité utile désirée.

Capacité réduite : Seule la moitié de la capacité totale est utilisable.

Configuration complexe : Demande une gestion rigoureuse de l'administration et de la surveillance.

Démonstration Pratique : Mise en Place d’un RAID via VirtualBox sous Ubuntu
Dans cette section, nous décrivons les huit étapes suivies pour mettre en place un environnement RAID à l'aide de VirtualBox et Ubuntu, accompagnées de captures d’écran.

Étape 1 : Ajout de Disques Virtuels
Description :

Quatre disques durs virtuels supplémentaires ont été ajoutés à la machine Ubuntu dans VirtualBox pour simuler un environnement RAID.

(Capture d’écran : step1.png)

Étape 2 : Vérification des Disques
Description :

Démarrage de la machine Ubuntu et vérification via une commande de liste des blocs pour s’assurer que les nouveaux disques sont reconnus par le système.

(Capture d’écran : step2.png)

Étape 3 : Installation de mdadm
Description :

Installation de mdadm, l’outil indispensable pour créer et gérer des ensembles RAID sous Linux.

(Capture d’écran : step3.png)

Étape 4 : Création de l’Ensemble RAID
Description :

Création d’un ensemble RAID 10 en utilisant les 4 disques, combinant ainsi les avantages du mirroring et du striping.

(Capture d’écran : step4.png)

Étape 5 : Formatage et Montage du RAID
Description :

Formatage de l’ensemble RAID avec un système de fichiers approprié et montage du volume dans un répertoire pour faciliter l’accès aux données.

(Capture d’écran : step5.png)

Étape 6 : Configuration du Montage Automatique
Description :

Modification de la configuration du système afin que l’ensemble RAID se monte automatiquement au démarrage de la machine.

(Capture d’écran : step6.png)

Étape 7 : Simulation d’une Défaillance de Disque
Description :

Simulation de la défaillance d’un des disques du RAID pour observer la réaction du système face à une panne.

(Capture d’écran : step7.png)

Étape 8 : Récupération et Reconstruction du RAID
Description :

Retrait du disque défaillant suivi de sa réintégration dans l’ensemble RAID, permettant ainsi la reconstruction du volume et le rétablissement de son intégrité.

(Capture d’écran : step8.png)

Conclusion
Ce rapport présente en détail la technologie RAID, en décrivant ses différents niveaux et en démontrant, étape par étape, son implémentation pratique via VirtualBox sous Ubuntu. Ce projet de groupe permet de mieux comprendre les avantages et les compromis de chaque configuration RAID ainsi que les aspects pratiques liés à leur mise en œuvre. Nous espérons que ce travail contribuera à une compréhension approfondie de cette technologie.
