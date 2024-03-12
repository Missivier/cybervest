# **Master 4 - GROUPE 9**

## **PROJET**

Cybervest évolue vers une organisation industrielle 4.0 en évoluant l'organisation de la production avec la mise en place d'un ERP (Odoo).
Pour cela, le service informatique a pour but d'intégrer une application pour intéragir avec l'ERP et la BDD. Cybervest est une entreprise de fabrication de veste haut de gamme. Les produits se démarquent par différentes fonctionnalités. 

## **Fonctions demandées**

- Le déploiement de l'ERP Odoo avec sa BDD
- Création des comptes (Admin, Logistique, Production, Vente/Commercial)
- Une page logistique avec l'affichage des articles (nom, code, prix, image) et un bouton pour modifier les quantités d'articles en stock
- Une page production avec l'affichage des OFs (numéro, date, quantité à produire) et un bouton pour modifier les quantités produites 
- L'accès aux différentes pages est controlé avec une identification avec un user et un mdp

## **Entreprise**

![Logo UIMM](https://github.com/Missivier/cybervest/blob/main/images/logo-uimm-250x250.jpg)
![Logo Cybervest](https://github.com/Missivier/cybervest/blob/main/images/Logo1.png)

## **Produits**

![Logo bouee](https://github.com/Missivier/cybervest/blob/main/images/Vestes/veste_bouee.png "Veste Bouée")
![Logo chauffante](https://github.com/Missivier/cybervest/blob/main/images/Vestes/veste_chauffante.png "Veste Chauffante")
![Logo parachute](https://github.com/Missivier/cybervest/blob/main/images/Vestes/veste_parachute.png "Veste Parachute")
![Logo refrigeree](https://github.com/Missivier/cybervest/blob/main/images/Vestes/veste_refrigeree.png "Veste Réfrigérée")
![Logo astronaute](https://github.com/Missivier/cybervest/blob/main/images/Vestes/veste_astronaute.png "Veste Astronaute")

## **Prérequis**

Pour le déploiement de l'application, il faut: - Python 3
                                               - Pip 3 (Généralement installé automatiquement avec Python3)
                                               


## **Installation**

### ***1. Déployer docker***
  1. Rendez-vous sur le lient suivant: "http://localhost:9000/"
  2. Sélectionner **Stack** dsans le menu de la liste de gauche
  3. Cliquer sur **AddStack** pour ajouter un stack
  4. Donner un nom ici "odoo70"
  5. Sélectionner **Web editor**
  6. Copier le fichier "docker-compose.yml" du projet GitHub ou copier le code suivant

**Code**:
  ```
  version: '2'
  services :
    web:
      image: odoo:15
      depends_on:
        - mydb
      ports:
        - "8069:8069"
      environment:
       - HOST=mydb
       - USER=odoo
       - PASSWORD=myodoo
    mydb: 
       image: postgres:13
       environment:
         - POSTGRES_DB=postgres
         - POSTGRES_PASSWORD=myodoo
         - POSTGRES_USER=odoo
  ```
  7. Cliquer sur **Deploy the stack**
  8. Vos images **Odoo** et **Postgres** doivent passer en **running**
![Image en run](https://github.com/Missivier/cybervest/blob/main/images/Image%20en%20run.png)

### ***2. Installation du Serveur ERP sur une machine virtuelle Linux***
  1. Récupération du Serveur ERP
 ```
git clone https://github.com/Missivier/cybervest
  ```
  2. Accès au Serveur ERP Odoo

Ouvrez le serveur ERP Odoo dans votre navigateur en accédant à ce lien : http://localhost:8069 ou en cliquant sur "8069" dans la colonne "published ports" du Docker fraîchement créé.

  3. Restauration de la Base de Données

Sur le site, accédez à "Gestion des bases de données" puis sélectionnez "Restore Database".
Entrez le mot de passe principal (MSIR5), parcourez et sélectionnez le fichier .ZIP téléchargé dans le même répertoire que le référentiel cloné.
Nommez votre base de données "cybervest".

  4. Configuration de l'Adresse IP

Changez l'adresse IP de votre machine virtuelle hébergeant le Docker en 172.31.11.241.
Modifiez les paramètres réseau pour passer en mode pont.
Déconnectez et reconnectez-vous du réseau WiFi de la machine virtuelle pour appliquer les modifications.

### ***3. Installation du Desktop sur Linux***
  1. Configuration du Réseau

Connectez-vous au réseau "afpicfai_wifi_guests" et passez les paramètres réseau de votre VM en mode pont. Redémarrez la VM.

  2. Récupération du Code
 ```
git clone https://github.com/Missivier/cybervest
  ```
  3. Installation des Dépendances
 ```
pip install -r requierement_linux.txt
  ```
  4. Lancement de l'Application

Ouvrez le fichier "App.py". Exécutez le code en appuyant sur Run ou F5 et connectez-vous avec vos identifiants ERP.

### ***4. Installation du Desktop pour Windows***
  1. Configuration du Réseau

Connectez-vous au réseau "afpicfai_wifi_guests" et passez les paramètres réseau de votre VM en mode pont. Redémarrez la VM.

 2. Installation de Git Bash
    
Téléchargez et installez Git Bach depuis [ce lien](https://git-scm.com/download/win) en sélectionnant "64-bit Git for Windows Setup".

  3. Récupération du Code
 ```
git clone https://github.com/Missivier/cybervest
  ```

  4. Installation de Python

Installez Python en ouvrant l'invite de commande et en tapant python3. Suivez les instructions pour installer à partir du Microsoft Store.
Vérifiez si Python s'est correctement installé en tapant python --version dans l'invite de commande.

  5. Installation des Dépendances
 ```
pip install -r requierement_windows.txt
  ```

  6. Lancement de l'Application

Ouvrez le fichier "App.py". Exécutez le code en appuyant sur Run ou F5 et connectez-vous avec vos identifiants ERP.

























