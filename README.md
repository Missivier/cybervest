 **Master 4 - GROUPE 9**

Projet Application Python (Tkinter)
(https://www.google.com/search?sca_esv=0fc881ea15ce3ce4&sxsrf=ACQVn09yv3U7LkcfVhDh9AGX1CgozfqtwQ:1710162101340&q=logo+uimm+bretagne&tbm=isch&source=lnms&sa=X&sqi=2&ved=2ahUKEwiV0rukouyEAxXCcvEDHY8UA_4Q0pQJegQIDRAB&biw=1920&bih=911&dpr=1#imgrc=zxnj2J6Oy254IM)
Entreprise - Cybervest 

Cybervest est une entreprise de fabrication de veste haut de gamme. Les produits se démarquent par différentes fonctionnalités. 


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



