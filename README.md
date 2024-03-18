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
![Logo astronaute](https://github.com/Missivier/cybervest/blob/main/images/Vestes/veste_astronaute.png)

## **Prérequis**

Pour le déploiement de l'application, il faut: - 3PC's avec Windows
                                               - 3VM's  --> Pour le PC1, une VM Linux Debian11 avec Docker, une image Odoo V15 et une image PostgreSQL v13 
                                                        --> Pour le PC2, une VM Linux Debian11 avec Python 3.9
                                                        --> Pour le PC3, une VM Windows 10 avec Python 3.9
                                               - une SSD avec les 3 VM's et le projet avec un dossier odoo pour le PC1 et un dossier application pour le PC2 et PC3
                                               - Connexion Wi-fi SSID: afpicfai_wifi_guest pour les 3PC's 
                                               
## **Installation**

### *** Installation des VM's sur les PC's***
  1. Ouvrir Oracle
  2. Cliquer sur Ajouter
  3. Sélectionner la VM1 sur le PC1 (Master Debian 11), la VM2 sur le PC2 (Base Debian 11), la VM2 sur le PC2 (Windows 10)
  4. Sur chaque VM, cliquer sur Configuration
  5. Dans l'onglet Réseau, changer le paramètre "Mode d'accès réseau" par "Accès par pont"
  6. Pour lancer les VM's, il suffit de cliquer sur Démarrer

### *** Déployer docker (Sur la PC1)***
  1. Rendez-vous sur [ce lien](http://localhost:9000/)
  2. Sélectionner **Stacks** dsans le menu de la liste de gauche
     
     ![Image Stack](https://github.com/Missivier/cybervest/blob/main/images/Stacks.png)
     
  4. Cliquer sur **AddStack** pour ajouter un stack

     ![Image AddStack](https://github.com/Missivier/cybervest/blob/main/images/Add%20stack.png)

  5. Donner un nom ici "odoo70"

     ![Image odoo70](https://github.com/Missivier/cybervest/blob/main/images/odoo70.png)


  6. Sélectionner **Web editor**

     ![Image Web editor](https://github.com/Missivier/cybervest/blob/main/images/Web%20editor.png)
     
  8. Copier le fichier "docker-compose.yml" du projet GitHub ou copier le code suivant

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

     ![Image Web editor](https://github.com/Missivier/cybervest/blob/main/images/Deploy%20the%20stack.png)

  8. Vos images **Odoo** et **Postgres** doivent passer en **running**
     
      ![Image en run](https://github.com/Missivier/cybervest/blob/main/images/Image%20en%20run.png)

### ***2. Installation du Serveur ERP sur une machine virtuelle Linux***
  1. Accès au Serveur ERP
  Rendez-vous sur [ce lien](http://localhost:8069/)
  2. Backup ERP odoo
     Récuperer le Fichier .zip présent dans le dossier odoo
  Cliquer sur restore data base 
  
   ![Image en run](https://github.com/Missivier/cybervest/blob/main/images/restore%20database.png)
  
  Entrez le mot de passe principal (jslpdl), parcourez et sélectionnez le fichier .ZIP téléchargé dans le même répertoire que le référentiel cloné.
  Nommez votre base de données "db_cybervest".
  
  ![Image en run](https://github.com/Missivier/cybervest/blob/main/images/zip.png)
     
  3. 

  4. Modification du réglage reseau (VM)

Modifiez les paramètres réseau pour passer en mode pont.
Déconnectez et reconnectez-vous du réseau WiFi de la machine virtuelle pour appliquer les modifications.

### ***3. Installation de l'application sur Linux***
  1. Récupération de l'application
Dans le SSD, récupérer le dossier "Application", et le glisser dans le dossier "Mes documents"

  3. Installation des Dépendances
 ```
pip install -r requierement_linux.txt
  ```
  4. Lancement de l'Application

Ouvrez le fichier "App.py". Exécutez le code en appuyant sur Run ou F5 et connectez-vous avec vos identifiants ERP.

   ![Image Web editor](https://github.com/Missivier/cybervest/blob/main/images/app.py.png)
   ![Image Web editor](https://github.com/Missivier/cybervest/blob/main/images/run.png)
      
### ***4. Installation du Desktop pour Windows***
  1. Configuration du Réseau

Connectez-vous au réseau "afpicfai_wifi_guests" et passez les paramètres réseau de votre VM en mode pont. Redémarrez la VM.

   ![Image Web editor](https://github.com/Missivier/cybervest/blob/main/images/wifi.png)

  3. Récupération du Code
Dans l

  5. Installation des Dépendances
 ```
pip install -r requierement_windows.txt
  ```

  6. Lancement de l'Application

Ouvrez le fichier "App.py". Exécutez le code en appuyant sur Run ou F5 et connectez-vous avec vos identifiants ERP.

   ![Image Web editor](https://github.com/Missivier/cybervest/blob/main/images/app.py.png)
   ![Image Web editor](https://github.com/Missivier/cybervest/blob/main/images/run.png)

























