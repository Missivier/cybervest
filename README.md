 **Master 4 - GROUPE 9**

Projet Application Python (Tkinter)

Entreprise - Cybervest 

![Logo UIMM](https://github.com/Missivier/cybervest/blob/main/images/logo-uimm-250x250.jpg)
![Logo Cybervest](https://github.com/Missivier/cybervest/blob/main/images/Logo1.png)

Cybervest est une entreprise de fabrication de veste haut de gamme. Les produits se démarquent par différentes fonctionnalités. 

![Logo bouee](https://github.com/Missivier/cybervest/blob/main/images/Vestes/veste_bouee.png)
![Logo chauffante](https://github.com/Missivier/cybervest/blob/main/images/Vestes/veste_chauffante.png)
![Logo parachute](https://github.com/Missivier/cybervest/blob/main/images/Vestes/veste_parachute.png)
![Logo refrigeree](https://github.com/Missivier/cybervest/blob/main/images/Vestes/veste_refrigeree.png)

**PROJET**

Cybervest évolue vers une organisation industrielle 4.0 en évoluant l'organisation de la production avec la mise en place d'un ERP (Odoo).
Pour cela, le service informatique a pour but d'intégrer une application pour intéragir avec l'ERP et la BDD. 

Fonctions demandées: - le déploiement de l'ERP ODoo avec sa BDD
                     - création des comptes (Admin, Logistique, Production, Vente/Commercial)
                     - une page logistique avec l'affichage des articles (nom, code, prix, image) et un bouton pour modifier les quantités d'articles en stock
                     - une page production avec l'affichage des OFs (numéro, date, quantité à produire) et un bouton pour modifier les quantités produites 
                     - l'accès aux différentes pages est controlé avec une identification avec un user et un mdp



**Prérequis**

Pour le déploiement de l'application, il faut: - Python 3
                                               - Pip 3 (Généralement installé automatiquement avec Python3)
                                               


**Installation**

***1. Ouvrir l'invite de commande***

***2. Se rendre dans le répertoire Documents***

***3. Cloner le projet GitHub***


***4. Installation des packages PIP***

***5. Déployer docker***
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



